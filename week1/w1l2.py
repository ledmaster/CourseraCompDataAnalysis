import numpy as np
import pylab

def sechfilter():
    L = 30
    n = 512
    x = np.linspace(-L, L, n+1)
    x = x[:-1]
    k = (2.*np.pi/(2.*L))*np.array((range(n/2) + range(-n/2,0)))
    ks = np.fft.fftshift(k)
    
    noise = 10.
    u = 2. / (np.exp(x) + np.exp(-x)) #sech
    ut = np.fft.fft(u)
    
    utn = ut + noise*(np.random.randn(n) + np.imag(np.random.randn(n)))
    
    un = np.fft.ifft(utn)
    
    filter = np.exp(-0.2*k**2)
    
    unft = np.multiply(filter,utn)
    unf = np.fft.ifft(unft)
    
    
    f, axarr = pylab.subplots(4)
    
    axarr[0].plot(x,u)
    axarr[1].plot(x,abs(un))
    axarr[2].plot(ks,abs(np.fft.fftshift(unft))/max(abs(np.fft.fftshift(unft))))
    axarr[3].plot(x,abs(unf))
    pylab.show()

sechfilter()
