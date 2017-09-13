import numpy as np 
import pylab as pl 
# Crea un vector (arreglo) con los valores del eje X 
x= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# Crea un vector (arreglo) con los valores en el eje Y para cada vector en el eje X 
y= [1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
# Grafica el vector x contra el vector y 
pl.plot(x,y)
pl.ylabel('Anio')
pl.xlabel('Edad')
pl.title('Lopezveloz Martinez Itzia')
pl.axis([0, 22, 1996, 2018])
pl.grid(True)
# Guarda la grafica en formato png
pl.savefig('temp1.png')
