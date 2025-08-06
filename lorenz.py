import torch
from torchdiffeq import odeint
import matplotlib.pyplot as plt
import numpy as np

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
    x, y, z = state.T
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(projection="3d")
    ax.plot(x, y, z, color='purple', linewidth=1.2)
    ax.set_title("Lorenz Attractor - Our Chaotic Love 🦋")
    ax.set_axis_off()
    plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()
