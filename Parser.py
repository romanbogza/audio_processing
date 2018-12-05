import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import json


def spectogram():
	sample_rate, samples = wavfile.read(r'.\Test Objects\1\RE3a6bbd996a111dba2fb87ead15598890.wav')
	frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
	plt.pcolormesh(times, frequencies, spectrogram)
	plt.imshow(spectrogram)
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.show()
def load_json():
	with open(r'.\Test Objects\1\3716302-FNe54a0db6f042444dfeb155ffc7765ff5.json') as json_data:
	    d = json.load(json_data)
	    print(d)

spectogram()
load_json()