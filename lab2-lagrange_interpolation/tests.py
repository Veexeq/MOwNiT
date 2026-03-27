import numpy as np
import csv

import utils
import interpolators
import visualizer

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
        f'Lagrange | y = {equation}', f'lagrange_{filename}.png', n,
        subdir='lagrange'
    )
    
    return max_diff_uniform, max_diff_chebyshev, error_2_uniform, error_2_chebyshev

def custom_function_lagrange_handler():
    """
    Handles tests of the assigned function for Lagrange interpolation: 
    - small number of nodes: {3, 4, ..., 9}
    - medium number of nodes: {10, 20, ..., 90}
    - big number of nodes: {100, 200}
    """
    lower_boundary = -3 * np.pi
    upper_boundary =  3 * np.pi
    function = utils.assigned_function
    
    csv_filepath: str = './data/lagrange_custom_function_errors.csv'
    
    # Ensure data directory exists
    import os
    os.makedirs('./data', exist_ok=True)
    
    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['nodes_number', 
                         'max_diff_uniform', 
                         'max_diff_chebyshev', 
                         'error_uniform', 
                         'error_chebyshev'])
        
        # Tworzymy jedną listę wszystkich węzłów do przetestowania
        nodes_to_test = list(range(3, 10)) + list(range(10, 100, 10)) + [100, 200]
        
        for nodes_number in nodes_to_test:
            max_u, max_c, rmse_u, rmse_c = custom_function_lagrange_testing(
                lower_boundary, upper_boundary, nodes_number, function, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
    print(f"\nFinished Lagrange testing. Saved results to path: {csv_filepath}")
    
    visualizer.plot_errors_from_csv(
        csv_filepath=csv_filepath,
        test_name="Analiza Błędów Interpolacji (Lagrange)",
        filename="lagrange_custom_function_errors.png",
        subdir='lagrange'
    )
    
def custom_function_newton_testing(a, b, n, func, equation, filename):
    """
    Testing how precise a given function 'func' behaves, when interpolated
    using the Newton polynomial.
    """
    
    # 1. A dense net for the reference function
    x_dense = np.linspace(a, b, 1000)
    y_true = func(x_dense)

    # 2. Uniform distribution
    x_unif = utils.generate_uniform_nodes(a, b, n)
    y_unif = func(x_unif)
        
    poly_unif_newton = interpolators.newton_formula(x_unif, y_unif)
    y_interp_unif_newton = poly_unif_newton(x_dense)

    # 3. Chebyshev's nodes
    x_cheb = utils.generate_chebyshev_nodes(a, b, n)
    y_cheb = func(x_cheb)
        
    poly_cheb_newton = interpolators.newton_formula(x_cheb, y_cheb)
    y_interp_cheb_newton = poly_cheb_newton(x_dense)

    # 4. Calculate errors between an interpolated polynomial and the reference one
    max_diff_uniform   = np.max(np.abs(y_interp_unif_newton - y_true))
    max_diff_chebyshev = np.max(np.abs(y_interp_cheb_newton - y_true))
    error_2_uniform    = np.sqrt(np.sum((y_interp_unif_newton - y_true) ** 2)) / n
    error_2_chebyshev  = np.sqrt(np.sum((y_interp_cheb_newton - y_true) ** 2)) / n

    # 5. Draw plots
    visualizer.plot_and_save_comparison(
        x_dense, y_true,
        x_unif, y_unif, y_interp_unif_newton, 
        x_cheb, y_cheb, y_interp_cheb_newton,
        f'Newton | y = {equation}', f'newton_{filename}.png', n,
        subdir='newton'
    )
    
    return max_diff_uniform, max_diff_chebyshev, error_2_uniform, error_2_chebyshev


def custom_function_newton_handler():
    """
    Handles tests of the assigned function for Newton interpolation.
    Outputs results to a separate CSV.
    """
    lower_boundary = -3 * np.pi
    upper_boundary =  3 * np.pi
    function = utils.assigned_function
    
    csv_filepath: str = './data/newton_custom_function_errors.csv'
    
    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['nodes_number', 
                         'max_diff_uniform', 
                         'max_diff_chebyshev', 
                         'error_uniform', 
                         'error_chebyshev'])
        
        nodes_to_test = list(range(3, 10)) + list(range(10, 100, 10)) + [100, 200]
        
        for nodes_number in nodes_to_test:
            max_u, max_c, rmse_u, rmse_c = custom_function_newton_testing(
                lower_boundary, upper_boundary, nodes_number, function, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
    print(f"\nFinished Newton testing. Saved results to path: {csv_filepath}")
    
    visualizer.plot_errors_from_csv(
        csv_filepath=csv_filepath,
        test_name="Analiza Błędów Interpolacji (Newton)",
        filename="newton_custom_function_errors.png",
        subdir='newton'
    )
    