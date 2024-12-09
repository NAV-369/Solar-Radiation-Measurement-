import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def analyze_and_visualize(csv_data):
    """
    Analyze and visualize the sensor data before and after cleaning events.

    Parameters:
    - csv_data: pandas DataFrame containing the following columns:
        'GHI', 'DHI', 'Tamb', 'ModA', 'ModB', 'Cleaning'
    """
    # Adjusting the subplot layout to 5 rows
    plt.figure(figsize=(14, 12))

    # Plot GHI
    plt.subplot(5, 1, 1)
    plt.plot(csv_data.index, csv_data['GHI'], label='GHI (Global Horizontal Irradiance)', color='orange')
    plt.title('Time Series of GHI')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)
    plt.legend(loc='best')

    # Plot DHI
    plt.subplot(5, 1, 2)
    plt.plot(csv_data.index, csv_data['DHI'], label='DHI (Diffuse Horizontal Irradiance)', color='blue')
    plt.title('Time Series of DHI')
    plt.ylabel('DHI (W/m²)')
    plt.grid(True)
    plt.legend(loc='best')

    # Plot Tamb
    plt.subplot(5, 1, 3)
    plt.plot(csv_data.index, csv_data['Tamb'], label='Ambient Temperature', color='green')
    plt.title('Time Series of Ambient Temperature')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.legend(loc='best')

    # Plot ModA with cleaning events
    plt.subplot(5, 1, 4)
    plt.plot(csv_data.index, csv_data['ModA'], label='ModA', color='blue')
    plt.scatter(csv_data.index[csv_data['Cleaning'] == 1], csv_data['ModA'][csv_data['Cleaning'] == 1], 
                color='red', label='Cleaning Event', s=10)
    plt.title('ModA Sensor Reading Over Time')
    plt.ylabel('ModA (W/m²)')
    plt.grid(True)
    plt.legend(loc='best')

    # Plot ModB with cleaning events
    plt.subplot(5, 1, 5)
    plt.plot(csv_data.index, csv_data['ModB'], label='ModB', color='green')
    plt.scatter(csv_data.index[csv_data['Cleaning'] == 1], csv_data['ModB'][csv_data['Cleaning'] == 1], 
                color='red', label='Cleaning Event', s=10)
    plt.title('ModB Sensor Reading Over Time')
    plt.ylabel('ModB (W/m²)')
    plt.grid(True)
    plt.legend(loc='best')

    plt.tight_layout()
    plt.show()

    # Statistical comparison before and after cleaning
    before_cleaning = csv_data[csv_data['Cleaning'] == 0]
    after_cleaning = csv_data[csv_data['Cleaning'] == 1]

    # Calculate means
    mean_before = before_cleaning[['ModA', 'ModB']].mean()
    mean_after = after_cleaning[['ModA', 'ModB']].mean()

    print("Mean sensor readings before cleaning:")
    print(mean_before)

    print("\nMean sensor readings after cleaning:")
    print(mean_after)

    # Perform t-tests
    t_stat_modA, p_val_modA = ttest_ind(before_cleaning['ModA'], after_cleaning['ModA'], nan_policy='omit')
    t_stat_modB, p_val_modB = ttest_ind(before_cleaning['ModB'], after_cleaning['ModB'], nan_policy='omit')

    print(f"\nT-test for ModA: t-statistic = {t_stat_modA:.2f}, p-value = {p_val_modA:.4f}")
    print(f"T-test for ModB: t-statistic = {t_stat_modB:.2f}, p-value = {p_val_modB:.4f}")