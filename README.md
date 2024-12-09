# Solar Radiation Measurement Data Analysis

## Overview

This project focuses on analyzing solar radiation measurement data, combined with various environmental parameters, to gain insights into solar energy patterns and applications. The primary goal is to identify trends, correlations, and anomalies in solar radiation and other related data. Key areas of focus include:

- **Exploratory Data Analysis (EDA)**: Understanding the distribution, relationships, and outliers in the data.
- **Statistical Analysis**: Identifying trends and significant relationships in the data.
- **Visualization**: Creating informative plots and charts to communicate the findings.

## Purpose

This analysis aims to identify high-potential regions for solar energy installation by exploring the solar radiation data and other relevant parameters. The goal is to translate these insights into actionable recommendations that can support strategic decision-making for future solar installations.

## Prerequisites

Before running the analysis, ensure you have the following installed on your system:

- **Python 3.x**: Ensure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Virtual Environment** (recommended for managing project dependencies):
  - Create a virtual environment using the following command:
    ```bash
    python -m venv venv
    ```
  - Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

## Installation

1. **Clone the repository**:
   
2. **Install the required dependencies:
   
	•	First, make sure your virtual environment is activated.
	•	Install the necessary packages using the command:
   ```bash
   pip install -r requirements.txt
   ```
  •	This command will install the required libraries as specified in the requirements.txt file. The libraries include:
	•	pandas: Data manipulation and analysis.
	•	numpy: Numerical operations and statistical analysis.
	•	matplotlib: Data visualization (plots, charts, graphs).
	•	seaborn: Statistical visualizations (heatmaps, correlation plots, etc.).
	•	scikit-learn: Machine learning algorithms (if applicable).
 
3. Add the dataset:
	•	The dataset used for this analysis is included in the repository under the data folder. If it’s missing, download it from the following source (insert the appropriate URL or location).
	•	Alternatively, you can add the dataset manually by placing the following CSV files in the data folder:
	•	benin_solar_measurements_cleaned.csv
	•	sierraleone-bumbuna_cleaned.csv
	•	togo-dapaong_qc_cleaned.csv

Dataset

The dataset contains the following key columns:
	•	Timestamp: Date and time of each observation.
	•	GHI (Global Horizontal Irradiance): Global Horizontal Irradiance in W/m².
	•	DNI (Direct Normal Irradiance): Direct Normal Irradiance in W/m².
	•	DHI (Diffuse Horizontal Irradiance): Diffuse Horizontal Irradiance in W/m².
	•	ModA/ModB: Measurements from sensors/modules A and B.
	•	Tamb (Ambient Temperature): Ambient temperature in °C.
	•	RH (Relative Humidity): Relative humidity in %.
	•	WS (Wind Speed): Wind speed in m/s.
	•	WSgust: Maximum wind gust speed in m/s.
	•	WSstdev: Standard deviation of wind speed.
	•	WD (Wind Direction): Wind direction in °N (measured to the east).
	•	WDstdev: Standard deviation of wind direction.
	•	BP (Barometric Pressure): Barometric pressure in hPa.
	•	Cleaning: Indicator for cleaning events.
	•	Precipitation: Precipitation rate in mm/min.
	•	TModA/TModB: Temperature of modules A/B in °C.
	•	Comments: Additional notes or observations.

The dataset will be processed for analysis, and you can explore the cleaned and transformed data in the provided Jupyter Notebooks.

Running the Analysis

1. Exploratory Data Analysis (EDA)
	•	Objective: Explore the data distribution, correlations, and outliers.
	•	Process:
	•	Load the data and perform initial checks (e.g., missing values).
	•	Visualize the data distribution with histograms and box plots.
	•	Identify correlations between key variables using a heatmap or scatter plots.
	•	Handle any outliers or data cleaning tasks.

2. Statistical Analysis
	•	Objective: Calculate summary statistics and identify any trends or significant relationships.
	•	Process:
	•	Calculate mean, median, and standard deviation for relevant columns.
	•	Perform hypothesis testing, such as correlation analysis to identify relationships.
	•	Investigate seasonal trends or cyclical patterns.

3. Visualization
	•	Objective: Create informative plots to convey key findings.
	•	Process:
	•	Visualize solar radiation patterns over time using time series plots.
	•	Create scatter plots to understand relationships between environmental parameters and solar radiation.
	•	Use heatmaps for correlation analysis between different variables.

Files Included

1. Notebooks:
	•	benin_data_analysis.ipynb: Jupyter Notebook containing the analysis for Benin.
	•	sierraleone_data_analysis.ipynb: Jupyter Notebook containing the analysis for Sierra Leone.
	•	togo_data_analysis.ipynb: Jupyter Notebook containing the analysis for Togo.

2. Data:
	•	benin_solar_measurements_cleaned.csv: Cleaned dataset for Benin.
	•	sierraleone-bumbuna_cleaned.csv: Cleaned dataset for Sierra Leone.
	•	togo-dapaong_qc_cleaned.csv: Cleaned dataset for Togo.

3. Scripts:
	•	analysis_module.py: Python script for conducting the analysis (optional, if you’re working outside Jupyter Notebooks).

Contributing

Contributions to this project are welcome! If you have suggestions for improving the analysis or the code, please feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
   

   
