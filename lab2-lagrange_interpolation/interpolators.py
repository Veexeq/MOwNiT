import numpy as np
from numpy.typing import NDArray
from typing import Callable, Union

def lagrange_formula(xs: NDArray[np.float64], 
                     ys: NDArray[np.float64]
) -> Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]:
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

def newton_formula(xs: NDArray[np.float64], 
                   ys: NDArray[np.float64]
) -> Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]:
    """
    Generates an optimized callable function for evaluating the Newton interpolating polynomial.

    Calculates the divided differences in-place to save memory, 
    and returns a closure that evaluates the polynomial using Horner's method 
    for maximum performance and numerical stability.

    Parameters
    ----------
    xs : NDArray[np.float64]
        A 1D array of x-coordinates (nodes).
    ys : NDArray[np.float64]
        A 1D array of y-coordinates.

    Returns
    -------
    Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]
        Function to evaluate the polynomial at given x-value(s).
    """
    n = len(xs)
    
    # Memory-optimized DP algorithm: use previous coefficients to build up the new ones
    coef = np.copy(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    
    def formula(x: Union[float, NDArray[np.float64]]) -> NDArray[np.float64]:
        x_array = np.asarray(x, dtype=np.float64)
        result = np.full_like(x_array, coef[-1], dtype=np.float64)
        
        # Horner's scheme
        for i in range(n - 2, -1, -1):
            result = coef[i] + (x_array - xs[i]) * result
        
        return result
    
    return formula

def hermite_formula(xs: NDArray[np.float64], 
                    ys: NDArray[np.float64],
                    dys: NDArray[np.float64]
) -> Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]:
    """
    Generates an optimized function to compute values of the Hermite interpolating polynomial.
    Requires providing function values and its first derivative at the nodes.

    Parameters
    ----------
    xs : NDArray[np.float64]
        One-dimensional array of x-coordinates (nodes).
    ys : NDArray[np.float64]
        One-dimensional array of function values at the nodes.
    dys : NDArray[np.float64]
        One-dimensional array of first derivative values at the nodes.

    Returns
    -------
    Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]
        A function evaluating the polynomial at given point(s) x.
    """
    n = len(xs)
    m = 2 * n 
    
    # Step 1: Duplicate nodes (we create the Z array)
    z = np.zeros(m, dtype=np.float64)
    z[0::2] = xs  # Even indices: 0, 2, 4...
    z[1::2] = xs  # Odd indices: 1, 3, 5...
    
    # Step 2: Initialize the coefficient array (function values)
    coef = np.zeros(m, dtype=np.float64)
    coef[0::2] = ys
    coef[1::2] = ys
    
    # Step 3: First-order divided differences (here we inject analytical derivatives)
    for i in range(m - 1, 0, -1):
        if i % 2 == 1:
            # Difference between identical nodes -> insert first derivative
            # Derivative index is obtained via integer division i // 2
            coef[i] = dys[i // 2]
        else:
            # Difference between different nodes -> standard formula
            coef[i] = (coef[i] - coef[i - 1]) / (z[i] - z[i - 1])
            
    # Step 4: Higher-order divided differences (standard Newton algorithm on array Z)
    for j in range(2, m):
        for i in range(m - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (z[i] - z[i - j])
            
    # Closure - evaluation using optimized Horner scheme
    def formula(x: Union[float, NDArray[np.float64]]) -> NDArray[np.float64]:
        x_array = np.asarray(x, dtype=np.float64)
        result = np.full_like(x_array, coef[-1], dtype=np.float64)
        
        for i in range(m - 2, -1, -1):
            result = coef[i] + (x_array - z[i]) * result
            
        return result
        
    return formula
