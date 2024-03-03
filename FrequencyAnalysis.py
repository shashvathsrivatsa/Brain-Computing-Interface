import AggregateData
import matplotlib.pyplot as plt
import numpy as np

data = AggregateData.getData()

# Perform FFT
fft_result = np.fft.fft(data)
frequencies = np.fft.fftfreq(len(data), d=1.0/256)  # Assuming data is sampled at 256 Hz

# Plot the frequency spectrum
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
