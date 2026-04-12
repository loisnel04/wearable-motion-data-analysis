import numpy as np
import pandas as pd
from src.config import SMOOTHING_WINDOW, ENERGY_WINDOW
from src.logger import logger


def compute_motion_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute movement-derived features from x, y, z motion signals.

    Features:
    - magnitude
    - delta_t
    - velocity
    - acceleration
    - jerk
    - smoothed_magnitude

    :param df:
    :return df:
    """

    logger.info(f"Compute motion features")

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

    features_df["jerk"] = (
        features_df["acceleration"].diff() / features_df["delta_t"]
    )

    features_df["smoothed_magnitude"] = (
        features_df["magnitude"].rolling(window=SMOOTHING_WINDOW, min_periods=1).mean()
    )

    features_df["signal_power"] =  features_df["smoothed_magnitude"] ** 2

    features_df["signal_energy"] = (
        features_df["signal_power"].rolling(window=ENERGY_WINDOW, min_periods=1).sum()
    )

    features_df = features_df.replace([np.inf, -np.inf], np.nan)
    features_df = features_df.fillna(0)

    return features_df