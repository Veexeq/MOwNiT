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
def manual_tests(a, b, n, func, equation, filename):
    
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

    # 4. Calculate errors between an interpolated polynomial and the reference one
    max_diff_uniform   = np.max(np.abs(y_interp_unif_lagrange - y_true))
    max_diff_chebyshev = np.max(np.abs(y_interp_cheb_lagrange - y_true))
    error_2_uniform   = np.sqrt(np.mean((y_interp_unif_lagrange - y_true) ** 2))
    error_2_chebyshev = np.sqrt(np.mean((y_interp_cheb_lagrange - y_true) ** 2))
    
    print(f'Maks. odchyłka (jednostajny vs ref): {max_diff_uniform}')
    print(f'Maks. odchyłka (Czebyszew vs ref): {max_diff_chebyshev}')
    print(f'Błąd RMSE (jednostajny vs ref): {error_2_uniform}')
    print(f'Błąd RMSE (Czebyszew vs ref): {error_2_chebyshev}')

    # 5. Draw plots
    visualizer.plot_and_save_comparison(
        x_dense, y_true,
        x_unif, y_unif, y_interp_unif_lagrange, 
        x_cheb, y_cheb, y_interp_cheb_lagrange,
        f'Lagrange | {equation}', f'lagrange_{filename}.png', n
    )
    # visualizer.plot_and_save_comparison(
    #     x_dense, y_true,
    #     x_unif, y_unif, y_interp_unif_newton, 
    #     x_cheb, y_cheb, y_interp_cheb_newton,
    #     f'Newton | {equation}', f'newton_{filename}.png', n
    # )
    
    return max_diff_uniform, max_diff_chebyshev, error_2_uniform, error_2_chebyshev

def manual_tests_handler():
    """
    Handles tests of the assigned function: 
    f(x) = 10*m + x^2/k - 10*m*cos(kx) (passed as a lambda).
    Tests for number of nodes between 3 and ...?
    """
    lower_boundary = -3 * np.pi
    upper_boundary =  3 * np.pi
    m = 1
    k = 2
    f = lambda x: 10*m + (x ** 2)/k - 10*m*np.cos(k*x)
    
    csv_filename = 'bledy_interpolacji.csv'
    
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Liczba węzłów (N)', 'Max Odchyłka (Jednostajny)', 'Max Odchyłka (Czebyszew)', 'RMSE (Jednostajny)', 'RMSE (Czebyszew)'])
        
        # Small nodes number:
        # for nodes_number in range(3, 20):
        #     max_u, max_c, rmse_u, rmse_c = manual_tests(
        #         lower_boundary, upper_boundary, nodes_number, f, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
        #     )
            
        #     writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
        
        # # Medium nodes number:
        # for nodes_number in range(20, 100, 10):
        #     max_u, max_c, rmse_u, rmse_c = manual_tests(
        #         lower_boundary, upper_boundary, nodes_number, f, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
        #     )
            
        #     writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
        # Big nodes number:
        for nodes_number in range(100, 1000, 100):
            max_u, max_c, rmse_u, rmse_c = manual_tests(
                lower_boundary, upper_boundary, nodes_number, f, '10 + x^2/2 - 10*cos(2x)', f'custom_function_{nodes_number}'
            )
            
            writer.writerow([nodes_number, max_u, max_c, rmse_u, rmse_c])
            
    print(f"\nZakończono testy. Zapisano wyniki do pliku: {csv_filename}")
            

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
