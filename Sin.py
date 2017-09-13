import numpy as np 
import pylab as pl
x = np.linspace(-3*np.pi, 3*np.pi, 2014)
y = np.sin(x)
pl.plot(x, y, 'r',ls="--", linewidth=0.5)
pl.grid(True)
pl.savefig('Sin.png')