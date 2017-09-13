import numpy as np 
import pylab as pl
x = np.linspace(-3*np.pi, 3*np.pi, 100)
y = np.sin(2014*x)
pl.plot(x, y, 'r',ls="--", linewidth=0.5)
pl.grid(True)
pl.savefig('Sin.png')