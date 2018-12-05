import matplotlib.pyplot as plt
import scipy
from scipy import signal
from scipy.io import wavfile
import json
from pydub import AudioSegment
from os import listdir
from os.path import isfile, join
import os
from scipy.fftpack import fft


def load_json(audio):
	with open(r'.\Test Objects\1\3716302-FNe54a0db6f042444dfeb155ffc7765ff5.json') as json_data:
	    parser = json.load(json_data)
	    total_items = len(parser['results']['items'])
	    for i in range(0, total_items):
	    	if 'start_time' in parser['results']['items'][i]:
	    		start_time = parser['results']['items'][i]['start_time']
	    		end_time = parser['results']['items'][i]['end_time']
	    		word = parser['results']['items'][i]['alternatives'][0]['content']
	    		audio.split(float(start_time), float(end_time), word)
	    	
class audio_split():
	def __init__(self):
		self.newAudio = AudioSegment.from_wav(r'.\Test Objects\1\RE3a6bbd996a111dba2fb87ead15598890.wav')

	def split(self, start_time, end_time, word):
		t1 = start_time * 1000
		t2 = end_time * 1000
		newAudio = self.newAudio[t1:t2]
		newAudio.export(r'.\Test Objects\1\parsed\\' + word + '_audio.wav', format="wav")

class plotting_signals():
	def __init__(self):
		self.path = r'C:\Users\Roman\Documents\audio_processing\Test Objects\1\parsed'
		self.audiofiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
		self.sample_rate, self.samples = wavfile.read(self.path + os.sep + self.audiofiles[0])
	
	def specto(self):
		frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
		plt.pcolormesh(times, frequencies, spectrogram)
		plt.imshow(spectrogram)
		plt.ylabel('Frequency [Hz]')
		plt.xlabel('Time [sec]')
		plt.show()
	def fft(self):
		b=[(ele/2**32.)*2-1 for ele in self.samples]
		c = fft(b)
		d = len(c)/2
		plt.plot(abs(c[:(d-1)]),'r') 
		plt.show()


# audio = audio_split()
# load_json(audio)
sig_analys = plotting_signals()
sig_analys.fft()
