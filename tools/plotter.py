from collections import deque
from threading import Thread

import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np
import serial

N = 256
s = serial.Serial("COM113", 115200)
q = deque(maxlen=N)
T = 1.0 / 1000.0

x = np.linspace(0.0, N*T, N)

def plot_spectrum():
    try:
        a = np.array(q) - np.mean(q)
        yf = scipy.fftpack.fft(a)
        xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
        plt.subplot(2, 1, 1)
        yfft = 2.0/N * np.abs(yf[:N//2])
        plt.plot(xf[xf < 20], yfft[xf < 20])
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.plot(a)
        plt.grid()
    except:
        pass

def read():
    global q, s
    while True:
        try:
            q.append(int(
                s.read_until(b"\r\r\n<info> app:")\
                .decode("utf-8")\
                .split("\r\r\n<info> app:")[0]))
        except:
            pass

Thread(target=read).start()

while True:
    try:
        plt.cla()
        plt.clf()
        plt.plot(q)
        plt.grid()
        plt.pause(0.1)

        if False:
            plot_spectrum()

    except:
        pass
