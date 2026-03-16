import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0,1,500)

clean = np.sin(2*np.pi*5*t)

noise = np.random.normal(0,0.5,t.shape)

noisy = clean + noise

filtered = signal.savgol_filter(noisy, 51, 3)

plt.plot(t,noisy,label="noisy")
plt.plot(t,filtered,label="filtered")
plt.legend()
plt.show()