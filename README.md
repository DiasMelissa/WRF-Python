# WRF-Python
Educational and practical examples on using WRF-Python for WRF post-processing and meteorological analysis.
# 🌦️ WRF-Python: Analysis and Visualization with the WRF Model

This repository gathers examples and tutorials on how to use the **WRF-Python** library to manipulate, analyze, and visualize outputs from the **WRF (Weather Research and Forecasting Model)**.  
The goal is to provide supporting material for meteorologists, researchers, and students who wish to explore WRF-generated data in a practical and automated way using Python.

---

## 📚 About WRF-Python

**WRF-Python** is a library developed by **NCAR (National Center for Atmospheric Research)** that allows simplified access to variables and coordinates from WRF output files.  
With it, you can compute derived meteorological variables (such as potential temperature, wind components, CAPE/CIN, etc.) and create customized visualizations using **Matplotlib**, **Cartopy**, and **xarray**.

🔗 [Official WRF-Python Documentation](https://wrf-python.readthedocs.io/en/latest/)

---

## ⚙️ Requirements

Before getting started, make sure you have a Python 3.9+ environment configured with the required libraries:

```bash
conda create -n wrf_python
conda activate wrf_python
conda install -c conda-forge wrf-python xarray netCDF4 cartopy matplotlib numpy
bash```

## 📖 References

Visualization & Analysis Systems Technologies. (2025). Geoscience Community Analysis Toolkit: WRF-Python (v1.4.0) [Software]. Boulder, CO, USA: UCAR/NCAR - Computational and Informational System Lab. doi:10.5281/zenodo.6685115.
