import os
import random
import numpy as np
import matplotlib.pyplot as plt


def amplify_circle_error(radius, pos_xy, amplify_factor=20):
    nr_list = []
    for i in range(point_num):
        nx, ny = pos_xy[:, i]
        nr = np.sqrt(nx**2+ny**2)
        nr_list.append(nr)
    nr_arr = np.array(nr_list)
    r_diff = (nr_arr - np.ones((point_num, )) * radius ) / radius
    amplify_xy_pos = noise_xy_pos * (1+10*r_diff)
    return amplify_xy_pos


point_num = 500
radius = 100
center_x, center_y = 0, 0
theta = np.linspace(0, 2*np.pi, point_num)
x = center_x + radius * np.cos(theta)
y = center_y + radius * np.sin(theta)

# # (500, ) -> (500, 2)
# xy_pos = np.column_stack((x, y))
# xy_pos = np.stack((x, y), axis=1)
# xy_pos = np.vstack((x, y)).T

# # (500, ) -> (2, 500)
xy_pos = np.vstack((x, y))


z = np.ones((point_num, )) * 0

# z_noise = z + np.random.random((500, ))
x_noise = np.random.uniform(-0.5, 0.5, size=(point_num, ))
y_noise = np.random.uniform(-0.5, 0.5, size=(point_num, ))
z_noise = np.random.uniform(-0.3, 0.3, size=(point_num, ))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color="tab:orange")
ax.plot(x, y, z_noise, color='tab:blue')

ax.set_title('3D Circle Trajectory')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim([-0.5, 0.5])

# plt.pause(4)
plt.close()


amplify_factor = 2
fig = plt.figure()
ax = fig.add_subplot(111)
noise_x1 = x + x_noise
noise_y1 = y + y_noise
noise_z1 = z + z_noise

nr_list = []
noise_xy_pos = np.vstack((noise_x1, noise_y1))
for i in range(point_num):
    nx, ny = noise_xy_pos[:, i]
    nr = np.sqrt(nx**2+ny**2)
    nr_list.append(nr)
nr_arr = np.array(nr_list)
r_diff = (nr_arr - np.ones((point_num, )) * radius ) / radius

amplify_xy_pos = noise_xy_pos * (1+20*r_diff)

result_xy_pos = amplify_circle_error(radius, noise_xy_pos, 10)

noise_x1_an = x + x_noise * amplify_factor
noise_y1_an = y + y_noise * amplify_factor
noise_z1_an = z + z_noise * amplify_factor
ax.plot(x, y, color="tab:orange")
ax.plot(noise_x1, noise_y1, color='tab:blue')
# ax.plot(noise_x1_an, noise_y1_an, color="tab:green")
# ax.plot(amplify_xy_pos[0,:], amplify_xy_pos[1,:], color="tab:green")
ax.plot(result_xy_pos[0,:], result_xy_pos[1,:], color="tab:green")
ax.set_aspect('equal')

for i in range(0, point_num, int(point_num/50)):
    ax.plot([center_x, result_xy_pos[0,i]], [center_y, result_xy_pos[1,i]], color='k')
    # ax.plot([center_x, amplify_xy_pos[0,i]], [center_y, amplify_xy_pos[1,i]], color='k')
    # ax.plot([center_x, noise_x1_an[i]], [center_y, noise_y1_an[i]], color='k')

# plt.pause(4)
# plt.close()
plt.show()

