from io import StringIO

import pandas as pd
from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

from src.load_data import load_motion_data
from src.preprocess import preprocess_motion_data
from src.features import compute_motion_features
from src.visualize import (create_dynamics_plot,
                           create_activity_plot,
                           create_raw_plot,
                           create_jerk_plot
)

DATA_PATH = "data/sample_motion_data.csv"

app = FastAPI(title="Wearable Motion Data Analysis API")


def build_pipeline():
    df = load_motion_data(DATA_PATH)
    df = preprocess_motion_data(df)
    df = compute_motion_features(df)
    return df


def build_pipeline_from_dataframe(df: pd.DataFrame) -> pd.DataFrame:
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
        "max_jerk": float(df["jerk"].max()),
        "mean_signal_power": float(df["signal_power"].mean()),
        "max_signal_energy": float(df["signal_energy"].max()),
    }

    return summary


@app.post("/analyze")
async def analyze_uploaded_csv(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only CSV files are supported.")

        content = await file.read()
        decoded_content = content.decode("utf-8")
        df = pd.read_csv(StringIO(decoded_content))

        required_columns = {"timestamp", "x", "y", "z"}
        missing_columns = required_columns - set(df.columns)

        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required columns: {sorted(missing_columns)}"
            )

        df = build_pipeline_from_dataframe(df)

        return {
            "filename": file.filename,
            "num_samples": int(len(df)),
            "mean_magnitude": float(df["magnitude"].mean()),
            "max_velocity": float(df["velocity"].max()),
            "max_acceleration": float(df["acceleration"].max()),
            "max_jerk": float(df["jerk"].max()),
            "mean_signal_power": float(df["signal_power"].mean()),
            "max_signal_energy": float(df["signal_energy"].max()),
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to analyze uploaded file: {e}")

@app.get("/data")
def get_data():
    df = build_pipeline()
    return df.to_dict(orient="records")


@app.get("/plot")
def get_plot():

    try:
        df = build_pipeline()

        fig_raw = create_raw_plot(df)
        fig_dynamics = create_dynamics_plot(df)
        fig_jerk = create_jerk_plot(df)
        fig_activity = create_activity_plot(df)

        fig_raw.write_html("docs/raw_plot.html")
        fig_raw.show()

        fig_dynamics.write_html("docs/dynamics_plot.html")
        fig_dynamics.show()

        fig_jerk.write_html("docs/jerk_plot.html")
        fig_jerk.show()

        fig_activity.write_html("docs/activity_plot.html")
        fig_activity.show()

        return {
            "raw_signals": fig_raw.to_dict(),
            "motion_dynamics": fig_dynamics.to_dict(),
            "jerk": fig_jerk.to_dict(),
            "intensity": fig_activity.to_dict(),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))