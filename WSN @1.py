import numpy as np
import matplotlib.pyplot as plt

# Constants
d0 = 1  # Reference distance in meters
gamma = 3.2  # Path loss exponent
freq = 900e6  # Frequency in Hertz
c = 3e8  # Speed of light in meters per second

# Antenna gains
Gtx = 0  # Transmit antenna gain in dBi
Grx = 0  # Receive antenna gain in dBi

# Path loss calculation function
def path_loss(distance):
    return 20 * np.log10(distance / d0) + 20 * np.log10(freq / (4 * np.pi * c)) + 10 * gamma * np.log10(distance / d0)

# Generate distance values
distances = np.linspace(1, 1000, 100)  # from 1 to 1000 meters

# Calculate path loss values
path_losses = path_loss(distances)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(distances, path_losses, label='Path Loss')
plt.title('Path Loss vs Distance')
plt.xlabel('Distance [m]')
plt.ylabel('Path Loss [dB]')
plt.legend()
plt.grid(True)
plt.show()
