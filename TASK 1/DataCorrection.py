# VINEET SINGHAL 2025A7PS0089H

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter 
import math
from pathlib import Path

""" 1. Load the raw CSV flight data"""

BASE_DIR = Path(r"D:\Vineet_Singhal_2025A7PS0089H_JANUS\TASK 1\Raw_Test_Flight_Data_25 - Sheet1.csv").resolve().parent
input_path = BASE_DIR / "Raw_Test_Flight_Data_25 - Sheet1.csv"

# Reads the raw test flight dataset into a DataFrame
raw_df = pd.read_csv(input_path)

"""2. Clean and prepare the dataset"""

# Convert 'Pressure (Pa)' column values to numeric (remove invalid entries)
raw_df['Pressure (Pa)'] = pd.to_numeric(raw_df['Pressure (Pa)'], errors='coerce')

# Drop rows where conversion failed (NaN values)
raw_df.dropna(inplace=True)

# Reset index after dropping rows
raw_df.reset_index(inplace=True, drop=True)

"""3. Extract useful arrays"""

# Pressure data (Pa)
pressure = raw_df['Pressure (Pa)'].astype(float).to_numpy()

# Generate a time column (0,1,2,... seconds)
time_s = np.arange(len(raw_df))
raw_df['Time(s)'] = time_s

""" 4. Define constants for barometric formula"""

P0 = pressure[0]     # Pa   → reference pressure at ground level (first data point)
T0 = 288.15          # K    → standard sea-level temperature
R  = 8.31447         # J/(mol·K) → universal gas constant
g  = 9.80665         # m/s² → gravitational acceleration
M  = 0.0289644       # kg/mol → molar mass of Earth's air

# Precompute constant used in barometric formula
k = (R * T0) / (g * M)

""" 5. Compute altitude from pressure"""

# Barometric altitude formula: height = k * log(P0/p)
altitude_m = []
for p in pressure:
    altitude_m.append(k* math.log(p/P0)*-1)

"""6. Compute velocity from altitude"""

# Velocity = change in altitude per unit time
velocity = np.diff(altitude_m)

# Insert initial velocity = 0 at t=0 (since np.diff reduces array length by 1)
velocity = np.insert(velocity, 0, 0)

"""7. Apply smoothing filter"""

# Savitzky-Golay filter smooths out noise in altitude and velocity
smooth_altitude = savgol_filter(altitude_m, window_length=5, polyorder=2)
smooth_velocity = savgol_filter(velocity, window_length=5, polyorder=2)

"""8. Add results back to DataFrame"""

raw_df['Velocity(m/s)'] = smooth_velocity
raw_df['Altitude(m)']  = smooth_altitude

""" 9. Save corrected data to new CSV"""

# Creates a clean + smoothed dataset for further analysis/plotting
raw_df.to_csv(r'D:\Vineet_Singhal_2025A7PS0089H_JANUS\TASK 1\correct&smooth_data.csv', index=False)
