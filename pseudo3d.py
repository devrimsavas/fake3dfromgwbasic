import matplotlib.pyplot as plt
import numpy as np

def FNA(X, Y):
    return 1 / (np.cos(X / 2) * np.cos(Y * 1.1) + 1.1 )

fig, ax = plt.subplots(figsize=(15,15))
ax.set_aspect('equal', 'box')
ax.set_facecolor('lightgray')
#ax.axis('off')
ax.set_facecolor('gray')

offset = -50  # Offset
colormap = plt.get_cmap("viridis")

# Loop for Y
for Y in np.arange(0, 8.25, 0.25):
    X = 0
    x1 = 20 * (Y + X) + 50 + offset
    y1 = -(Y - X + 2 + FNA(X, Y)) * 6 + 150
    ax.scatter(x1, y1, color=colormap(Y/8), s=15)  
    
    # Inner  X
    for X in np.arange(0.25, 8.25, 0.25):
        x2 = 20 * (Y + X) + 50 + offset
        y2 = -(Y - X + 2 + FNA(X, Y)) * 6 + 150
        ax.plot([x1, x2], [y1, y2], color=colormap(Y/8), linewidth=3)  
        x1, y1 = x2, y2
    
    x2 = 20 * (Y + 8) + 50 + offset
    y2 = -(Y - X + 2) * 6 + 150
    ax.plot([x1, x2], [y1, y2], color=colormap(Y/8), linewidth=3)

# Loop for X
for X in np.arange(0, 8.25, 0.25):
    x1 = 20 * X + 50 + offset
    y1 = -(-6 * X + 12 - 150)
    ax.scatter(x1, y1, color=colormap(X/8), s=15)  
    
    # Inner Y
    for Y in np.arange(0, 8.25, 0.25):
        x2 = 20 * (Y + X) + 50 + offset
        y2 = -(Y - X + 2 + FNA(X, Y)) * 6 + 150
        ax.plot([x1, x2], [y1, y2], color=colormap(X/8), linewidth=3)
        x1, y1 = x2, y2

#  view
ax.set_xlim(0, 300)
ax.set_ylim(300, 0)  #  y-axis inverted 

plt.show()


