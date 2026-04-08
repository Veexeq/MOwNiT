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
    
    k = np.arange(1, n + 1)
    
    standard_nodes = np.cos((2 * k - 1) / (2 * n) * np.pi)
    
    # Scale nodes to the [a, b] interval
    scaled_nodes = 0.5 * (a + b) + 0.5 * (b - a) * standard_nodes
    
    return scaled_nodes

def assigned_function(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    A function that was assigned to me in the lab-work description:
    f(x) = 10*m + (x ** 2)/k - 10*m*np.cos(k*x), where m = 1 and k = 2.
    Testing interval pointed out in the description: [-3*pi, 3*pi]
    """
    
    m: int = 1
    k: int = 2
    
    return 10*m + (x ** 2)/k - 10*m*np.cos(k*x)

def assigned_function_deriv(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    The first derivative of an assigned function, calculated analytically:
    f(x)  = 10*m + (x^2)/k - 10*m*cos(k*x)
    f'(x) = (2*x)/k + 10*m*k*sin(k*x)
    """
    m: int = 1
    k: int = 2
    
    return (2.0 * x) / k + 10.0 * m * k * np.sin(k * x)
