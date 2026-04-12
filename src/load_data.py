from pathlib import Path
import pandas as pd
from src.logger import logger


def load_motion_data(file_path: str | Path) -> pd.DataFrame:
    """
    Load wearable motion sensor data from a CSV file.

    Expected columns:
    - timestamp
    - x
    - y
    - z

    :param file_path:
    :return pd.Dataframe:
    """
    file_path = Path(file_path)
    print("path is", file_path, file_path.exists())
    if not file_path.exists():
        raise FileNotFoundError(f'File {file_path} does not exist')

    logger.info(f"Loading data from {file_path}")
    df = pd.read_csv(file_path)

    required_columns = {'timestamp', 'x', 'y', 'z'}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        logger.warning(f"Columns {missing_columns} are missing")
        raise ValueError(f'Columns {missing_columns} are missing')

    return df