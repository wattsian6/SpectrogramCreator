import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy
from scipy import signal
# Read the wav file (mono)
Fs, signalData = wavfile.read('07-00-00-left.wav')
plt.title('Spectrogram of a wav file of Bees')
spectrum, freqs, t, im = plt.specgram(signalData, Fs=16000, NFFT=16384, noverlap=1024)
im._interpolation = 'sinc'
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.yscale('log')
plt.ylim(ymax=8000)
plt.ylim(ymin=10)
plt.show()
#plot.savefig('spectrogram.png')
