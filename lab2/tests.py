import numpy as np
import csv

import utils
import interpolators
import visualizer

"""
NA RYSUNKACH MA BYĆ WSZYSTKO PO POLSKU
NA RAZ NASTĘPNY (DO HERMITA) MAMY TYLKO PIERWSZĄ POCHODNĄ, 
WYLICZONĄ ANALITYCZNIE. MOŻEMY SIĘ OGRANICZYĆ TYLKO DO JEDNEGO WZORU.

BŁĄD LICZYMY W PUNKTACH KONTROLNYCH: MOICH 'x_dense'.

LICZBA WĘZŁÓW SENSOWNIE <= 200
"""
def custom_function_lagrange_testing(a, b, n, func, equation, filename):
    """
    Testing how precise a given function 'func' behaves, when interpolated
    using the Lagrange polynomial. This testing doesn't cover using Newton's polynomial.
    """
    
    # 1. A dense net for the reference function
    x_dense = np.linspace(a, b, 1000)
    y_true = func(x_dense)

    # 2. Uniform distribution
    x_unif = utils.generate_uniform_nodes(a, b, n)
    y_unif = func(x_unif)
        
    poly_unif_lagrange = interpolators.lagrange_formula(x_unif, y_unif)
    y_interp_unif_lagrange = poly_unif_lagrange(x_dense)

    # 3. Chebyshev's nodes
    x_cheb = utils.generate_chebyshev_nodes(a, b, n)
    y_cheb = func(x_cheb)
        
    poly_cheb_lagrange = interpolators.lagrange_formula(x_cheb, y_cheb)
    y_interp_cheb_lagrange = poly_cheb_lagrange(x_dense)

    # 4. Calculate errors between an interpolated polynomial and the reference one
    max_diff_uniform   = np.max(np.abs(y_interp_unif_lagrange - y_true))
    max_diff_chebyshev = np.max(np.abs(y_interp_cheb_lagrange - y_true))
    error_2_uniform    = np.sqrt(np.sum((y_interp_unif_lagrange - y_true) ** 2)) / n
    error_2_chebyshev  = np.sqrt(np.sum((y_interp_cheb_lagrange - y_true) ** 2)) / n

    # 5. Draw plots
    visualizer.plot_and_save_comparison(
        x_dense, y_true,
        x_unif, y_unif, y_interp_unif_lagrange, 
        x_cheb, y_cheb, y_interp_cheb_lagrange,
        f'Lagrange | {equation}', f'lagrange_{filename}.png', n
    )
    
    return max_diff_uniform, max_diff_chebyshev, error_2_uniform, error_2_chebyshev

def custom_function_handler():
    """
    Handles tests of the assigned function: 
    Tests for:
    - small number of nodes: {3, 4, ..., 9}
    - medium number of nodes: {10, 20, ..., 90}
    - big number of nodes: {100, 200, 300, 400}
    """
    lower_boundary = -3 * np.pi
    upper_boundary =  3 * np.pi
    function = utils.assigned_function
    
    csv_filepath: str = './data/custom_function_errors.csv'
    
    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['nodes_number', 
                         'max_diff_uniform', 
                         'max_diff_chebyshev', 
                         'error_uniform', 
                         'error_chebyshev'])
        
        # Small nodes number:
        for nodes_number in range(3, 10):
            max_u, max_c, rmse_u, rmse_c = custom_function_lagrange_testing(
                lower_boundary, upper_boundary, nodes_number, function, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
        
        # # Medium nodes number:
        for nodes_number in range(10, 100, 10):
            max_u, max_c, rmse_u, rmse_c = custom_function_lagrange_testing(
                lower_boundary, upper_boundary, nodes_number, function, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
        # Big nodes number:
        for nodes_number in range(100, 500, 100):
            max_u, max_c, rmse_u, rmse_c = custom_function_lagrange_testing(
                lower_boundary, upper_boundary, nodes_number, function, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
    print(f"\nFinished testing. Saved results to path: {csv_filepath}")
    
    # Draw the error plot from .csv file.
    visualizer.plot_errors_from_csv(
        csv_filepath=csv_filepath,
        test_name="Analiza Błędów Interpolacji",
        filename="lagrange_custom_function_errors.png"
    )

def custom_function_hermite_testing(a, b, n, func, func_deriv, equation, filename):
    """
    Tests the accuracy of interpolating a given function 'func' using the Hermite polynomial.
    Requires providing a function 'func_deriv' that computes the analytical first derivative.
    """
    
    # 1. Dense grid for the reference function
    x_dense = np.linspace(a, b, 1000)
    y_true = func(x_dense)

    # 2. Uniform nodes
    x_unif = utils.generate_uniform_nodes(a, b, n)
    y_unif = func(x_unif)
    dy_unif = func_deriv(x_unif) # Note: we obtain derivatives
        
    poly_unif_hermite = interpolators.hermite_formula(x_unif, y_unif, dy_unif)
    y_interp_unif_hermite = poly_unif_hermite(x_dense)

    # 3. Chebyshev nodes
    x_cheb = utils.generate_chebyshev_nodes(a, b, n)
    y_cheb = func(x_cheb)
    dy_cheb = func_deriv(x_cheb) # Note: we obtain derivatives
        
    poly_cheb_hermite = interpolators.hermite_formula(x_cheb, y_cheb, dy_cheb)
    y_interp_cheb_hermite = poly_cheb_hermite(x_dense)

    # 4. Error calculations
    max_diff_uniform   = np.max(np.abs(y_interp_unif_hermite - y_true))
    max_diff_chebyshev = np.max(np.abs(y_interp_cheb_hermite - y_true))
    error_2_uniform    = np.sqrt(np.sum((y_interp_unif_hermite - y_true) ** 2)) / n
    error_2_chebyshev  = np.sqrt(np.sum((y_interp_cheb_hermite - y_true) ** 2)) / n

    # 5. Plot comparison graphs (we use the same function from visualizer.py!)
    visualizer.plot_and_save_comparison(
        x_dense, y_true,
        x_unif, y_unif, y_interp_unif_hermite, 
        x_cheb, y_cheb, y_interp_cheb_hermite,
        f'Hermite | {equation}', f'hermite_{filename}.png', n
    )
    
    return max_diff_uniform, max_diff_chebyshev, error_2_uniform, error_2_chebyshev

def custom_function_hermite_handler():
    """
    Manages tests for Hermite interpolation and saves the results to a dedicated CSV file.
    """
    lower_boundary = -3 * np.pi
    upper_boundary =  3 * np.pi
    
    # We attach our function and its derivative from utils.py
    function = utils.assigned_function
    function_deriv = utils.assigned_function_deriv 
    
    csv_filepath: str = './data/hermite_custom_function_errors.csv'
    
    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['nodes_number', 
                         'max_diff_uniform', 
                         'max_diff_chebyshev', 
                         'error_uniform', 
                         'error_chebyshev'])
        
        # Prepare a list of node counts to test
        nodes_to_test = list(range(3, 10)) + list(range(10, 100, 10)) + list(range(100, 500, 100))
        
        for nodes_number in nodes_to_test:
            # Note passing 'function_deriv' to the new testing function
            max_u, max_c, rmse_u, rmse_c = custom_function_hermite_testing(
                lower_boundary, upper_boundary, nodes_number, 
                function, function_deriv, 
                '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
    print(f"\nFinished Hermite testing. Saved results to path: {csv_filepath}")
    
    # Plot aggregate error graph from the new file
    visualizer.plot_errors_from_csv(
        csv_filepath=csv_filepath,
        test_name="Error Analysis of Interpolation (Hermite)",
        filename="hermite_custom_function_errors.png"
    )

def run_all_tests():
    n = 15 

    test_cases = [
        (utils.runge_function, "Funkcja Rungego", "runge.png", -1.0, 1.0),
        (utils.sine_function, "Sinusoida", "sinus.png", -np.pi, np.pi),
        (utils.absolute_function, "Wartość Bezwzględna", "abs.png", -1.0, 1.0)
    ]

    print(f"Generating plots (N = {n})...")

    for func, name, filename, a, b in test_cases:
        # 1. A dense net for the reference function
        x_dense = np.linspace(a, b, 1000)
        y_true = func(x_dense)

        # 2. Uniform distribution
        x_unif = utils.generate_uniform_nodes(a, b, n)
        y_unif = func(x_unif)
        
        poly_unif_lagrange = interpolators.lagrange_formula(x_unif, y_unif)
        poly_unif_newton   = interpolators.newton_formula(x_unif, y_unif)
        y_interp_unif_lagrange = poly_unif_lagrange(x_dense)
        y_interp_unif_newton   = poly_unif_newton(x_dense)

        # 3. Chebyshev's nodes
        x_cheb = utils.generate_chebyshev_nodes(a, b, n)
        y_cheb = func(x_cheb)
        
        poly_cheb_lagrange = interpolators.lagrange_formula(x_cheb, y_cheb)
        poly_cheb_newton   = interpolators.newton_formula(x_cheb, y_cheb)
        y_interp_cheb_lagrange = poly_cheb_lagrange(x_dense)
        y_interp_cheb_newton   = poly_cheb_newton(x_dense)

        # 4. Draw plots
        visualizer.plot_and_save_comparison(
            x_dense, y_true,
            x_unif, y_unif, y_interp_unif_lagrange, 
            x_cheb, y_cheb, y_interp_cheb_lagrange,
            f'Lagrange | {name}', f'lagrange_{filename}.png', n
        )
        visualizer.plot_and_save_comparison(
            x_dense, y_true,
            x_unif, y_unif, y_interp_unif_newton, 
            x_cheb, y_cheb, y_interp_cheb_newton,
            f'Newton | {name}', f'newton_{filename}.png', n
        )
        
    print('Finished. Check ./plots/ directory.')
