import os
import subprocess
from pathlib import Path
import time
import sys
from itertools import cycle

class Spinner:
    def __init__(self):
        self.spinner = cycle(['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏'])
    
    def spin(self, text):
        sys.stdout.write(f'\r{next(self.spinner)} {text}')
        sys.stdout.flush()

def run_git_command(command, check=True, show_spinner=True):
    spinner = Spinner()
    try:
        print(f"\nExecuting: git {' '.join(command[1:])}")
        if show_spinner:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while process.poll() is None:
                spinner.spin("Working...")
                time.sleep(0.1)
            stdout, stderr = process.communicate()
            result = subprocess.CompletedProcess(command, process.returncode, stdout, stderr)
        else:
            result = subprocess.run(command, check=check, capture_output=True, text=True)
        
        if result.returncode == 0:
            return result
        
        # Auto-retry on push failures
        if 'push' in command and result.returncode != 0:
            print("\nPush failed, retrying...")
            time.sleep(2)
            return run_git_command(command, check, show_spinner)
            
        print(f"\nWarning: {result.stderr}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"\nError: {e.stderr}")
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return None

def setup_git():
    # Initialize git if not already initialized
    if not Path('.git').exists():
        subprocess.run(['git', 'init'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Initial commit'])

def sync_with_github(repo_url):
    print(f"\nSynchronizing with {repo_url}")
    
    # Setup credential caching
    run_git_command(['git', 'config', '--global', 'credential.helper', 'store'])
    
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
