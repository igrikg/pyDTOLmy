# -*- coding: utf-8 -*-
"""
Created on Fri May 16 14:15:43 2014

@author: Jens Brauer
"""

from DTOL import DTOL
import matplotlib.pyplot as plt
import numpy as np


io = DTOL(name='DT9802(00)')
data = io.setupAiLiveview()
dataneu = []


for datai in data:
    for val in datai:
        dataneu.append(io.CodeToVolts(val))

plt.plot(np.linspace(0,10,len(dataneu)),dataneu)
plt.xlabel('Time / s')
plt.ylabel('Voltage / V')
plt.show()


