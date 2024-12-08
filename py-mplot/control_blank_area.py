import os
import numpy as np
import matplotlib.pyplot as plt


"""
    Show how to adjust the blank area in figure windows.
"""

current_path = os.path.dirname(__file__)
output_path = os.path.join(current_path, 'blank_output')
os.makedirs(output_path, exist_ok=True)

x = np.linspace(0, np.pi, 200)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
# plt.pause(3)
plt.savefig(os.path.join(output_path, 'fig1.png'))
plt.close()

# plt.tight_layout() will auto adjust subplot layout to decrease blank area
fig, ax = plt.subplots()
ax.plot(x, y)
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'fig2.png'))
plt.close()


# use bbox_inches = 'tight' in savefig function can decrease blank area
fig, ax = plt.subplots()
ax.plot(x, y)
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'fig3.png'), bbox_inches='tight')
plt.close()


# manual use subplots.adjust parameter
fig, ax = plt.subplots()
ax.plot(x, y)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # 调整边距
plt.savefig(os.path.join(output_path, 'fig4.png'), bbox_inches='tight')
plt.close()


# use fig.subplots_adjust do more precise layout control
fig, ax = plt.subplots()
ax.plot(x, y)
# fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Distance (m)")
plt.savefig(os.path.join(output_path, 'fig5.png'), bbox_inches='tight')
plt.close()


# adjust figure size
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y)
# plt.tight_layout()
plt.savefig(os.path.join(output_path, 'fig6.png'), bbox_inches='tight')
plt.close()



# remove axis and border (if suitable)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.axis('off')
plt.savefig(os.path.join(output_path, 'fig7.png'), bbox_inches='tight')
plt.close()