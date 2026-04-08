import numpy as np
import csv
import os

import utils
import interpolators
import visualizer


def custom_function_hermite_testing(a, b, n, func, deriv_func, equation, filename):
    """
    Testing how precise a given function 'func' behaves, when interpolated
    using the Hermite polynomial. Requires the first derivative 'deriv_func'.
    """
    
    # 1. A dense net for the reference function
    x_dense = np.linspace(a, b, 1000)
    y_true = func(x_dense)

    # 2. Uniform distribution
    x_unif = utils.generate_uniform_nodes(a, b, n)
    y_unif = func(x_unif)
    dy_unif = deriv_func(x_unif) # Obliczamy pochodne
        
    poly_unif_hermite = interpolators.hermite_formula(x_unif, y_unif, dy_unif)
    y_interp_unif_hermite = poly_unif_hermite(x_dense)

    # 3. Chebyshev's nodes
    x_cheb = utils.generate_chebyshev_nodes(a, b, n)
    y_cheb = func(x_cheb)
    dy_cheb = deriv_func(x_cheb)
        
    poly_cheb_hermite = interpolators.hermite_formula(x_cheb, y_cheb, dy_cheb)
    y_interp_cheb_hermite = poly_cheb_hermite(x_dense)

    # 4. Calculate errors between an interpolated polynomial and the reference one
    max_diff_uniform   = np.max(np.abs(y_interp_unif_hermite - y_true))
    max_diff_chebyshev = np.max(np.abs(y_interp_cheb_hermite - y_true))
    error_2_uniform    = np.sqrt(np.sum((y_interp_unif_hermite - y_true) ** 2)) / n
    error_2_chebyshev  = np.sqrt(np.sum((y_interp_cheb_hermite - y_true) ** 2)) / n

    # 5. Draw plots
    visualizer.plot_and_save_comparison(
        x_dense, y_true,
        x_unif, y_unif, y_interp_unif_hermite, 
        x_cheb, y_cheb, y_interp_cheb_hermite,
        f'Hermite | y = {equation}', f'hermite_{filename}.png', n,
        subdir='hermite'
    )
    
    return max_diff_uniform, max_diff_chebyshev, error_2_uniform, error_2_chebyshev


def custom_function_hermite_handler():
    """
    Handles tests of the assigned function for Hermite interpolation.
    Outputs results to a separate CSV.
    """
    lower_boundary = -3 * np.pi
    upper_boundary =  3 * np.pi
    
    function = utils.assigned_function
    deriv_function = utils.assigned_function_deriv
    
    csv_filepath: str = './data/hermite_custom_function_errors.csv'
    os.makedirs('./data', exist_ok=True)
    
    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['nodes_number', 
                         'max_diff_uniform', 
                         'max_diff_chebyshev', 
                         'error_uniform', 
                         'error_chebyshev'])
        
        nodes_to_test = list(range(3, 10)) + list(range(10, 100, 10)) + [100, 200]
        
        for nodes_number in nodes_to_test:
            max_u, max_c, rmse_u, rmse_c = custom_function_hermite_testing(
                lower_boundary, upper_boundary, nodes_number, function, deriv_function, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
    print(f"\nFinished Hermite testing. Saved results to path: {csv_filepath}")
    
    visualizer.plot_errors_from_csv(
        csv_filepath=csv_filepath,
        test_name="Analiza Błędów Interpolacji (Hermite)",
        filename="hermite_custom_function_errors.png",
        subdir='hermite'
    )
