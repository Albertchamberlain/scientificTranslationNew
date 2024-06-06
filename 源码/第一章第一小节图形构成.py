import scipy
import numpy as np
import matplotlib.pyplot as plt

plt.plot(range(10))
plt.show()

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(aspect=1)
ax.plot(range(10))
plt.show()

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"aspect": 1})
ax.plot(range(10))
plt.show()