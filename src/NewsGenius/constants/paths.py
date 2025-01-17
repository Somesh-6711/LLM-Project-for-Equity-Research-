from pathlib import Path

# project-wide paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "config" / "config.yaml"
LOG_FILE = BASE_DIR / "logs" / "project.log"
