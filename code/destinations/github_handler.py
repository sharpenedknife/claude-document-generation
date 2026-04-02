"""
GitHub Destination Handler with OAuth
Pushes generated documents to GitHub repositories
"""

import os
import logging
from typing import List, Dict, Any
from datetime import datetime

try:
    from github import Github, GithubException
    from github import InputGitAuthor
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', 'PyGithub'])
    from github import Github, GithubException
    from github import InputGitAuthor

logger = logging.getLogger(__name__)


class GitHubHandler:
    """Push documents to GitHub repository"""
    
    def __init__(self, token: str = None, repo_url: str = None):
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.repo_url = repo_url or os.getenv('GITHUB_REPO_URL')
        
        if not self.token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
        if not self.repo_url:
            raise ValueError("GITHUB_REPO_URL environment variable not set")
        
        self.gh = Github(self.token)
        self.repo = self._parse_and_get_repo()
    
    def _parse_and_get_repo(self):
        """Parse repo URL and get repository object"""
        if self.repo_url.startswith('https://'):
            parts = self.repo_url.rstrip('/').split('/')
            owner, repo = parts[-2], parts[-1]
        else:
            owner, repo = self.repo_url.split('/')
        
        try:
            return self.gh.get_user(owner).get_repo(repo)
        except GithubException as e:
            raise ValueError(f"Failed to access repository {owner}/{repo}: {e}")
    
    def push(self, documents: List[Dict[str, Any]], branch: str = "main") -> str:
        """Push documents to GitHub"""
        
        try:
            logger.info(f"Pushing {len(documents)} documents to GitHub")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            commit_branch = f"docgen/{timestamp}"
            
            try:
                main_ref = self.repo.get_git_ref(f"heads/{branch}")
                base_sha = main_ref.object.sha
                self.repo.create_git_ref(f"refs/heads/{commit_branch}", base_sha)
            except GithubException:
                pass
            
            for doc in documents:
                filename = doc['filename']
                content = doc['content']
                file_path = f"docs/{filename}"
                
                try:
                    existing_file = self.repo.get_contents(file_path, ref=commit_branch)
                    self.repo.update_file(
                        path=file_path,
                        message=f"Update {filename} via Docgen",
                        content=content,
                        sha=existing_file.sha,
                        branch=commit_branch,
                        committer=InputGitAuthor("Docgen", "docgen@example.com")
                    )
                    logger.info(f"  ✓ Updated: {file_path}")
                except:
                    self.repo.create_file(
                        path=file_path,
                        message=f"Add {filename} via Docgen",
                        content=content,
                        branch=commit_branch,
                        committer=InputGitAuthor("Docgen", "docgen@example.com")
                    )
                    logger.info(f"  ✓ Created: {file_path}")
            
            try:
                pr = self.repo.create_pull(
                    title=f"📚 Docgen: Generated documentation ({timestamp})",
                    body=f"Automated documentation generated via Docgen.\n\nDocuments:\n" + 
                         "\n".join(f"- {doc['filename']}" for doc in documents),
                    head=commit_branch,
                    base=branch
                )
                logger.info(f"  ✓ Created PR: #{pr.number}")
                return f"{self.repo.html_url}/pull/{pr.number}"
            except Exception as e:
                logger.warning(f"Failed to create PR: {e}")
                return self.repo.html_url
        
        except Exception as e:
            logger.error(f"GitHub push failed: {e}", exc_info=True)
            raise
