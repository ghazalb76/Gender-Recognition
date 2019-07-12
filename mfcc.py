

import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob
from scipy.io import wavfile
import numpy as np

a = []

path = 'data/male/*.wav'
for filename in glob.glob(path):
    fs, signal = wavfile.read(filename)
    spectrum = np.fft.fft(signal)
    phase = np.angle(spectrum)
    a.append(len(a))

print(max(a))
print(min(a))
# x = np.arange(0, len(phase), 1)
# plt.plot(x, phase)
# plt.show()
