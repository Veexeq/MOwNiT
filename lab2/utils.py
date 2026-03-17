import numpy as np
from numpy.typing import NDArray

def generate_uniform_nodes(a: float, b: float, n: int) -> NDArray[np.float64]:
    """
    Generates a numpy's n-dimensional vector of nodes that are 
    equidistantly placed within the interval [a, b] (inclusive). 
    """
    
    return np.linspace(a, b, n)
    
def generate_chebyshev_nodes(a: float, b: float, n: int) -> NDArray[np.float64]:
    """
    Generates a numpy's n-dimensional vector of Chebyshev nodes 
    that are placed within the interval [a, b] (inclusive).
    Those nodes minimalize Runge's effect at the boundaries of the interval.  
    """
    
    # Generate [1, 2, 3, ..., n]
    k = np.arange(1, n + 1)
    
    # Generate nodes within the standard [-1, 1] interval
    standard_nodes = np.cos((2 * k - 1) / (2 * n) * np.pi)
    
    # Scale those nodes to the [a, b] interval
    scaled_nodes = 0.5 * (a + b) + 0.5 * (b - a) * standard_nodes
    
    return scaled_nodes
    