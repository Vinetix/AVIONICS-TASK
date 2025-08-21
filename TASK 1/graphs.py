# VINEET SINGHAL 2025A7PS0089H

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from matplotlib.widgets import RadioButtons
from pathlib import Path

"""1. Load and process the data"""

#Load CSV file
BASE_DIR = Path(r"D:\Vineet_Singhal_2025A7PS0089H_JANUS\TASK 1\correct&smooth_data.csv").resolve().parent
input_path = BASE_DIR / "correct&smooth_data.csv"

# Reads the raw test flight dataset into a DataFrame
df = pd.read_csv(input_path)

# Extract Altitude, Velocity and Time columns 
smooth_altitude = df['Altitude(m)'].astype(float).to_numpy()
smooth_velocity = df['Velocity(m/s)'].to_numpy()
time = df['Time(s)'].to_numpy()

#By default, start in "ALtitude" mode 
current_mode = "Altitude"
ydata = smooth_altitude

"""2. Set up the figure and axes"""
fig,ax = plt.subplots(figsize=(9,5))

#Animate line and point(moving marker)
line, = ax.plot([],[],'#141B9C',label = "Altitude",linestyle = '--')
point, = ax.plot(0,0,'ro') #red point marker

## Adjust layout for radio button space
plt.subplots_adjust(right=0.8,bottom=0.13)

"""3. Add radio button for mode toggle"""
ax_radio = plt.axes([0.825, 0.6, 0.16, 0.18])
## Toggle options : Velocity & Altitude
radio = RadioButtons(ax_radio,("Altitude","Velocity"),label_props=
                     {'fontsize':[15,15]},radio_props={'s':[60,60],'facecolor':'m'})

"""4. Initial plot setup"""
ax.set_xlim(0,max(time)+1)
ax.set_ylim(min(smooth_altitude)-30,max(smooth_altitude)+100)
ax.set_yticks(np.arange(0,500,50))
ax.set_xlabel("Time(in seconds)",fontdict={'fontname':'arial','fontweight':5,'fontsize' : 14,'color':'#590808'})
ax.set_ylabel("Altitude(in m)",fontdict={'fontname':'arial','fontweight':5,'fontsize' : 14,'color':'#590808'})
ax.set_title("Altitude vs Time",fontdict={'fontweight':100,'fontsize' : 20,'color':'#DE2B1F'})
ax.legend(loc='best',labelcolor="#08400E",frameon=True,shadow=True
           ,edgecolor='black',fancybox=True,facecolor="#FFFFA5",
           prop={'weight':'bold','size':13},handlelength=2.5)
ax.grid(True)

"""5. Helper function for line style"""
def style_set(style,width,color):
    line.set_linestyle(style)
    line.set_linewidth(width)
    line.set_color(color)
    
"""6. Autoscale when toggling"""    
def autoscale(the_label):
    """Reset axes, labels, styles whenever mode changes (Altitude/Velocity)"""
    # Clear old data so no ghosting remains
    line.set_data([], [])
    point.set_data([], [])
    if the_label == "Altitude":
        ax.set_ylim(min(smooth_altitude)-30,max(smooth_altitude)+100)
        ax.set_yticks(np.arange(0,500,50))
    else:    
        ax.set_ylim(min(smooth_velocity)-10,max(smooth_velocity)+30)
        ax.set_yticks(np.arange(-40,85,10))
    ax.set_xlabel("Time(in seconds)",fontdict={'fontname':'arial','fontweight':5,'fontsize' : 14,'color':'#590808'})
    ax.set_ylabel(f"{the_label}(in m)",fontdict={'fontname':'arial','fontweight':5,'fontsize' : 14,'color':'#590808'})
    ax.set_title(f"{the_label} vs Time",fontdict={'fontweight':100,'fontsize' : 20,'color':'#DE2B1F'})
    line.set_label(f"{the_label}")
    if the_label == "Velocity":
        style_set(':',2.5,'g') # green dotted line
    else:
        style_set('--',1.5,'b') # blue dashed line
    ax.legend(loc='best',labelcolor="#08400E",frameon=True,shadow=True
           ,edgecolor='black',fancybox=True,facecolor="#FFFFA5",
           prop={'weight':'bold','size':13},handlelength=2.5)
    ax.grid(True)
    fig.canvas.draw_idle()

"""7. Callback for radio button"""
def on_selected(label):
    # Called when user clicks a radio button
    global current_mode 
    current_mode = label
    autoscale(label)
    ani.frame_seq = ani.new_frame_seq() # Restart animation from beginning 

"""8. Update function for animation"""
def update(frame):
    """Animates the graph frame by frame."""
    global ydata
     # Pick dataset depending on mode
    if current_mode == "Altitude":
        ydata = smooth_altitude
    else:
        ydata = smooth_velocity
        
    # Different cases for animation frames
    if frame == 0:
        # keep empty until first frame arrives
        line.set_data([], [])
        point.set_data([], [])
    elif frame < len(time):
         # Progressive plotting
        x = time[:frame]
        y = ydata[:frame]
        line.set_data(x, y)
        point.set_data([time[frame-1]], [ydata[frame-1]])
    else:
        # # When animation finishes, show full graph
        line.set_data(time, ydata)
        point.set_data([time[-1]], [ydata[-1]])
    return line,point

"""9. Run animation"""
ani = FuncAnimation(fig,update,frames=len(time)+10,interval=100)
radio.on_clicked(on_selected)
plt.show()