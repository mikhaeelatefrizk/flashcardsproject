import os
import subprocess
from pathlib import Path

def run_git_command(command, check=True):
    try:
        print(f"Executing: git {' '.join(command[1:])}")
        result = subprocess.run(command, check=check, capture_output=True, text=True)
        if result.returncode == 0:
            return result
        print(f"Warning: {result.stderr}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def setup_git():
    # Initialize git if not already initialized
    if not Path('.git').exists():
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Initial commit'])

def sync_with_github(repo_url):
    print(f"\nSynchronizing with {repo_url}")
    # Check if remote exists
    remote_exists = run_git_command(['git', 'remote', 'get-url', 'origin'], check=False)
    
    if remote_exists and remote_exists.returncode == 0:
        # Remove existing remote if URL is different
        current_url = remote_exists.stdout.strip()
        if current_url != repo_url:
            run_git_command(['git', 'remote', 'remove', 'origin'])
            run_git_command(['git', 'remote', 'add', 'origin', repo_url])
    else:
        # Add new remote
        run_git_command(['git', 'remote', 'add', 'origin', repo_url])
    
    # Push to GitHub
    run_git_command(['git', 'add', '.'])
    run_git_command(['git', 'commit', '-m', 'Update flashcards project'])
    result = run_git_command(['git', 'push', '-u', 'origin', 'main', '--force'])
    
    if result and result.returncode == 0:
        print("\nSuccessfully synchronized with GitHub!")
    else:
        print("\nSync completed with some warnings. Please check the messages above.")

if __name__ == '__main__':
    repo_url = input("Enter your GitHub repository URL: ")
    setup_git()
    sync_with_github(repo_url)
