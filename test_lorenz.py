from lorenz import simulate_lorenz, create_lorenz_gif
import torch

t = torch.linspace(0, 40, 2000)
initial = torch.tensor([1.0, 1.0, 1.0])
trajectory = simulate_lorenz(initial, t)

create_lorenz_gif(trajectory)

print("🦋 Animated Lorenz GIF saved to assets/lorenz.gif")
