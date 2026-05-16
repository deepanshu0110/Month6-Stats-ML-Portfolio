import os, re, subprocess, time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "C:/Users/Deepanshu/OneDrive/Desktop/Month6"
REPO_URL = "https://github.com/deepanshu0110/Month6-Stats-ML-Portfolio.git"
BRANCH = "main"
TRACKED_EXTS = {".ipynb", ".py", ".xlsx", ".csv", ".png", ".pdf"}
IGNORE_PATTERNS = {"auto_sync", "__pycache__", ".git", ".ipynb_checkpoints"}
BATCH_DELAY = 3.0

def run(cmd):
    r = subprocess.run(cmd, shell=True, cwd=WATCH_FOLDER, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()

def git_push(reason=""):
    readme = "# Month 6 Stats + ML Portfolio\n**deepanshu0110**\n\nDays 101-131 | scipy.stats | scikit-learn | Python\n"
    with open(os.path.join(WATCH_FOLDER, "README.md"), "w") as f:
        f.write(readme)
    run("git add -A")
    rc, out = run("git status --short")
    if not out.strip():
        print("  [skip] Nothing to commit")
        return
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    run(f'git commit -m "sync: {reason} [{ts}]"')
    rc2, out2 = run(f"git push origin {BRANCH}")
    print("  Pushed OK" if rc2 == 0 else f"  Push failed: {out2}")

class SyncHandler(FileSystemEventHandler):
    def __init__(self):
        self.pending = {}
    def on_created(self, e):
        self._q(e)
    def on_modified(self, e):
        self._q(e)
    def _q(self, e):
        if e.is_directory: return
        fn = os.path.basename(e.src_path)
        if os.path.splitext(fn)[1].lower() not in TRACKED_EXTS: return
        if any(p in fn for p in IGNORE_PATTERNS): return
        print(f"  Detected: {fn}")
        self.pending[fn] = time.time()
    def flush(self):
        now = time.time()
        ready = [f for f, t in self.pending.items() if now - t >= BATCH_DELAY]
        if not ready: return
        for f in ready: del self.pending[f]
        git_push(", ".join(ready))

os.chdir(WATCH_FOLDER)
rc, _ = run("git rev-parse --is-inside-work-tree")
if rc != 0:
    run("git init")
    run(f"git remote add origin {REPO_URL}")
    run(f"git branch -M {BRANCH}")

print("Month 6 Auto Sync running. Ctrl+C to stop.")
git_push("startup")
h = SyncHandler()
obs = Observer()
obs.schedule(h, WATCH_FOLDER, recursive=False)
obs.start()
try:
    while True:
        h.flush()
        time.sleep(0.5)
except KeyboardInterrupt:
    obs.stop()
    print("Stopped.")
obs.join()
