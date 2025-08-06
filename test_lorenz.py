from lorenz import simulate_lorenz, plot_lorenz
import torch

t = torch.linspace(0, 40, 2000)
initial = torch.tensor([1.0, 1.0, 1.0])
trajectory = simulate_lorenz(initial, t)
plot_lorenz(trajectory)
print("🦋 Lorenz image saved!")
