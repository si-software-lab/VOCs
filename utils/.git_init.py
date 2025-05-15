import pathlib
import subprocess

# Check if .git directory exists
git_dir = pathlib.Path(".git")

if not git_dir.exists():
    print("Git not initialized. Running git init...")
    subprocess.run(["git", "init"])
else:
    print("Git already initialized.")
