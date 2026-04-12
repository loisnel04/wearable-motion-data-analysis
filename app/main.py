from fastapi import FastAPI
from src.load_data import load_motion_data
from src.preprocess import preprocess_motion_data
from src.features import compute_motion_features
from src.visualize import create_motion_plot

DATA_PATH = "data/sample_motion_data.csv"

app = FastAPI(title="Wearable Motion Data Analysis API")


def build_pipeline():
    df = load_motion_data(DATA_PATH)
    df = preprocess_motion_data(df)
    df = compute_motion_features(df)
    return df


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def get_metrics():
    df = build_pipeline()

    summary = {
        "num_samples": int(len(df)),
        "mean_magnitude": float(df["magnitude"].mean()),
        "max_velocity": float(df["velocity"].max()),
        "max_acceleration": float(df["acceleration"].max()),
    }

    return summary


@app.get("/data")
def get_data():
    df = build_pipeline()
    return df.to_dict(orient="records")


@app.get("/plot")
def get_plot():
    df = build_pipeline()
    fig = create_motion_plot(df)

    fig.write_html("docs/motion_plot.html")
    fig.show()
    return fig.to_dict()