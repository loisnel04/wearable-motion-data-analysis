import numpy as np
import pandas as pd


def compute_motion_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute movement-derived features from x, y, z motion signals.

    Features:
    - magnitude
    - delta_t
    - velocity
    - acceleration
    - smoothed_magnitude

    :param df:
    :return df:
    """

    features_df = df.copy()

    features_df["magnitude"] = np.sqrt(
        features_df["x"] ** 2 +
        features_df["y"] ** 2 +
        features_df["z"] ** 2
    )

    features_df["delta_t"] = features_df["timestamp"].diff()

    features_df["velocity"] = (
        features_df["magnitude"].diff() / features_df["delta_t"]
    )

    features_df["acceleration"] = (
        features_df["velocity"].diff() / features_df["delta_t"]
    )

    features_df["smoothed_magnitude"] = (
        features_df["magnitude"].rolling(window=3, min_periods=1).mean()
    )

    features_df = features_df.replace([np.inf, -np.inf], np.nan)
    features_df = features_df.fillna(0)

    return features_df