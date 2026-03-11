import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRECISE_DELTA_SOURCE = BASE_DIR / 'analysis' / 'precise_deltas' / 'precise_deltas.csv'
GCC_SOURCE = BASE_DIR / 'output' / 'gcc_results.csv'
MSVC_SOURCE = BASE_DIR / 'output' / 'msvc_results.csv'
PLOTS_DEST = BASE_DIR / 'analysis' / 'graphs'

def plot_errors(compiler, x0, variant):
    df_main = pd.read_csv(GCC_SOURCE if compiler == 'GCC' else MSVC_SOURCE, dtype={'x0': str})
    df_precise = pd.read_csv(PRECISE_DELTA_SOURCE, dtype={'x0': str})

    mask_m = (df_main['x0'] == x0) & (df_main['variant'] == variant)
    mask_p = (df_precise['x0'] == x0) & (df_precise['variant'] == variant) & (df_precise['compiler'] == compiler)
    
    d_m = df_main[mask_m].sort_values('k')
    d_p = df_precise[mask_p].sort_values('k')
    
    if d_m.empty or d_p.empty:
        print(f"Lack of data for: {compiler}, {x0}")
        return
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(d_m['k'], d_m['delta_fd'], label='Błąd: Float - Double', color='red', alpha=0.7)
    plt.plot(d_m['k'], d_m['delta_dl'], label='Błąd: Double - Long Double', color='blue', alpha=0.7)
    plt.plot(d_p['k'], d_p['precise_delta'], label='Błąd: Long Double - Reference', color='black', linewidth=2)
    
    plt.yscale('log')
    
    plt.xlabel('k')
    plt.ylabel('$|x_k - x_k\'|$ (log scale)')
    plt.title(f'Analiza błędów precyzji ({compiler}, $x_0={x0}$, {variant})')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    
    PLOTS_DEST.mkdir(parents=True, exist_ok=True)
    plt.savefig(PLOTS_DEST / compiler.lower() / f'errors_{compiler}_{variant}_{x0}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
if __name__ == '__main__':
    plot_errors('GCC', '0.100000000000000000001', 'basic')