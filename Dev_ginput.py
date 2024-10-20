import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the Fourier series with 3 sine components, feel free to modify!
def fourier_series(x):
    return np.sin(x) + 0.5 * np.sin(3 * x) + 0.15 * np.sin(25 * x) + 0.15 * np.sin(50 * x)

# Create the Fourier series
x = np.linspace(0, 2 * np.pi, 1000)
y_fourier = fourier_series(x)

# Plot curve
fig, ax = plt.subplots()
ax.plot(x, y_fourier, label='Fourier Series')
ax.axhline(0, color='black', linewidth=0.5)  # Add zero line for the x-axis
ax.grid(True, which='both', color='lightgray', linestyle=':', linewidth=0.5)  # Add light gray dotted grid lines
ax.set_title('Select two points on the Fourier series curve')
ax.set_xlabel('time in seconds')  # Change x-axis title to 'time in seconds'
ax.set_ylabel('Light Intensity')  # Change y-axis title to 'Light Intensity'
ax.legend()

# Function to handle mouse clicks
points = []

def onclick(event):
    if len(points) < 2:
        points.append(event.xdata)
        ax.plot(event.xdata, event.ydata, 'ro')
        fig.canvas.draw()
        if len(points) == 2:
            integrate_area()

def integrate_area():
    x1, x2 = sorted(points)
    area, _ = quad(fourier_series, x1, x2)
    ax.fill_between(x, y_fourier, where=(x >= x1) & (x <= x2), color='gray', alpha=0.5)
    ax.fill_between(x, y_fourier, where=(x >= x1) & (x <= x2), facecolor='none', hatch='/'*int(5.5), edgecolor='red')  # Increase spacing of red hashed lines by a factor of 1.2, feel free to change
    ax.set_title(f'Energy efficiency is {area:.2f}')  # Change title under the curve to 'energy efficiency is'
    fig.canvas.draw()

# Connect the click event to the handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
