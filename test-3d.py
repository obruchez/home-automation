import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define the corners of the rectangle
#corner1 = np.array([lon1, lat1, alt1])
#corner2 = np.array([lon2, lat2, alt2])
#corner3 = np.array([lon3, lat3, alt3])
#corner4 = np.array([lon4, lat4, alt4])
corner1 = np.array([43.1, 17.1, 830])
corner2 = np.array([43.1, 17.2, 830])
corner3 = np.array([43.2, 17.2, 830])
corner4 = np.array([43.2, 17.1, 830])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the rectangle edges
edges = [
    [corner1, corner2],
    [corner2, corner3],
    [corner3, corner4],
    [corner4, corner1]
]

for edge in edges:
    xs, ys, zs = zip(*edge)
    ax.plot(xs, ys, zs, color='b')

# Plot the rectangle faces
verts = [[corner1, corner2, corner3, corner4]]
ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.2))

# Set plot labels
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Altitude')

# Set plot limits
#ax.set_xlim([min(lon1, lon2, lon3, lon4), max(lon1, lon2, lon3, lon4)])
#ax.set_ylim([min(lat1, lat2, lat3, lat4), max(lat1, lat2, lat3, lat4)])
#ax.set_zlim([min(alt1, alt2, alt3, alt4), max(alt1, alt2, alt3, alt4)])

# Set camera position
ax.view_init(elev=30, azim=45)  # Change elevation (angle above the x-y plane) and azimuth (angle around the z-axis)

plt.show()
