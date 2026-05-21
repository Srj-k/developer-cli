from pathlib import Path
import os

ENV = os.getenv("DEVCLI_ENV", "development")

BASE_DIR = (Path("./devcli") if ENV == "development" else Path.home() / ".devcli")

TASK_FILE = BASE_DIR / "tasks.json"
CONFIG_FILE = BASE_DIR / "config.json"
SHORTCUT_FILE = BASE_DIR / "shortcuts.json"