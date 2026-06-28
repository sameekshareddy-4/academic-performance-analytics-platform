from pathlib import Path

# Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = BASE_DIR / "data"

RAW_DATA = DATA_DIR / "raw"
PROCESSED_DATA = DATA_DIR / "processed"
FINAL_DATA = DATA_DIR / "final"

# Create folders automatically
for folder in [RAW_DATA, PROCESSED_DATA, FINAL_DATA]:
    folder.mkdir(parents=True, exist_ok=True)