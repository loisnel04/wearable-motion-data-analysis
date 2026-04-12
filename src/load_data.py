from pathlib import Path
import pandas as pd


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

    if not file_path.exists():
        raise FileNotFoundError(f'File {file_path} does not exist')

    df = pd.read_csv(file_path)

    required_columns = {'timestamp', 'x', 'y', 'z'}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f'Columns {missing_columns} are missing')

    return df