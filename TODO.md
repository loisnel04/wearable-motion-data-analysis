# Project Roadmap / TODO

This document tracks potential improvements and future work for the **Wearable Motion Data Analysis** project.

The goal is to progressively evolve this repository from a simple demonstration pipeline into a more realistic motion-analysis tool.

---

# Pipeline Improvements

- [ ] Add additional motion features:
  - Signal variance
  - Signal entropy
  - Root Mean Square (RMS)
  - Frequency-domain features (FFT)

- [ ] Improve signal smoothing:
  - configurable smoothing filters
  - compare moving average vs low-pass filtering

- [ ] Make window sizes configurable through a config file or API parameters.

---

# Dataset Improvements

- [ ] Add a larger synthetic dataset generator simulating:
  - walking
  - resting
  - sudden movements
  - irregular motion patterns

- [ ] Include a real open wearable dataset for demonstration.

Examples:
- WISDM dataset
- UCI HAR dataset

---

# API Improvements

- [ ] Add endpoint:
  `POST /analyze/plot`
  to return plots for uploaded datasets.

- [ ] Allow optional parameters in API requests:
  - smoothing window
  - energy window
  - feature selection

- [ ] Add better input validation for uploaded CSV files.

---

# Visualization Improvements

- [ ] Improve Plotly charts:
  - add zoom presets
  - allow feature selection
  - export plots as images.

- [ ] Add combined dashboard-style visualization.

---

# Engineering Improvements

- [ ] Add unit tests for:
  - feature extraction
  - preprocessing
  - data validation

- [ ] Add continuous integration (GitHub Actions).

- [ ] Add code formatting tools:
  - black
  - ruff / flake8

---

# Potential Future Extensions

- [ ] Real-time streaming motion data analysis.

- [ ] Activity classification model using extracted features.

- [ ] Interactive dashboard interface.

- [ ] Integration with wearable device data formats.

- [ ] Front-end

- [ ] Download directly the plot without showing it. 
---

# Notes

This repository is intentionally lightweight and focused on demonstrating:

- clean data pipelines
- signal feature extraction
- visualization
- API exposure

Future improvements aim to make it closer to a real-world wearable motion analytics system.