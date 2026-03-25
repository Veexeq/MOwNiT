import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent / 'plots'
CUSTOM_FUNCTION_OUTPUT_PATH = OUTPUT_PATH / 'custom_function'

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
    CUSTOM_FUNCTION_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    plt.tight_layout()
    plt.savefig(CUSTOM_FUNCTION_OUTPUT_PATH / filename, dpi=150)
    plt.close()
    print(f"Saved plot: {filename}")

def plot_and_save_errors(
    nodes_number: NDArray[np.float64], 
    max_diff_uniform: NDArray[np.float64], 
    max_diff_chebyshev: NDArray[np.float64], 
    error_uniform: NDArray[np.float64], 
    error_chebyshev: NDArray[np.float64], 
    test_name: str, 
    filename: str
) -> None:
    """
    Draw a plot of errors of the interpolation process in a logarithmic scale.
    """
    plt.figure(figsize=(14, 6))

    # --- Plot 1: Max diff ---
    plt.subplot(1, 2, 1)
    plt.plot(nodes_number, max_diff_uniform, 'r-o', label='Węzły Równomierne')
    plt.plot(nodes_number, max_diff_chebyshev, 'b-s', label='Węzły Czebyszewa')
    plt.yscale('log') 
    
    plt.title(f'{test_name} - Błąd maksymalny')
    plt.xlabel('Liczba węzłów (N)')
    plt.ylabel('Błąd (skala logarytmiczna)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.grid(True, which='minor', linestyle=':', alpha=0.4) 

    # --- Plot 2: Custom error given by a formula ---
    plt.subplot(1, 2, 2)
    plt.plot(nodes_number, error_uniform, 'r-o', label='Węzły Równomierne')
    plt.plot(nodes_number, error_chebyshev, 'b-s', label='Węzły Czebyszewa')
    plt.yscale('log')
    
    plt.title(f'{test_name} - Błąd zadany wzorem')
    plt.xlabel('Liczba węzłów (N)')
    plt.ylabel('Błąd (skala logarytmiczna)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.grid(True, which='minor', linestyle=':', alpha=0.4)

    # Save and cleanup
    CUSTOM_FUNCTION_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    plt.tight_layout()
    plt.savefig(CUSTOM_FUNCTION_OUTPUT_PATH / filename, dpi=150)
    plt.close()
    print(f"Saved error plot: {filename}")


def plot_errors_from_csv(csv_filepath: str, test_name: str, filename: str) -> None:
    """
    Generates an error plot from a .csv file.
    """
    data = np.loadtxt(csv_filepath, delimiter=',', skiprows=1)
    
    nodes_number       = data[:, 0]
    max_diff_uniform   = data[:, 1]
    max_diff_chebyshev = data[:, 2]
    error_uniform      = data[:, 3]
    error_chebyshev    = data[:, 4]

    plot_and_save_errors(
        nodes_number, max_diff_uniform, max_diff_chebyshev, 
        error_uniform, error_chebyshev, test_name, filename
    )
