import numpy as np
from numpy.typing import NDArray
from typing import Callable, Union

def hermite_formula(xs: NDArray[np.float64], 
                    ys: NDArray[np.float64],
                    dys: NDArray[np.float64]
) -> Callable[[Union[float, NDArray[np.float64]]], NDArray[np.float64]]:
    """
    Generates a callable function for evaluating the Hermite interpolating polynomial.
    """
    n = len(xs)
    # Hermite doubles the number of effective nodes
    z = np.zeros(2 * n, dtype=np.float64)
    coef = np.zeros(2 * n, dtype=np.float64)
    
    # 1. Setup double nodes (z) and 0-th divided differences
    for i in range(n):
        z[2*i] = xs[i]
        z[2*i + 1] = xs[i]
        coef[2*i] = ys[i]
        coef[2*i + 1] = ys[i]
        
    # 2. Calculate 1st divided differences (injecting derivatives)
    for i in range(2 * n - 1, 0, -1):
        if z[i] == z[i - 1]:
            # If nodes are the same, the divided difference is the derivative
            coef[i] = dys[i // 2]
        else:
            # Standard divided difference
            coef[i] = (coef[i] - coef[i - 1]) / (z[i] - z[i - 1])
            
    # 3. Calculate higher order divided differences (j >= 2)
    for j in range(2, 2 * n):
        for i in range(2 * n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (z[i] - z[i - j])
            
    # 4. Evaluation closure using Horner's scheme on the 'z' array
    def formula(x: Union[float, NDArray[np.float64]]) -> NDArray[np.float64]:
        x_array = np.asarray(x, dtype=np.float64)
        result = np.full_like(x_array, coef[-1], dtype=np.float64)
        
        for i in range(2 * n - 2, -1, -1):
            result = coef[i] + (x_array - z[i]) * result
            
        return result
        
    return formula
