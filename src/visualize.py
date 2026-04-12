import plotly.graph_objects as go
import pandas as pd
from src.logger import logger


def create_dynamics_plot(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive Plotly figure for dynamics motion metrics.
    Metrics:
    - velocity
    - acceleration
    :param df:
    :return fig:
    """
    logger.info(f"Create dynamic plot")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["velocity"],
            mode="lines",
            name="Velocity"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["acceleration"],
            mode="lines",
            name="Acceleration"
        )
    )

    fig.update_layout(
        title="Wearable Motion Metrics Over Time",
        xaxis_title="Time (s)",
        yaxis_title="Metric value",
        template="plotly_white"
    )

    return fig


def create_activity_plot(df: pd.DataFrame) -> go.Figure:
    """
        Create an interactive Plotly figure for activity metrics.
        Metrics :
        - signal power
        - signal energy
        :param df:
        :return fig:
    """
    logger.info(f"Create activity plot")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["signal_power"],
            mode="lines",
            name="Signal Power"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["signal_energy"],
            mode="lines",
            name="Signal Energy"
        )
    )

    fig.update_layout(
        title="Wearable Motion Metrics Over Time",
        xaxis_title="Time (s)",
        yaxis_title="Metric value",
        template="plotly_white"
    )

    return fig


def create_raw_plot(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive Plotly figure for raw metrics.
    Metrics:
    - smoothed magnitude as magnitude
    - x
    - y
    - z
    :param df:
    :return fig:
    """
    logger.info(f"Create raw plot")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["smoothed_magnitude"],
            mode="lines",
            name="Magnitude"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["x"],
            mode="lines",
            name="x"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["y"],
            mode="lines",
            name="y"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["z"],
            mode="lines",
            name="z"
        )
    )

    fig.update_layout(
        title="Wearable Motion Metrics Over Time",
        xaxis_title="Time (s)",
        yaxis_title="Metric value",
        template="plotly_white"
    )

    return fig


def create_jerk_plot(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive Plotly figure for jerk metric.
    Metrics:
    - jerk
    :param df:
    :return fig:
    """
    logger.info(f"Create jerk plot")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["jerk"],
            mode="lines",
            name="Jerk"
        )
    )

    fig.update_layout(
        title="Wearable Motion Metrics Over Time",
        xaxis_title="Time (s)",
        yaxis_title="Metric value",
        template="plotly_white",
        showlegend=True
    )

    return fig