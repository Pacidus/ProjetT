#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scipy.spatial import SphericalVoronoi as sphV
import matplotlib.pyplot as plt
import numpy as np
import noise

h = 200
theta = np.linspace(0, np.pi, h)
phi = np.linspace(0, 2 * np.pi, 2 * h)
r = 0.7
x0, y0, z0 = 2 * (np.random.rand(3) - 0.5)


def surf(r, t, p):
    x = x0 + r * np.sin(t) * np.cos(p)
    y = y0 + r * np.sin(t) * np.sin(p)
    z = z0 + r * np.cos(t)
    return noise.snoise3(x, y, z, octaves=10)


def distcirc(r, phi1, phi2, theta1, theta2):
    sin = np.sin((phi2 - phi1) / 2)
    sinp2 = sin * sin
    sin = np.sin((theta2 - theta1) / 2)
    sint2 = sin * sin
    cosp = np.cos(phi1) * np.cos(phi2)

    return 2 * r * np.arcsin(np.sqrt(sinp2 + cosp * sint2))


img = np.array([[surf(r, t, p) for p in phi] for t in theta])

img = (img - img.min()) / (img.max() - img.min())

img[img < 0.65] = 0

plt.imshow(img)
plt.show()
