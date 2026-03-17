import numpy as np
from numpy.typing import NDArray
from typing import Callable, Union

def lagrange_formula(xs: NDArray[np.float64], ys: NDArray[np.float64]) -> Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]:
    """
    Generates a callable function for evaluating the Lagrange interpolating polynomial.

    This function separates the interpolation process into two steps to improve performance. 
    First, it pre-calculates the constant coefficients (the denominators of the Lagrange 
    basis polynomials combined with the y-values), which depend solely on the input nodes. 
    It then returns a closure that computes only the numerators for any given target 'x', 
    significantly speeding up repeated evaluations (e.g., when plotting).

    Parameters
    ----------
    xs : NDArray[np.float64]
        A 1D array containing the x-coordinates of the interpolation nodes. 
        All values must be distinct.
    ys : NDArray[np.float64]
        A 1D array containing the y-coordinates corresponding to the 'xs' nodes.

    Returns
    -------
    Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]
        An evaluation function that takes a target x-value (scalar or 1D array) 
        and returns the computed interpolated y-value(s).
    """
    
    n: int = len(xs)
    
    # Coefficients, dependant only on the nodes
    C = np.zeros(n, dtype=np.float64)
    
    # Build these `n` coefficients
    for i in range(n):
        diffs = xs[i] - xs
        
        # This would be 0, but we omit (x_j - x_i) if i == j therefore, 
        # we insert a 1, that doesn't affect multiplication
        diffs[i] = 1.0
        C[i] = ys[i] / np.prod(diffs)
    
    # Create a closure, `x` can either be a singular value or an array (for quick calculations using nodes generation)
    def formula(x: Union[float, NDArray[np.float64]]) -> NDArray[np.float64]:
        x_array = np.asarray(x, dtype=np.float64)
        result = np.zeros_like(x_array)
        
        for i in range(n):
            # Calculate the nominator for i-th coefficient
            term = np.ones_like(x_array)
            for j in range(n):
                if i != j:
                    term *= (x_array - xs[j])
                    
            result += C[i] * term
        
        return result

    return formula
