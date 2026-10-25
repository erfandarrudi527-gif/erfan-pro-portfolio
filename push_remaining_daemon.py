import os
import subprocess
import time

CANDIDATES = [
    {
        "name": "parsa-sports-store",
        "path": "D:/عرفان/مدرسه عرفان/parsa",
        "desc": "Athletic Equipment & Apparel E-Commerce Storefront with Reactive Client State"
    },
    {
        "name": "cool-react-site",
        "path": "D:/عرفان/سایت های نمونه کار/cool-react-site",
        "desc": "Vite & React Modern Web Application"
    },
    {
        "name": "workplace-website-v2",
        "path": "D:/عرفان/سایت های نمونه کار/سایت محل کار 2",
        "desc": "Corporate & Workplace Enterprise Portal with Motion Systems"
    },
    {
        "name": "react-ecommerce-simple",
        "path": "D:/عرفان/سایت های نمونه کار/نمونه سایت فروشگاهی ساده با ری اکت",
        "desc": "React Simple E-Commerce Application with State Management"
    },
    {
        "name": "motion-sites-collection",
        "path": "D:/عرفان/سایت های نمونه کار/سایت های موشن دار",
        "desc": "Curated Collection of High-Fidelity Motion & Parallax Web Experiences"
    },
    {
        "name": "antigravity-fixer",
        "path": "D:/عرفان/نمونه کار/New folder (2)/antigravity-fixer",
        "desc": "Automated IDE Fixer & Code Quality Utility"
    },
    {
        "name": "safe-home-landing",
        "path": "D:/عرفان/نمونه کار/خانه امن",
        "desc": "Safe Home Real Estate & Security Landing Page"
    }
]

gh_exe = "C:/Program Files/GitHub CLI/gh.exe"

def ensure_gitignore(path):
    gi = os.path.join(path, ".gitignore")
    ignores = ["node_modules/", ".next/", "dist/", "build/", ".env*", "*.zip", "*.rar", "*.exe", ".freebuff/"]
    existing = ""
    if os.path.exists(gi):
        with open(gi, "r", encoding="utf-8", errors="ignore") as f:
            existing = f.read()
    to_add = [ig for ig in ignores if ig not in existing]
    if to_add:
        with open(gi, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(to_add) + "\n")

def push_one(p):
    name = p["name"]
    path = p["path"]
    desc = p["desc"]
    if not os.path.exists(path):
        return False
    ensure_gitignore(path)
    subprocess.run("git init", cwd=path, shell=True, capture_output=True)
    subprocess.run('git config user.name "Erfan Mehdi Sadeghi"', cwd=path, shell=True, capture_output=True)
    subprocess.run('git config user.email "erfandarrudi527@gmail.com"', cwd=path, shell=True, capture_output=True)
    subprocess.run("git branch -M main", cwd=path, shell=True, capture_output=True)
    subprocess.run("git add -A", cwd=path, shell=True, capture_output=True)
    subprocess.run(f'git commit -m "feat: initial release of {name}"', cwd=path, shell=True, capture_output=True)

    cmd = [gh_exe, "repo", "create", name, "--private", "--description", desc, "--source=.", "--remote=origin", "--push"]
    res = subprocess.run(cmd, cwd=path, capture_output=True, text=True)
    if res.returncode == 0 or "already exists" in res.stderr:
        print(f"SUCCESS: {name}")
        return True
    elif "too many repositories" in res.stderr.lower():
        print(f"RATE_LIMITED: {name} - {res.stderr.strip()}")
        return "rate_limited"
    else:
        print(f"FAILED: {name} - {res.stderr.strip()[:100]}")
        return False

if __name__ == "__main__":
    print("Daemon waiting for GitHub rate limit to clear...")
    for item in CANDIDATES:
        while True:
            status = push_one(item)
            if status == "rate_limited":
                print("Sleeping 90s for GitHub GraphQL rate limit...")
                time.sleep(90)
            else:
                time.sleep(15) # pause between creations to stay under rate limit
                break
    print("ALL REMAINING PROJECTS PUSHED.")
