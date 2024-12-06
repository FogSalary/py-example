import os
import numpy as np
import matplotlib.pyplot as plt


current_path = os.path.dirname(__file__)

x = np.linspace(0, np.pi, 100)
y = np.sin(x)

fig = plt.figure(figsize=(4, 4))
plt.plot(x, y)
plt.title("Sin curve figure")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.pause(3)
plt.savefig(os.path.join(current_path, "fig1.png"))
plt.close()
