import os
import subprocess
import sys

PROJECTS = [
    {
        "name": "erfan-pro-portfolio",
        "path": "C:/Users/erfan/Desktop/erfan-pro-portfolio",
        "desc": "Personal Portfolio & Interactive OS for Erfan Mehdi Sadeghi (Deployed on Vercel)"
    },
    {
        "name": "qreet-cms",
        "path": "C:/Users/erfan/Desktop/qreet-cms",
        "desc": "Enterprise Headless CMS built with Next.js 15, Prisma ORM, and TipTap Editor"
    },
    {
        "name": "dun-coffee-roastery",
        "path": "D:/عرفان/نمونه کار/پروژه/DUN",
        "desc": "Specialty Coffee Roastery & Interactive Brew Lab Extraction Calculator (#020101 Aesthetic)"
    },
    {
        "name": "webdev-master-learning-hub",
        "path": "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub",
        "desc": "Multi-Track Web Development Learning Hub & In-Browser Code Sandboxes"
    },
    {
        "name": "barg-reader-app",
        "path": "D:/عرفان/نمونه کار/barg",
        "desc": "Distraction-Free Book Reader PWA with High-Precision RTL Typography & APK Pipeline"
    },
    {
        "name": "parsa-sports-store",
        "path": "D:/عرفان/مدرسه عرفان/parsa",
        "desc": "Athletic Equipment & Apparel E-Commerce Platform with Reactive Client State"
    },
    {
        "name": "habit-tracker-pwa",
        "path": "D:/عرفان/اپ/habit-app",
        "desc": "Minimalist Habit & Goal Tracker PWA with Contribution Heatmaps"
    },
    {
        "name": "nova-ui-design-system",
        "path": "D:/عرفان/سایت های نمونه کار/nova-ui",
        "desc": "Modular Dark-Mode UI Component System & Analytics Dashboard Kit"
    },
    {
        "name": "taaghche-book-platform",
        "path": "D:/عرفان/مدرسه عرفان/taaghche-project",
        "desc": "React 18 & Vite Digital Bookstore & Reader Discovery Platform"
    },
    {
        "name": "skymission-studio",
        "path": "D:/عرفان/سایت های نمونه کار/skymission-studio-with-style-controls (1)",
        "desc": "Interactive Creative Agency Showcase with Dynamic Style Controls"
    },
    {
        "name": "hotel-reservation-system",
        "path": "D:/عرفان/مدرسه عرفان/Hotel",
        "desc": "Comprehensive Hotel Reservation System with Dynamic Rate Engine"
    }
]

def run(cmd, cwd=None):
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    return res.returncode == 0, res.stdout + res.stderr

def ensure_gitignore(path):
    gi = os.path.join(path, ".gitignore")
    ignores = ["node_modules/", ".next/", "dist/", "build/", ".env", ".env.local", "*.zip", "*.rar", "*.exe"]
    existing = ""
    if os.path.exists(gi):
        with open(gi, "r", encoding="utf-8", errors="ignore") as f:
            existing = f.read()
    to_add = [ig for ig in ignores if ig not in existing]
    if to_add:
        with open(gi, "a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(to_add) + "\n")

def push_project(p):
    path = p["path"]
    name = p["name"]
    desc = p["desc"]
    print(f"\n==========================================")
    print(f"Processing: {name} ({path})")
    
    if not os.path.exists(path):
        print(f"[SKIP] Path does not exist: {path}")
        return

    ensure_gitignore(path)

    # Check git init
    if not os.path.exists(os.path.join(path, ".git")):
        ok, out = run("git init", cwd=path)
        print("git init:", ok)

    run("git config user.name \"Erfan Mehdi Sadeghi\"", cwd=path)
    run("git config user.email \"erfandarrudi527@gmail.com\"", cwd=path)
    run("git branch -M main", cwd=path)

    run("git add -A", cwd=path)
    run("git commit -m \"feat: initial release of " + name + "\"", cwd=path)

    gh_exe = "C:/Program Files/GitHub CLI/gh.exe"
    gh_cmd = f'"{gh_exe}" repo create "{name}" --public --description "{desc}" --source=. --remote=origin --push'
    ok, out = run(gh_cmd, cwd=path)
    if "already exists" in out or not ok:
        print("Repo might already exist or remote needed. Trying git push directly...")
        run("git push -u origin main --force", cwd=path)
    print(out.strip())

if __name__ == "__main__":
    for p in PROJECTS:
        try:
            push_project(p)
        except Exception as e:
            print("Error on", p["name"], e)
