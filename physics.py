import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Important variables for simulation (step in seconds)
step = 0.05
numstep = 1000

# Initial values for amplitude and frequency
amp = 1.0
freq1 = 1.0
freq2 = 2.0
damping = 0.25

# Defining a function to compute the y values for plotting
def data_gen():
    t = 0
    ctr = 0
    for ctr in range(numstep):
        # Calculating the y value for each wave at a given time (1 Hz)
        y1 = amp * np.sin(2 * np.pi * freq1 * t)
        # SHM wave with twice the frequency
        y2 = amp * np.sin(2 * np.pi * freq2 * t)
        # SHM wave with a damping coefficient i.e. damped sine wave
        y3 = amp * np.sin(2 * np.pi * freq1 * t) * np.exp(-t * damping)
        t += step
        yield t, y1, y2, y3

# Create a figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Initializations for plotting
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(-(amp + 0.2), (amp + 0.2))
    ax.set_xlim(0, 10)
    ax.grid()
    ax.set_xticks(np.arange(1, 11))

# Data arrays to store the values for plotting
xdata, y1data, y2data, y3data = [], [], [], []

# Initialize three line objects (one in each subplot)
line1, = ax1.plot(xdata, y1data, color='b')
line2, = ax2.plot(xdata, y2data, color='r')
line3, = ax3.plot(xdata, y3data, color='g')
line = [line1, line2, line3]

# Set the title for each subplot
ax1.set_title('SHM wave with frequency of 1 Hz', size=10)
ax2.set_title('SHM wave with frequency of 2 Hz', size=10)
ax3.set_title('Damped sine wave with decay constant of 0.25', size=10)

# Label x axis
ax3.set_xlabel('Time (s)', size=15)

# Function to update the plot with new data
def calculate(data):
    x, y1, y2, y3 = data
    xdata.append(x)
    y1data.append(y1)
    y2data.append(y2)
    y3data.append(y3)

    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)
    line[2].set_data(xdata, y3data)
    return line

# Adjust the layout of the sliders
fig.subplots_adjust(bottom=0.25)

# Create sliders for parameter adjustment
ax_amp = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_freq1 = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_freq2 = plt.axes([0.2, 0.09, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_damping = plt.axes([0.2, 0.13, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_amp = Slider(ax_amp, 'Amplitude', 0.1, 5.0, valinit=amp)
slider_freq1 = Slider(ax_freq1, 'Freq1 (Hz)', 0.1, 10.0, valinit=freq1)
slider_freq2 = Slider(ax_freq2, 'Freq2 (Hz)', 0.1, 10.0, valinit=freq2)
slider_damping = Slider(ax_damping, 'Damping', 0.01, 1.0, valinit=damping)

# Update function for sliders
def update(val):
    global amp, freq1, freq2, damping
    amp = slider_amp.val
    freq1 = slider_freq1.val
    freq2 = slider_freq2.val
    damping = slider_damping.val

# Attach the update function to the sliders
slider_amp.on_changed(update)
slider_freq1.on_changed(update)
slider_freq2.on_changed(update)
slider_damping.on_changed(update)

# Animation function
ani = animation.FuncAnimation(fig, calculate, data_gen, blit=True, interval=50, repeat=False)

# Display the plot
plt.show()
