import subprocess
import sys

def run_git_command(command):
    """Runs a terminal command and prints the output."""
    try:
        # Run the command and capture the output
        result = subprocess.run(command, check=True, shell=True, text=True, capture_output=True)
        print(f"✅ Success: {command}")
        if result.stdout.strip():
            print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {command}")
        print(e.stderr.strip())
        sys.exit(1) # Stop the script if a command fails

def push_portfolio_to_github(repo_url):
    """Automates the Git init, add, commit, and push process."""
    print("🚀 Starting GitHub push process...\n")

    # 1. Initialize the local directory as a Git repository
    run_git_command("git init")

    # 2. Add the index.html (and any other files in the folder) to staging
    run_git_command("git add .")

    # 3. Commit the changes
    commit_message = "Initial commit: Added portfolio website"
    # Using double quotes around the message for Windows/Mac compatibility
    run_git_command(f'git commit -m "{commit_message}"')

    # 4. Rename the default branch to 'main'
    run_git_command("git branch -M main")

    # 5. Link the local repository to your remote GitHub repository
    # First, we try to remove 'origin' just in case you ran this script before
    subprocess.run("git remote remove origin", shell=True, capture_output=True)
    run_git_command(f"git remote add origin {repo_url}")

    # 6. Push the code to GitHub
    print("\n⏳ Pushing to GitHub (this might ask for your credentials)...")
    run_git_command("git push -u origin main")
    
    print("\n🎉 Done! Your portfolio is now on GitHub at: " + repo_url)

if __name__ == "__main__":
    # --- IMPLEMENTATION ---
    # The URL has been updated to your specific repository
    GITHUB_REPO_URL = "https://github.com/prinson2006-bot/prince.git"
    
    push_portfolio_to_github(GITHUB_REPO_URL)