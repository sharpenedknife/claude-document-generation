"""
Notion Destination Handler
Syncs generated documents to Notion workspace
"""

import os
import logging
import json
from typing import List, Dict, Any
from datetime import datetime

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', 'requests'])
    import requests

logger = logging.getLogger(__name__)


class NotionHandler:
    """Sync documents to Notion database"""
    
    def __init__(self, token: str = None, database_id: str = None):
        self.token = token or os.getenv('NOTION_TOKEN')
        self.database_id = database_id or os.getenv('NOTION_DATABASE_ID')
        
        if not self.token:
            raise ValueError("NOTION_TOKEN environment variable not set")
        if not self.database_id:
            raise ValueError("NOTION_DATABASE_ID environment variable not set")
        
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """Make API request to Notion"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == "POST":
                response = requests.post(url, headers=self.headers, json=data)
            elif method == "PATCH":
                response = requests.patch(url, headers=self.headers, json=data)
            elif method == "GET":
                response = requests.get(url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            if response.status_code >= 400:
                logger.error(f"Notion API error: {response.text}")
                raise Exception(f"Notion API error: {response.status_code}")
            
            return response.json() if response.text else {}
        
        except Exception as e:
            logger.error(f"Notion request failed: {e}")
            raise
    
    def push(self, documents: List[Dict[str, Any]]) -> str:
        """
        Add documents to Notion database
        
        Returns:
            Notion database URL
        """
        
        try:
            logger.info(f"Syncing {len(documents)} documents to Notion")
            
            for doc in documents:
                # Create page in database
                page_data = {
                    "parent": {"database_id": self.database_id},
                    "properties": {
                        "Name": {
                            "title": [
                                {
                                    "text": {"content": doc['filename']}
                                }
                            ]
                        },
                        "Status": {
                            "status": {"name": doc['metadata'].get('status', 'Draft')}
                        },
                        "Quality": {
                            "number": doc['metadata'].get('quality_score', 0)
                        },
                        "Category": {
                            "select": {"name": doc['metadata'].get('category', 'General')}
                        },
                        "Date": {
                            "date": {"start": datetime.now().isoformat()}
                        }
                    },
                    "children": [
                        {
                            "object": "block",
                            "type": "heading_1",
                            "heading_1": {
                                "rich_text": [
                                    {"type": "text", "text": {"content": doc['filename']}}
                                ]
                            }
                        },
                        {
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [
                                    {
                                        "type": "text",
                                        "text": {
                                            "content": f"Quality Score: {doc['metadata'].get('quality_score', 'N/A')}/100"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "object": "block",
                            "type": "code",
                            "code": {
                                "language": "markdown",
                                "rich_text": [
                                    {
                                        "type": "text",
                                        "text": {"content": doc['content'][:2000]}  # First 2000 chars
                                    }
                                ]
                            }
                        }
                    ]
                }
                
                response = self._make_request("POST", "/pages", page_data)
                logger.info(f"  ✓ Created: {doc['filename']} (Page ID: {response.get('id', 'N/A')})")
            
            db_url = f"https://www.notion.so/{self.database_id.replace('-', '')}"
            logger.info(f"  ✓ Synced to Notion database")
            return db_url
        
        except Exception as e:
            logger.error(f"Notion sync failed: {e}", exc_info=True)
            raise


class NotionAuthFlow:
    """OAuth flow for Notion authentication"""
    
    @staticmethod
    def get_auth_url(client_id: str = None, redirect_uri: str = None) -> str:
        """Generate Notion OAuth authorization URL"""
        client_id = client_id or os.getenv('NOTION_CLIENT_ID')
        redirect_uri = redirect_uri or os.getenv('NOTION_REDIRECT_URI')
        
        if not client_id or not redirect_uri:
            raise ValueError("NOTION_CLIENT_ID and NOTION_REDIRECT_URI required")
        
        return f"https://api.notion.com/v1/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    
    @staticmethod
    def exchange_code_for_token(code: str, client_id: str = None,
                               client_secret: str = None, redirect_uri: str = None) -> str:
        """Exchange OAuth code for access token"""
        
        client_id = client_id or os.getenv('NOTION_CLIENT_ID')
        client_secret = client_secret or os.getenv('NOTION_CLIENT_SECRET')
        redirect_uri = redirect_uri or os.getenv('NOTION_REDIRECT_URI')
        
        if not all([client_id, client_secret, redirect_uri]):
            raise ValueError("NOTION_CLIENT_ID, NOTION_CLIENT_SECRET, NOTION_REDIRECT_URI required")
        
        import base64
        auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        
        response = requests.post(
            'https://api.notion.com/v1/oauth/token',
            headers={'Authorization': f'Basic {auth}'},
            json={
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': redirect_uri
            }
        )
        
        data = response.json()
        if 'error' in data:
            raise ValueError(f"OAuth error: {data.get('error_description', data['error'])}")
        
        return data['access_token']
