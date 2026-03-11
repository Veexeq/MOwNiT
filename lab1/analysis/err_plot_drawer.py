import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import precise_sequence_gen as psg

BASE_DIR = Path(__file__).resolve().parent.parent
PRECISE_DELTA_SOURCE = BASE_DIR / 'analysis' / 'precise_deltas' / 'precise_deltas.csv'
GCC_SOURCE = BASE_DIR / 'output' / 'gcc_results.csv'
MSVC_SOURCE = BASE_DIR / 'output' / 'msvc_results.csv'
PLOTS_DEST = BASE_DIR / 'analysis' / 'graphs'

def get_errors_df(compiler, x0, variant):
    df = pd.read_csv(GCC_SOURCE if compiler == 'GCC' else MSVC_SOURCE, dtype={'x0': str})
    df = df[(df['x0'] == x0) & (df['variant'] == variant)].sort_values('k')
    
    if df.empty:
        return None

    k_max = df['k'].max()
    ref_values = psg.get_reference_sequence(x0, k_max)
    
    df['ref_val'] = ref_values
    
    df['err_f']  = (df['float_val'] - df['ref_val']).abs()
    df['err_d']  = (df['double_val'] - df['ref_val']).abs()
    df['err_ld'] = (df['long_double_val'] - df['ref_val']).abs()
    
    return df

def plot_errors(compiler, x0, variant):
    df = get_errors_df(compiler, x0, variant)
    
    if df is None:
        print(f"Lack of data for: {compiler}, {x0}, {variant}")
        return
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(df['k'], df['err_f'],  label='Błąd: Float vs Ref',  color='red', alpha=0.7)
    plt.plot(df['k'], df['err_d'],  label='Błąd: Double vs Ref', color='blue', alpha=0.7)
    plt.plot(df['k'], df['err_ld'], label='Błąd: Long Double vs Ref', color='black', linewidth=2)
    
    plt.yscale('log')
    plt.xlabel('Iteracja (k)')
    plt.ylabel('Błąd bezwzględny $|x_k - x_{ref}|$ (log scale)')
    plt.title(f'Błędy względem referencji ({compiler}, $x_0={x0}$, {variant})')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    
    save_path = PLOTS_DEST / compiler.lower()
    save_path.mkdir(parents=True, exist_ok=True)
    plt.savefig(save_path / f'ref_errors_{compiler}_{variant}_{x0}.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_variant_errors(compiler, x0, delta_type):
    mapping = {
        'f':  {'col': 'err_f',  'label': 'Float vs Ref'},
        'd':  {'col': 'err_d',  'label': 'Double vs Ref'},
        'ld': {'col': 'err_ld', 'label': 'Long Double vs Ref'}
    }
    
    cfg = mapping[delta_type]
    
    df_basic = get_errors_df(compiler, x0, 'basic')
    df_alt   = get_errors_df(compiler, x0, 'alt')
    
    if df_basic is None or df_alt is None:
        print(f"Lack of data for variant comparison: {compiler}, {x0}, {delta_type}")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_basic['k'], df_basic[cfg['col']], label='Wariant: basic', color='tab:blue', linewidth=1.5)
    plt.plot(df_alt['k'], df_alt[cfg['col']], label='Wariant: alt', color='tab:orange', linestyle='--', linewidth=1.5)
    
    plt.yscale('log')
    plt.xlabel('k')
    plt.ylabel(f'Błąd {cfg["label"]} (log scale)')
    plt.title(f'Porównanie wariantów - błąd {cfg["label"]}\n({compiler}, $x_0={x0}$)')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    
    save_path = PLOTS_DEST / compiler.lower()
    save_path.mkdir(parents=True, exist_ok=True)
    plt.savefig(save_path / f'variant_comp_{delta_type}_{compiler}_{x0}.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    x0_gcc = '0.100000000000000000001'
    plot_errors('GCC', x0_gcc, 'basic')
    plot_errors('GCC', x0_gcc, 'alt')
    plot_variant_errors('GCC', x0_gcc, 'f')
    plot_variant_errors('GCC', x0_gcc, 'd')
    plot_variant_errors('GCC', x0_gcc, 'ld')
    