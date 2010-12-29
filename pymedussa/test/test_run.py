import medussa
import numpy as np
#from pal import signal
from time import sleep
import sys

fs = 44100.0
x,fs = medussa.readfile("clean.wav")
#y = np.hstack((x,x))
#x,fs = medussa.readfile("speech-noise-tone.wav")
#shape =x.shape
#x[:,0] = 1.0
#x[:,1] = 2.0
#x[:,2] = 3.0

d = medussa.open_device()
sleep(0.5)
s1 = d.open_array(x,fs)
s2 = d.open_file("clean.wav")
s3 = d.create_tone(400,fs)
#s = d.create_white(44100)
#s.play()
#sleep(6)



def sweep_right(s, delta=0.001, steps=500):
    s.play()
    fade = np.linspace(0.0, 1.0, steps)
    for i in xrange(steps):
        s.mix_mat = np.array([1.0-fade[i], fade[i]])
        sleep(delta)
    s.pause()

def sweep_left(s, delta=0.001, steps=500):
    s.play()
    fade = np.linspace(0.0, 1.0, steps)
    for i in xrange(steps):
        s.mix_mat = np.array([fade[i], 1.0-fade[i]])
        sleep(delta)
    s.pause()
