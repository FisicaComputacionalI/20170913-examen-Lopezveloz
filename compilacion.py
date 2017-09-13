import numpy as np 
import pylab as pl
x= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
y= [1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
pl.plot(x,y, 'k',linewidth=10)
x1= np.linspace(-3*np.pi, 3*np.pi, 22)
y2= np.sin(x)
pl.figure(1)
pl.subplot(211)
pl.plot(x1,y2, 'g', linewidth=3)
pl.axis([-10, 22, -1, 2050])
pl.grid(True)
pl.subplot(212)
x = np.linspace(-3*np.pi, 3*np.pi, 100)
y = np.sin(2014*x)
pl.plot(x, y, 'r',ls="--", linewidth=0.5)
pl.grid(True)
pl.savefig('compilacion.png')