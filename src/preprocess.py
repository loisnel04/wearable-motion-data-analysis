import pandas as pd


def preprocess_motion_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic preprocessing for motion data:
    - remove rows with missing values
    - sort by timestamp
    - reset index

    :param df:
    :return df:
    """

    cleaned_df = df.dropna().copy()
    cleaned_df = cleaned_df.sort_values("timestamp").reset_index(drop=True)

    return cleaned_df