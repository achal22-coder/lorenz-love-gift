import torch
from torchdiffeq import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio

def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return torch.tensor([dx, dy, dz])

def simulate_lorenz(initial_state, t):
    state = odeint(lorenz, initial_state, t)
    return state.detach().numpy()

def plot_lorenz(state, save_path="assets/lorenz.png"):
    os.makedirs("assets", exist_ok=True)
    
    x, y, z = state.T

    # Create gradient colors
    points = np.array([x, y, z]).T.reshape(-1, 1, 3)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    from matplotlib.collections import Line3DCollection
    fig = plt.figure(figsize=(10, 6), facecolor='black')
    ax = fig.add_subplot(projection='3d')

    # Set color gradient
    norm = plt.Normalize(z.min(), z.max())
    colors = plt.cm.plasma(norm(z))

    # Create line segments and color them
    for i in range(len(x)-1):
        ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=colors[i])

    # Style the plot
    ax.set_facecolor("black")
    ax.set_title("Lorenz Attractor — Our Chaotic Love 🦋", color='white', fontsize=14, pad=20)
    ax.set_axis_off()

    # Optional: add text inside the plot
    ax.text2D(0.05, 0.95, "Built on chaos. Bound by love.", transform=ax.transAxes, color='white', fontsize=10)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

    def create_lorenz_gif(state, save_path="assets/lorenz.gif"):
        os.makedirs("assets", exist_ok=True)

    x, y, z = state.T
    frames = []

    fig = plt.figure(figsize=(8, 6), facecolor='black')
    ax = fig.add_subplot(projection='3d')

    for i in range(10, len(x), 10):
        ax.clear()
        ax.set_facecolor('black')
        ax.set_axis_off()

        # Plot the current portion of the trajectory
        ax.plot(x[:i], y[:i], z[:i], color='hotpink', linewidth=1.8)

        ax.set_title("Our Chaotic Love 🦋", color='white', fontsize=12, pad=20)
        ax.text2D(0.05, 0.9, "Built on chaos, bound by love.", transform=ax.transAxes, color='white', fontsize=9)

        # Save this frame to a temporary buffer
        fname = f"assets/frame_{i}.png"
        plt.savefig(fname, bbox_inches='tight', facecolor='black')
        frames.append(imageio.imread(fname))

    # Save the gif
    imageio.mimsave(save_path, frames, fps=20)

    # Cleanup: remove temp frames
    for f in frames:
        os.remove(f.name)
    
    plt.close()