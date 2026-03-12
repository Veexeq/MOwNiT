import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import precise_sequence_gen as psg

BASE_DIR    = Path(__file__).resolve().parent.parent
GCC_SOURCE  = BASE_DIR / 'output'   / 'gcc_results.csv'
GCC_DEST    = BASE_DIR / 'analysis' / 'graphs' / 'gcc'
MSVC_SOURCE = BASE_DIR / 'output'   / 'msvc_results.csv'
MSVC_DEST   = BASE_DIR / 'analysis' / 'graphs' / 'msvc'

GCC_PRECISIONS = ['0.100000000000000000001',
              '0.100000099999999999997',
              '0.100000000000000099999']
MSVC_PRECISIONS = ['0.100000000000000005551',
                   '0.100000099999999994549',
                   '0.100000000000000102696']

VARIANTS = ['basic', 'alt']

def create_plot(data, compiler, precision, variant):
    # Filter data
    data = data[(data['x0'] == precision) & 
                (data['variant'] == variant)]
    
    # Generate precise sequence
    K_MAX = 100
    ref_data = psg.get_reference_sequence(precision, K_MAX)

    # Draw the plot
    plt.figure(figsize=(10, 6))
    plt.plot(data['k'], data['float_val'],       label='Float',       marker='o', markersize=2, linestyle='-')
    plt.plot(data['k'], data['double_val'],      label='Double',      marker='s', markersize=2, linestyle='--')
    plt.plot(data['k'], data['long_double_val'], label='Long Double', marker='^', markersize=2, linestyle=':')
    
    # Draw the reference
    ref_k = list(range(K_MAX + 1))
    plt.plot(ref_k, ref_data, label='Reference (mpmath 100 dps)', color='black', linestyle='-', linewidth=2, zorder=0)
    
    # Label the plot
    formula = f'$x_{{k+1}} = x_k + 3x_k(1 - x_k), x_0 = {precision}$' if variant == 'basic' else f'$x_{{k+1}} = 4x_k - 3x_k^2, x_0 = {precision}$'
    
    plt.xlabel('Iteracja (k)')
    plt.ylabel('$x_k$')
    plt.title(f'Wykres ciągu {formula} ({compiler})')
    
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
    plt.grid(True, linestyle='--', alpha=0.5)
    
    filename = f'plot_{variant}_{compiler}_{precision}.png'
    dest_dir = GCC_DEST if compiler == 'GCC' else MSVC_DEST
    plt.savefig(dest_dir / filename, dpi=300, bbox_inches='tight')
    
    plt.close()
    
def generate_all_plots():
    # 'x0' column must remain a string, because of its high precision
    df_gcc = pd.read_csv(GCC_SOURCE,   dtype={'x0': str})
    df_msvc = pd.read_csv(MSVC_SOURCE, dtype={'x0': str})
    
    # GCC-related plots
    for precision in GCC_PRECISIONS:
        for variant in VARIANTS:
            create_plot(df_gcc, 'GCC', precision, variant)

    # MSVC-related plots
    for precision in MSVC_PRECISIONS:
        for variant in VARIANTS:
            create_plot(df_msvc, 'MSVC', precision, variant)

if __name__ == '__main__':
    generate_all_plots()
