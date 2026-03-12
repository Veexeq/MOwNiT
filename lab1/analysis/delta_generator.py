import pandas as pd
from pathlib import Path
from mpmath import mp
import precise_sequence_gen as psg

mp.dps = 100

BASE_DIR    = Path(__file__).resolve().parent.parent
GCC_SOURCE  = BASE_DIR / 'output' / 'gcc_results.csv'
MSVC_SOURCE = BASE_DIR / 'output' / 'msvc_results.csv'
OUTPUT_FILE = BASE_DIR / 'analysis' / 'precise_deltas' / 'precise_deltas.csv'

GCC_PRECISIONS = ['0.100000000000000000001', '0.100000099999999999997', '0.100000000000000099999']
MSVC_PRECISIONS = ['0.100000000000000005551', '0.100000099999999994549', '0.100000000000000102696']
VARIANTS = ['basic', 'alt']

def calculate_precise_delta(x0_str, actual_long_doubles):
    k_max = len(actual_long_doubles)
    ref_seq = psg.get_reference_sequence(x0_str, k_max)
    
    deltas = []
    for i, actual_val in enumerate(actual_long_doubles):
        diff = mp.absmin(ref_seq[i] - mp.mpf(str(actual_val)))
        deltas.append(float(diff))
    
    return deltas

def generate_csv():
    all_results = []
    
    compilers = {
        'GCC': {'file': GCC_SOURCE, 'precisions': GCC_PRECISIONS},
        'MSVC': {'file': MSVC_SOURCE, 'precisions': MSVC_PRECISIONS}
    }

    for comp_name, config in compilers.items():
        df = pd.read_csv(config['file'], dtype={'x0': str})
        
        for prec in config['precisions']:
            for var in VARIANTS:
                subset = df[(df['x0'] == prec) & (df['variant'] == var)].sort_values('k')
                
                if subset.empty:
                    continue
                
                actual_vals = subset['long_double_val'].tolist()
                k_values = subset['k'].tolist()
                
                precise_deltas = calculate_precise_delta(prec, actual_vals)
                
                for i in range(len(k_values)):
                    all_results.append({
                        'k': k_values[i],
                        'compiler': comp_name,
                        'x0': prec,
                        'variant': var,
                        'precise_delta': f"{precise_deltas[i]:.2e}"
                    })

    output_df = pd.DataFrame(all_results)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(OUTPUT_FILE, index=False)

if __name__ == '__main__':
    generate_csv()