import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('myvoice8.wav')
print(data.shape)

plt.plot(data);
plt.show()
'''fs2,data2=wav.read('high_voice.wav')
print(fs,fs2)
t1=np.arange(0,len(data)/fs,1.0/fs)
t2=np.arange(0,len(data2)/fs2,1.0/fs2)
#print(data)
a1=plt.subplot(211)
a1.plot(t1,data[0:len(t1)])
a2=plt.subplot(212,sharex=a1)
a2.plot(t2,data2[0:len(t2)])
plt.show()
'''
wav.write('high_voice.wav',0.5*fs,data)
