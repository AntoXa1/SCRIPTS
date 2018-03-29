#!/Users/dora/anaconda3/bin/python

import numpy as np

import matplotlib.pyplot as plt


Ns = 4

dT = 1.0 / 4

fs = 1/dT

t = np.linspace(0.0, Ns*dT, Ns)

y = np.sin(50.0 * 2.0*np.pi*t) 


# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

plt.plot(t, y )

# plt.grid()

plt.show()

res=1