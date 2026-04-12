import plotly.graph_objects as go
import pandas as pd


def create_motion_plot(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive Plotly figure for motion metrics.
    :param df:
    :return fig:
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["magnitude"],
            mode="lines",
            name="Magnitude"
        )
    )

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