import os
import subprocess

class GitHubManager:
    def __init__(self, folder_path=r"E:\Excel Agent"):
        self.path = folder_path
        os.chdir(self.path)

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)

    def initialize_repo(self, repo_url):
        print("--- Initializing Git Repository ---")
        commands = [
            "git init",
            f"git remote add origin {repo_url}",
            "git branch -M main"
        ]
        for cmd in commands:
            print(self.run_command(cmd))

    def sync_to_github(self, commit_message="Update from Network Agent"):
        print(f"--- Syncing to GitHub: {commit_message} ---")
        commands = [
            "git add .",
            f'git commit -m "{commit_message}"',
            "git push origin main"
        ]
        for cmd in commands:
            print(self.run_command(cmd))

if __name__ == "__main__":
    manager = GitHubManager()
    print("GitHub Manager Agent Ready.")
    # Example usage (Uncomment after installing Git and creating a repo):
    # manager.initialize_repo("https://github.com/yourusername/your-repo.git")
    # manager.sync_to_github("Finalizing BOQ and RF Designs")
