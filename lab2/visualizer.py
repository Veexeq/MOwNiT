import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent / 'plots'

def plot_and_save_comparison(
    x_dense: NDArray[np.float64], y_true: NDArray[np.float64],
    x_unif: NDArray[np.float64], y_unif: NDArray[np.float64], y_interp_unif: NDArray[np.float64],
    x_cheb: NDArray[np.float64], y_cheb: NDArray[np.float64], y_interp_cheb: NDArray[np.float64],
    test_name: str, filename: str, n_nodes: int
) -> None:
    """
    Generates and saves to a file a plot that compares the interpolation 
    and a real function (given (x,y) points of both) for both equidistant and Chebyshev nodes.
    """
    plt.figure(figsize=(14, 6))

    y_min, y_max = np.min(y_true), np.max(y_true)
    margin = (y_max - y_min) * 0.2
    y_limits = (y_min - margin, y_max + margin)

    # --- Plot 1: Equidistant nodes ---
    plt.subplot(1, 2, 1)
    plt.plot(x_dense, y_true, 'k--', label='Referencja')
    plt.plot(x_dense, y_interp_unif, 'r-', label="Interpolacja")
    plt.scatter(x_unif, y_unif, color='red', zorder=5, label='Węzły')
    
    plt.title(f'{test_name} - Węzły Równomierne (N = {n_nodes})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(y_limits)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)

    # --- Plot 2: Chebyshev's nodes ---
    plt.subplot(1, 2, 2)
    plt.plot(x_dense, y_true, 'k--', label='Referencja')
    plt.plot(x_dense, y_interp_cheb, 'b-', label="Interpolacja")
    plt.scatter(x_cheb, y_cheb, color='blue', zorder=5, label='Węzły')
    
    plt.title(f'{test_name} - Węzły Czebyszewa (N = {n_nodes})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(y_limits)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)

    # Save and cleanup
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH / filename, dpi=150)
    plt.close()
    print(f"Zapisano wykres: {filename}")
    