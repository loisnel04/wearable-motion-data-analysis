from src.load_data import load_motion_data
from src.preprocess import preprocess_motion_data
from src.features import compute_motion_features

from src.config import DATA_PATH


def main():
    df = load_motion_data(DATA_PATH)
    df = preprocess_motion_data(df)
    df = compute_motion_features(df)

    print(df.head())


if __name__ == "__main__":
    main()