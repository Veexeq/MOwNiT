import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GCC_SOURCE  = BASE_DIR / 'output' / 'gcc_results.csv'
MSVC_SOURCE = BASE_DIR / 'output' / 'msvc_results.csv'
PLOTS_DEST  = BASE_DIR / 'analysis' / 'graphs' / 'compiler_comp'

GCC_PRECISIONS = ['0.100000000000000000001', '0.100000099999999999997', '0.100000000000000099999']
MSVC_PRECISIONS = ['0.100000000000000005551', '0.100000099999999994549', '0.100000000000000102696']

def plot_compiler_comparison(x0_idx, variant, precision_type):
    precision_map = {
        'float_val': 'Float',
        'double_val': 'Double',
        'long_double_val': 'Long Double'
    }
    
    x0_gcc = GCC_PRECISIONS[x0_idx]
    x0_msvc = MSVC_PRECISIONS[x0_idx]

    df_gcc = pd.read_csv(GCC_SOURCE, dtype={'x0': str})
    df_msvc = pd.read_csv(MSVC_SOURCE, dtype={'x0': str})

    d_gcc = df_gcc[(df_gcc['x0'] == x0_gcc) & (df_gcc['variant'] == variant)].sort_values('k')
    d_msvc = df_msvc[(df_msvc['x0'] == x0_msvc) & (df_msvc['variant'] == variant)].sort_values('k')

    if d_gcc.empty or d_msvc.empty:
        print(f"Lack of data for precision-idx: {x0_idx}, variant: {variant}")
        return

    plt.figure(figsize=(11, 6))

    plt.plot(d_gcc['k'], d_gcc[precision_type], label=f'GCC ({precision_type})', 
             color='blue', marker='o', markersize=3, alpha=0.8)
    
    plt.plot(d_msvc['k'], d_msvc[precision_type], label=f'MSVC ({precision_type})', 
             color='red', marker='x', markersize=3, alpha=0.8)
    
    plt.xlabel('Iteracja (k)')
    plt.ylabel('$x_k$')
    plt.title(f'Porównanie Kompilatorów: {precision_map[precision_type]}\n(Wariant: {variant}, $x_0 = 0.1$)')
    plt.grid(True, alpha=0.3)
    plt.legend()

    PLOTS_DEST.mkdir(parents=True, exist_ok=True)
    filename = f'comp_{precision_type}_{variant}_idx{x0_idx}.png'
    plt.savefig(PLOTS_DEST / filename, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    plot_compiler_comparison(0, 'basic', 'float_val')
    plot_compiler_comparison(0, 'basic', 'double_val')
    plot_compiler_comparison(0, 'basic', 'long_double_val')
    