from matplotlib import colors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from scipy.spatial import SphericalVoronoi
from mpl_toolkits.mplot3d import proj3d
import numpy as np


def SphCart(r, t, p):
    x = x0 + r * np.sin(t) * np.cos(p)
    y = y0 + r * np.sin(t) * np.sin(p)
    z = z0 + r * np.cos(t)
    return np.array([x, y, z]).T

# set input data

x0, y0, z0 = 0, 0, 0
SphCart(1, np.random.rand(200)*np.pi*2, np.random.rand(200)*np.pi)
points = np.random.normal(size = (3,200))
points /= np.linalg.norm(points, axis = 0)
points = points.T


radius = 1

center = np.array([x0, y0, z0])

sv = SphericalVoronoi(points, radius, center)

# sort vertices (optional, helpful for plotting)

sv.sort_vertices_of_regions()

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# plot the unit sphere for reference (optional)

u = np.linspace(0, 2 * np.pi, 100)

v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))

y = np.outer(np.sin(u), np.sin(v))

z = np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='y', alpha=0.1)

# plot generator points

ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b.')

# plot Voronoi vertices

ax.plot(sv.vertices[:, 0], sv.vertices[:, 1], sv.vertices[:, 2], 'g.')

# indicate Voronoi regions (as Euclidean polygons)

for region in sv.regions:

   random_color = colors.rgb2hex(np.random.rand(3))

   polygon = Poly3DCollection([sv.vertices[region]], alpha=1.0)

   polygon.set_color(random_color)

   ax.add_collection3d(polygon)

plt.show()
