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
    
def runge_function(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Runge's function: f(x) = 1 / (1 + 25x^2).
    Demonstrates the Runge's phenomenon, where the interpolating function oscilates wildly
    at the boundaries of the interval.
    Recommended test interval: [-1, 1] 
    """
    return 1.0 / (1.0 + 25.0 * x**2)

def sine_function(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    A smooth function: f(x) = sin(x).
    Great for showcasing that the interpolation works well on smooth functions.
    Recommended test interval: [-np.pi, np.pi] 
    """
    return np.sin(x)

def absolute_function(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    A function with a "sharp" kink: f(x) = |x|
    Interesting example, because it's not differentiable at x = 0.
    Interpolating a "sharp" function with polynomials that are inherently
    smooth often leads to notable issues and significant errors near 0.
    Recommended test interval: [-1, 1] 
    """
    return np.abs(x)

def assigned_function(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    A function that was assigned to me in the lab-work description:
    f(x) = 10*m + (x ** 2)/k - 10*m*np.cos(k*x), where m = 1 and k = 2.
    Testing interval pointed out in the description: [-3*pi, 3*pi]
    """
    
    m: int = 1
    k: int = 2
    
    return 10*m + (x ** 2)/k - 10*m*np.cos(k*x)
