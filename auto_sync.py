# Month 6 Auto Sync - deepanshu0110
# Watches: C:/Users/Deepanshu/OneDrive/Desktop/Month6
# Repo   : Month6-Stats-ML-Portfolio
# Tracks : .ipynb  .py  .xlsx  .csv  .png  .pdf
# Ignores: auto_sync.py  __pycache__  .git  .ipynb_checkpoints
# Usage  : python auto_sync.py
# Stop   : Ctrl+C

import os
import re
import subprocess
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ── CONFIG — edit only this block ────────────────────────────────────────────
WATCH_FOLDER  = "C:/Users/Deepanshu/OneDrive/Desktop/Month6"
REPO_URL      = "https://github.com/deepanshu0110/Month6-Stats-ML-Portfolio.git"
BRANCH        = "main"
TRACKED_EXTS  = {".ipynb", ".py", ".xlsx", ".csv", ".png", ".pdf"}
IGNORE_PATTERNS = {"auto_sync", "__pycache__", ".git",
                   ".ipynb_checkpoints", ".DS_Store", "Thumbs.db"}
BATCH_DELAY   = 3.0   # seconds to wait before committing after last change
# ─────────────────────────────────────────────────────────────────────────────

# ── Scorecard — filled from known Month 5 data, Month 6 slots pending ────────
SCORECARD = {
    # Month 5 (closed) — carried for context
    "Day86":  ("RLS + Bookmarks",                    "90/80 ✅"),
    "Day87":  ("Advanced DAX",                        "90/80 ✅"),
    "Day88":  ("Tableau LOD + Sets + Params",         "90/80 ✅"),
    "Day89":  ("Week 1 Mini-Project",                 "110/100 ✅"),
    "Day90":  ("SQL → Python Pipeline",               "110/100 ✅"),
    "Day91":  ("Python → BI Integration",             "90/80 ✅"),
    "Day92":  ("End-to-End Pipeline",                 "79/80 ✅"),
    "Day93":  ("Streamlit Dashboard",                 "80/80 ✅"),
    "Day94":  ("Upwork Activation",                   "77/80 ✅"),
    "Day100": ("Month 5 Capstone — UrbanNest India",  "120/120 ✅"),
    # Month 6 — filled automatically as files arrive
    "Day101": ("Descriptive Stats + Distributions",   "— 🔵"),
    "Day102": ("T-Tests + Confidence Intervals",      "— 🔵"),
    "Day103": ("Chi-Square + ANOVA",                  "— 🔵"),
    "Day104": ("A/B Testing with scipy",              "— 🔵"),
    "Day105": ("Week 1 Mini-Project",                 "— 🔵"),
    "Day106": ("Hypothesis Testing Deep Dive",        "— 🔵"),
    "Day107": ("Effect Size + Power",                 "— 🔵"),
    "Day108": ("Week 2 Mini-Project",                 "— 🔵"),
    "Day109": ("Linear Regression Foundations",       "— 🔵"),
    "Day110": ("Train-Test Split + R² + RMSE",        "— 🔵"),
    "Day111": ("Feature Selection",                   "— 🔵"),
    "Day112": ("Overfitting + Regularisation",        "— 🔵"),
    "Day113": ("Week 3 Mini-Project",                 "— 🔵"),
    "Day114": ("Logistic Regression",                 "— 🔵"),
    "Day115": ("Decision Tree",                       "— 🔵"),
    "Day116": ("Random Forest",                       "— 🔵"),
    "Day117": ("Model Comparison",                    "— 🔵"),
    "Day118": ("Week 4 Mini-Project",                 "— 🔵"),
    "Day119": ("Confusion Matrix + Precision/Recall", "— 🔵"),
    "Day120": ("ROC-AUC",                             "— 🔵"),
    "Day121": ("Cross-Validation",                    "— 🔵"),
    "Day122": ("GridSearchCV",                        "— 🔵"),
    "Day123": ("Scikit-learn Pipeline",               "— 🔵"),
    "Day124": ("Week 5 Mini-Project",                 "— 🔵"),
    "Day125": ("E-commerce KPIs — CAC + LTV + Churn","— 🔵"),
    "Day126": ("Model Explainability Intro",          "— 🔵"),
    "Day127": ("SHAP Values",                         "— 🔵"),
    "Day128": ("Domain Niche Deep Dive",              "— 🔵"),
    "Day129": ("Week 6 Mini-Project",                 "— 🔵"),
    "Day130": ("Portfolio Polish",                    "— 🔵"),
    "Day131": ("Month 6 Capstone — Full ML Pipeline", "— 🔵"),
}

MONTH6_TOOLS = "Python · NumPy · Pandas · scipy.stats · scikit-learn · Matplotlib · Seaborn · Streamlit"


def run(cmd, cwd=None):
    """Run a shell command, return (returncode, stdout+stderr)."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd or WATCH_FOLDER,
        capture_output=True, text=True
    )
    return result.returncode, (result.stdout + result.stderr).strip()


def extract_day(filename):
    """Extract 'Day101' from filenames like Day101_Statistics.ipynb"""
    m = re.search(r'[Dd]ay(\d+)', filename)
    if m:
        return f"Day{m.group(1)}"
    return None


def build_readme(last_file="", last_day=""):
    """Generate the README.md content."""
    now = datetime.now().strftime("%d %b %Y %H:%M")

    # Build scorecard rows — Month 6 only
    m6_rows = ""
    for key in sorted(SCORECARD.keys(), key=lambda x: int(x.replace("Day",""))):
        day_num = int(key.replace("Day", ""))
        if day_num < 101:
            continue
        topic, score = SCORECARD[key]
        status = score
        m6_rows += f"| {key} | {topic} | {status} |\n"

    # Count completed
    completed = sum(
        1 for k, (_, s) in SCORECARD.items()
        if int(k.replace("Day","")) >= 101 and "✅" in s
    )
    in_progress = sum(
        1 for k, (_, s) in SCORECARD.items()
        if int(k.replace("Day","")) >= 101 and "🔵" in s
    )

    last_line = ""
    if last_file and last_day:
        topic = SCORECARD.get(last_day, ("", ""))[0]
        last_line = f"\n> **Last push:** `{last_file}` ({last_day} — {topic}) at {now}\n"

    readme = f"""# Month 6 — Statistics + Machine Learning Portfolio
**Deepanshu Garg | [@deepanshu0110](https://github.com/deepanshu0110)**

> 31-day structured programme: descriptive statistics, probability distributions,
> hypothesis testing, A/B testing, linear + logistic regression, tree-based models,
> scikit-learn pipelines, model evaluation, and domain niche (e-commerce analytics).
{last_line}
---

## Progress

| Metric | Value |
|--------|-------|
| Days Completed | {completed} / 31 |
| Days In Progress | {in_progress} |
| Month 5 Capstone | 120/120 ✅ (UrbanNest India — best score in programme) |
| Upwork Status | Active — bids submitted Month 5 W4 |
| IELTS Target | Jun–Aug 2026, score 6.5+ |
| Netherlands MSc | TU/e DSAI (first choice), Sep 2027 intake |

---

## Month 6 Scorecard

| Day | Topic | Score |
|-----|-------|-------|
{m6_rows}
---

## Tools & Stack

{MONTH6_TOOLS}

---

## Repo Structure

```
Month6/
├── Day101_Statistics_Foundations.ipynb
├── Day102_T_Tests_Confidence_Intervals.ipynb
├── ...
├── Day131_Month6_Capstone.ipynb
└── auto_sync.py
```

---

## Previous Months

| Month | Repo | Top Score |
|-------|------|-----------|
| Month 1 — Excel | [excel-data-analytics](https://github.com/deepanshu0110/excel-data-analytics) | 88/80 |
| Month 2 — SQL | [Month2-SQL-Portfolio](https://github.com/deepanshu0110/Month2-SQL-Portfolio) | 119/120 |
| Month 3 — Python/Pandas | [Month3-Python-Portfolio](https://github.com/deepanshu0110/Month3-Python-Portfolio) | 100/100 |
| Month 4 — Power BI + Tableau | [Month4-PowerBI-Tableau-Portfolio](https://github.com/deepanshu0110/Month4-PowerBI-Tableau-Portfolio) | 110/100 |
| Month 5 — BI + Upwork | [Month5-BI-Upwork-Portfolio](https://github.com/deepanshu0110/Month5-BI-Upwork-Portfolio) | 120/120 |

---

*Auto-synced via watchdog · Last updated: {now}*
"""
    return readme


def update_score(day_key, score_str):
    """
    Update SCORECARD in memory from filename hints.
    e.g. 'Day101_Statistics_Foundations.ipynb' → mark as pushed.
    """
    if day_key in SCORECARD:
        topic = SCORECARD[day_key][0]
        # Keep existing score if already has one; otherwise mark as synced
        current_score = SCORECARD[day_key][1]
        if "🔵" in current_score:
            SCORECARD[day_key] = (topic, "📤 Pushed")
    return SCORECARD.get(day_key, ("", ""))[0]


def git_push(reason=""):
    """Stage everything, commit, push. Returns True on success."""
    # Write README
    readme_path = os.path.join(WATCH_FOLDER, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(build_readme())

    rc, out = run("git add -A")
    rc2, out2 = run('git status --short')
    if not out2.strip():
        print(f"  [skip] No changes to commit ({reason})")
        return False

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = f"sync: {reason} [{timestamp}]"
    rc3, out3 = run(f'git commit -m "{msg}"')
    if rc3 != 0 and "nothing to commit" in out3.lower():
        print(f"  [skip] Nothing to commit")
        return False

    rc4, out4 = run(f"git push origin {BRANCH}")
    if rc4 == 0:
        print(f"  ✅ Pushed — {reason}")
        return True
    else:
        print(f"  ❌ Push failed:\n{out4}")
        return False


def should_ignore(filename):
    fname_lower = filename.lower()
    for pat in IGNORE_PATTERNS:
        if pat.lower() in fname_lower:
            return True
    return False


class SyncHandler(FileSystemEventHandler):
    def __init__(self):
        self.pending = {}   # filename → timestamp of last change

    def on_created(self, event):
        self._handle(event)

    def on_modified(self, event):
        self._handle(event)

    def _handle(self, event):
        if event.is_directory:
            return
        fname = os.path.basename(event.src_path)
        ext   = os.path.splitext(fname)[1].lower()
        if ext not in TRACKED_EXTS:
            return
        if should_ignore(fname):
            return
        print(f"  📄 Detected: {fname}")
        self.pending[fname] = time.time()

    def flush_pending(self):
        now = time.time()
        to_commit = [f for f, t in self.pending.items()
                     if now - t >= BATCH_DELAY]
        if not to_commit:
            return
        for fname in to_commit:
            day_key = extract_day(fname)
            if day_key:
                update_score(day_key, "")
            del self.pending[fname]

        files_str = ", ".join(to_commit)
        # Build commit label from day numbers found
        days = [extract_day(f) for f in to_commit if extract_day(f)]
        if days:
            day_label = "+".join(sorted(set(days)))
            topics    = " + ".join(
                SCORECARD.get(d, (f, ""))[0] for d in sorted(set(days))
            )
            reason = f"{day_label} — {topics}"
        else:
            reason = files_str

        git_push(reason)


def git_initial_setup():
    """Check git is initialised, remote is set, branch is main."""
    rc, out = run("git rev-parse --is-inside-work-tree")
    if rc != 0:
        print("  Initialising git repo...")
        run("git init")
        run(f"git remote add origin {REPO_URL}")
        run(f"git branch -M {BRANCH}")

    rc2, out2 = run("git remote get-url origin")
    if REPO_URL not in out2:
        run(f"git remote set-url origin {REPO_URL}")

    # Write .gitignore
    gi_path = os.path.join(WATCH_FOLDER, ".gitignore")
    if not os.path.exists(gi_path):
        with open(gi_path, "w") as f:
            f.write("__pycache__/\n.ipynb_checkpoints/\n*.pyc\n.DS_Store\nThumbs.db\n")
        run("git add .gitignore")


def main():
    print("\n" + "="*55)
    print("  Month 6 Auto Sync — deepanshu0110")
    print("  Watching:", WATCH_FOLDER)
    print("  Repo    :", REPO_URL)
    print("="*55)

    if not os.path.isdir(WATCH_FOLDER):
        print(f"\n  ❌ Folder not found: {WATCH_FOLDER}")
        print("  Create it first, then run again.")
        return

    os.chdir(WATCH_FOLDER)
    git_initial_setup()

    print("\n  Writing initial README + pushing startup commit...")
    git_push("startup — Month 6 initialised")

    handler = SyncHandler()
    observer = Observer()
    observer.schedule(handler, WATCH_FOLDER, recursive=False)
    observer.start()

    print("\n  ✅ Watching for .ipynb .py .xlsx .csv .png .pdf")
    print("  Save any file into Month6 folder → auto commit + push")
    print("  Stop: Ctrl+C\n")

    try:
        while True:
            handler.flush_pending()
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
        print("\n\n  Auto Sync stopped. All changes pushed. Goodbye.\n")
    observer.join()


if __name__ == "__main__":
    main()
