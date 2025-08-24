<h1 align="center">🚀 Task 1 – Planning to Surprise <span style="color:#9b59b6;">Galactus</span></h1>

---

## 📂 Files
- 🗂️ **`Raw_Test_Flight_Data_25 - Sheet1.csv`** → <span style="color:#3498db;">Raw pressure data</span>  
- 🐍 **`DataCorrection.py`** → Processes pressure → altitude & velocity, applies smoothing, exports cleaned CSV  
   *(uses **numpy** & **pandas**)*  
- 📊 **`graphs.py`** → Animated **Altitude/Velocity vs Time** graph with toggle  

---

## ✨ Features
- 🎛️ Noise reduction → **Savitzky-Golay filter** (`savgol_filter`) from **scipy**  
- 📈 Interactive animation → **moving point marker** + **radio button toggle**  

---

## 🔎 Approach
1. **Data Processing**  
   - Clean raw pressure → altitude using barometric formula  
     > *h = (RT/Mg) × ln(P₀ / P)*  
   - Velocity from `numpy.diff()`  
   - Smooth with `savgol_filter`  
   - Save as cleaned CSV  

2. **Visualization**  
   - Animated graphs with **matplotlib** (`pyplot`, `FuncAnimation`)  
   - Toggle between altitude/velocity using **RadioButtons**  

---

## ⚙️ Requirements

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)  
![NumPy](https://img.shields.io/badge/numpy-lightgrey?logo=numpy)  
![Pandas](https://img.shields.io/badge/pandas-black?logo=pandas)  
![SciPy](https://img.shields.io/badge/scipy-orange?logo=scipy)  
![Matplotlib](https://img.shields.io/badge/matplotlib-blueviolet?logo=plotly)  

Install with:  
```bash
pip install numpy pandas scipy matplotlib

▶️ Run Order:
DataCorrection.py
graphs.py

<h1 align="center">⚡ Task 2 – Surprising <span style="color:#e74c3c;">Galactus</span></h1>
🔌 Circuit (Tinkercad)
⚡ Force Sensor (FSR) → Detects force/pressure
🔴🟡🟢 3 LEDs → Red = Ascending | Yellow = Apogee | Green = Descending
🔔 Buzzer → Sounds briefly at Apogee
(when person is ascending & force stabilizes)

🧠 Logic
📉 Moving Average filter (5 samples) → reduces noise
🛰️ State detection: Ascending / Apogee / Descending
Uses threshold = 3 units (10 N = 914 units)
🔔 Buzzer → triggers once at Apogee
💡 Only one LED active at a time
🖥️ Serial Monitor → prints pressure from force readings

📷 Screenshots of circuit & code are attached

📌 Submitted by: Vineet Singhal
🆔 ID: 2025A7PS0089H
📡 Avionics
