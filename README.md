# Task 1 – Planning to Surprise Galactus

### **Files**

- **`Raw_Test_Flight_Data_25 - Sheet1.csv`** → Given raw pressure data  
- **`DataCorrection.py`** → Processes pressure → altitude & velocity, applies smoothing, exports cleaned CSV using **`numpy`** & **`pandas`** libraries
- **`graphs.py`** → Plots animated Altitude/Velocity vs Time graph with toggle  

### **Features**

- Noise reduction with **Savitzky-Golay filter** (savgol_filter) from **`scipy`** library
- Interactive animation with **moving point marker + radio button toggle**  

### **Approach**

1. **Data Processing** – Clean raw pressure → altitude using barometric formula ***(h = (RT/Mg) x ln(P0/P))*** → velocity using ***numpy.diff()***, smooth with ***savgol_filter***, save CSV  
2. **Visualization** – Animated graphs using **`matplotlib`** (***pyplot, FuncAnimation***); toggle between altitude/velocity using ***RadioButtons***

### **Requirements**
      Python 3.9+
      ***Packages*** :-
         numpy
         pandas
         scipy
         matplotlib   
      (pip install (package name))
      
#### First run DataCorrection.py & then run graphs.py     

---

# Task 2 – Surprising Galactus

### **Circuit (Tinkercad)**  

- **Force Sensor (FSR)** – Detects force/pressure  
- **3 LEDs** – Red (Ascending), Yellow (Apogee), Green (Descending)  
- **Buzzer** – Sounds briefly at ***Apogee*** *(person should be ascending & force must stabilize(no significant change))*

### **Logic**

- Moving Average filter (5 samples) to reduce noise  
- State detection: Ascending / Apogee / Descending *(using a threshold of 3 units) (10 N = 914 units)*
- Buzzer at apogee (once at a moment), LEDs indicate state, only 1 LED active at a time
- Prints pressure calculated from the force reading on Serial Monitor in Tinkercad

> Screenshots of circuit & code are attached

---

📌 **Submitted by: Vineet Singhal (ID: 2025A7PS0089H)**
