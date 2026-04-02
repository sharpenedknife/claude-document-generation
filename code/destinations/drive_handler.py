"""
Google Drive Destination Handler
Uploads generated documents to Google Drive
"""

import os
import logging
import json
from typing import List, Dict, Any
from datetime import datetime

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth import default as auth_default
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', 'google-auth-oauthlib', 'google-auth-httplib2', 'google-api-python-client'])
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

SCOPES = ['https://www.googleapis.com/auth/drive.file']


class GoogleDriveHandler:
    """Upload documents to Google Drive"""
    
    def __init__(self, credentials_json: str = None, folder_id: str = None):
        self.credentials_json = credentials_json or os.getenv('GOOGLE_CREDENTIALS_JSON')
        self.folder_id = folder_id or os.getenv('GOOGLE_DRIVE_FOLDER_ID')
        
        if not self.folder_id:
            raise ValueError("GOOGLE_DRIVE_FOLDER_ID environment variable not set")
        
        self.service = self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Google Drive API"""
        
        creds = None
        token_file = 'token.json'
        
        # Try to load existing token
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        
        # If no valid credentials, perform OAuth flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_json:
                    raise ValueError("GOOGLE_CREDENTIALS_JSON required for initial authentication")
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_json, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save token for future use
            with open(token_file, 'w') as token:
                token.write(creds.to_json())
        
        return build('drive', 'v3', credentials=creds)
    
    def push(self, documents: List[Dict[str, Any]]) -> str:
        """
        Upload documents to Google Drive
        
        Returns:
            Folder URL
        """
        
        try:
            logger.info(f"Uploading {len(documents)} documents to Google Drive")
            
            # Create timestamped subfolder
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            subfolder_name = f"Docgen {timestamp}"
            
            subfolder_metadata = {
                'name': subfolder_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [self.folder_id]
            }
            
            subfolder = self.service.files().create(
                body=subfolder_metadata,
                fields='id'
            ).execute()
            
            subfolder_id = subfolder['id']
            logger.info(f"  ✓ Created folder: {subfolder_name}")
            
            # Upload documents
            for doc in documents:
                file_metadata = {
                    'name': doc['filename'],
                    'parents': [subfolder_id]
                }
                
                file_content = doc['content'].encode('utf-8')
                
                media = MediaFileUpload(
                    io.BytesIO(file_content).name,
                    mimetype='text/markdown',
                    resumable=True
                ) if False else None
                
                # Upload as text file
                try:
                    # Create temp file
                    import tempfile
                    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                        f.write(doc['content'])
                        temp_path = f.name
                    
                    media = MediaFileUpload(temp_path, mimetype='text/markdown', resumable=True)
                    
                    file_result = self.service.files().create(
                        body=file_metadata,
                        media_body=media,
                        fields='id, webViewLink'
                    ).execute()
                    
                    logger.info(f"  ✓ Uploaded: {doc['filename']}")
                    
                    # Clean up temp file
                    os.unlink(temp_path)
                
                except Exception as e:
                    logger.error(f"Failed to upload {doc['filename']}: {e}")
            
            # Upload metadata as JSON
            for doc in documents:
                metadata_name = doc['filename'].replace('.md', '_metadata.json')
                file_metadata = {
                    'name': metadata_name,
                    'parents': [subfolder_id]
                }
                
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                    json.dump(doc['metadata'], f, indent=2)
                    temp_path = f.name
                
                try:
                    media = MediaFileUpload(temp_path, mimetype='application/json', resumable=True)
                    self.service.files().create(
                        body=file_metadata,
                        media_body=media,
                        fields='id'
                    ).execute()
                    os.unlink(temp_path)
                except Exception as e:
                    logger.error(f"Failed to upload metadata: {e}")
            
            # Generate Drive folder URL
            drive_url = f"https://drive.google.com/drive/folders/{subfolder_id}"
            logger.info(f"  ✓ Uploaded to: {drive_url}")
            return drive_url
        
        except Exception as e:
            logger.error(f"Google Drive upload failed: {e}", exc_info=True)
            raise


class GoogleDriveAuthFlow:
    """OAuth flow for Google Drive authentication"""
    
    @staticmethod
    def get_auth_url(client_id: str = None, redirect_uri: str = None) -> str:
        """Generate Google OAuth authorization URL"""
        client_id = client_id or os.getenv('GOOGLE_CLIENT_ID')
        
        if not client_id:
            raise ValueError("GOOGLE_CLIENT_ID not set")
        
        return f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri or 'http://localhost:8080/callback'}&response_type=code&scope=https://www.googleapis.com/auth/drive.file"
    
    @staticmethod
    def exchange_code_for_token(code: str, client_id: str = None,
                               client_secret: str = None, redirect_uri: str = None) -> str:
        """Exchange OAuth code for access token"""
        import requests
        
        client_id = client_id or os.getenv('GOOGLE_CLIENT_ID')
        client_secret = client_secret or os.getenv('GOOGLE_CLIENT_SECRET')
        redirect_uri = redirect_uri or 'http://localhost:8080/callback'
        
        if not client_id or not client_secret:
            raise ValueError("GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET required")
        
        response = requests.post(
            'https://oauth2.googleapis.com/token',
            data={
                'code': code,
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            }
        )
        
        data = response.json()
        if 'error' in data:
            raise ValueError(f"OAuth error: {data['error_description']}")
        
        return data['access_token']


import io
