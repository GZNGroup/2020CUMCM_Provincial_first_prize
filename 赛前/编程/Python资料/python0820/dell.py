import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)
t = np.linspace(0, 3.2, 100)

fig, ax = plt.subplots()

plt.ion()
for i in t:
    plt.cla()
    u = np.sin(x - i)
    ax.scatter(x, u, c='r', label='sine function')
    plt.pause(0.02)
plt.ioff()

plt.show()
