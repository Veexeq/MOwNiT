import numpy as np

import utils
import interpolators
import visualizer

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
