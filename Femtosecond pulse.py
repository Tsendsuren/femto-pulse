# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:44:48 2018

@author: Tsende
"""
import numpy as np
import matplotlib.pyplot as plt

E0 = 1;
t = np.arange(-10e-15,10e-15,0.01e-15);
tau = 5e-15;
b = 0;
phi1 = 0;
phi2 = -np.pi/2;
phi1_t = phi1+b*np.power(t,2);
phi2_t = phi2+b*np.power(t,2);
c = 299792458;

lambd = 800e-9;
omega = 2*np.pi*c/lambd;

E1 = np.multiply(np.exp(-2*np.log(2)*np.power(t,2)/tau**2),np.exp(-1j*(np.multiply(omega,t)+phi1_t)));
E2 = np.multiply(np.exp(-2*np.log(2)*np.power(t,2)/tau**2),np.exp(-1j*(np.multiply(omega,t)+phi2_t)));
plt.plot(t*1e15,np.real(E1),'b', t*1e15,np.real(E2),'m--',t*1e15,np.abs(E2),'r-',linewidth=0.75)
plt.xlabel('Time (fs)')
plt.ylabel('Electric field (normalized)')
plt.legend(('$\phi=0$','$\phi=-\pi/2$','Envelope'),
           loc='upper right', shadow=True)
#plt.grid(True)
plt.axis([-12, 12,-1.3, 1.3])
plt.savefig("Femtosecond pulse.pdf", dpi=900)
