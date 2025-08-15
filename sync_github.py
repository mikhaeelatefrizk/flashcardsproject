import os
import subprocess
from pathlib import Path

def setup_git():
    # Initialize git if not already initialized
    if not Path('.git').exists():
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Initial commit'])

def sync_with_github(repo_url):
    # Add remote if not exists
    try:
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url])
    except:
        pass
    
    # Push to GitHub
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Update flashcards project'])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])

if __name__ == '__main__':
    repo_url = input("Enter your GitHub repository URL: ")
    setup_git()
    sync_with_github(repo_url)
