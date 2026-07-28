import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files = [
    "scraper.py",
    "cleaner.py",
    "database.py",
    "queries.py"
]

for file in files:

    print("=" * 60)
    print(f"Running {file}")
    print("=" * 60)

    subprocess.run(
        [sys.executable, os.path.join(BASE_DIR, file)],
        check=True
    )

print("\n")
print("=" * 60)
print("DATA PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)