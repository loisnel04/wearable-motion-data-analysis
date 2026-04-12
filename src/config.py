from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "sample_motion_data.csv"

SMOOTHING_WINDOW = 3
ENERGY_WINDOW = 100