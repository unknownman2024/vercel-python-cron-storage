import os
from git import Repo
from datetime import datetime

GITHUB_USER = "unknownman2024"
GITHUB_REPO = "vercel-python-cron-storage"

GH_TOKEN = os.getenv("GH_TOKEN")
REMOTE_URL = f"https://{GH_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
LOCAL_PATH = "/tmp/repo"

def run():
    print("🚀 Cron Triggered")

    if not os.path.exists(LOCAL_PATH):
        print("📥 Cloning repository...")
        Repo.clone_from(REMOTE_URL, LOCAL_PATH)

    repo = Repo(LOCAL_PATH)

    filepath = os.path.join(LOCAL_PATH, "log.txt")
    with open(filepath, "a") as f:
        f.write(f"[{datetime.now()}] Cron Executed\n")

    repo.git.add(".")

    try:
        repo.git.commit("-m", "Automated Cron Update")
        print("📌 Committed changes.")
    except:
        print("⚠ No new changes.")

    repo.git.push()
    print("☑️ Pushed to GitHub.")

if __name__ == "__main__":
    run()