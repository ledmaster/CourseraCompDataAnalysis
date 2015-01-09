import numpy as np
import pylab

def sechavg():
    L = 30
    n = 512
    x = np.linspace(-L, L, n+1)
    x = x[:-1]
    k = (2.*np.pi/(2.*L))*np.array((range(n/2) + range(-n/2,0)))
    ks = np.fft.fftshift(k)
    
    noise = 30.
    u = 2. / (np.exp(x) + np.exp(-x)) #sech
    ut = np.fft.fft(u)
    
    realizations = 100
    ave = np.zeros(n)
    for j in xrange(realizations):
        utn = ut + noise*(np.random.randn(n) + np.imag(np.random.randn(n)))
        ave += utn
    
    utna = ave / realizations
    
    una = np.fft.ifft(utna)

    f, axarr = pylab.subplots(3)
    
    axarr[0].plot(x,u)
    axarr[1].plot(ks,abs(np.fft.fftshift(utna)))
    axarr[2].plot(x,abs(una))
    pylab.show()

sechavg()
