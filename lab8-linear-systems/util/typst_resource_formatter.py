import sys
import argparse
import pandas as pd
from pathlib import Path

def parse_val(val, is_memory=False) -> str:
    """Helper function to format values consistently."""
    if pd.isna(val):
        return "-"
    if is_memory:
        # Konwersja bajtów na KB z jednym miejscem po przecinku
        return f"{float(val) / 1024:.1f}"
    if isinstance(val, (int, float)):
        return f"{val:.4e}"
    return str(val)

def generate_error_table(df: pd.DataFrame) -> str:
    """Generates Typst code for the Error Comparison table."""
    typst_code = '''#figure(
  caption: [Porównanie błędu: Eliminacja Gaussa vs Algorytm Thomasa],
  table(
    columns: (auto, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt,
    table.header(
      table.cell(rowspan: 2)[*n*],
      table.cell(colspan: 2)[*Eliminacja Gaussa*],
      table.cell(colspan: 2)[*Algorytm Thomasa*],
      
      [*f32*], [*f64*], [*f32*], [*f64*]
    ),
'''
    for _, row in df.iterrows():
        n = int(row['n'])
        eg_32 = parse_val(row.get('||x||_max_gauss_float32'))
        eg_64 = parse_val(row.get('||x||_max_gauss_float64'))
        et_32 = parse_val(row.get('||x||_max_thomas_float32'))
        et_64 = parse_val(row.get('||x||_max_thomas_float64'))
        
        typst_code += f"    [{n}], [{eg_32}], [{eg_64}], [{et_32}], [{et_64}],\n"
        
    typst_code += '''  )
)
'''
    return typst_code

def generate_resource_table(df: pd.DataFrame) -> str:
    """Generates Typst code for the Resource (Time & Memory) Comparison table."""
    # Używamy nieco mniejszej czcionki (9pt), bo mamy 9 kolumn
    typst_code = '''#figure(
  caption: [Porównanie zużycia zasobów: Eliminacja Gaussa vs Algorytm Thomasa],
  #set text(size: 9pt)
  table(
    columns: (auto, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt,
    table.header(
      table.cell(rowspan: 3)[*n*],
      table.cell(colspan: 4)[*Eliminacja Gaussa*],
      table.cell(colspan: 4)[*Algorytm Thomasa*],
      
      table.cell(colspan: 2)[*Czas [s]*], table.cell(colspan: 2)[*Pamięć [KB]*],
      table.cell(colspan: 2)[*Czas [s]*], table.cell(colspan: 2)[*Pamięć [KB]*],
      
      [*f32*], [*f64*], [*f32*], [*f64*],
      [*f32*], [*f64*], [*f32*], [*f64*]
    ),
'''
    for _, row in df.iterrows():
        n = int(row['n'])
        tg_32 = parse_val(row.get('time_gauss_float32'))
        tg_64 = parse_val(row.get('time_gauss_float64'))
        mg_32 = parse_val(row.get('mem_gauss_float32'), is_memory=True)
        mg_64 = parse_val(row.get('mem_gauss_float64'), is_memory=True)
        
        tt_32 = parse_val(row.get('time_thomas_float32'))
        tt_64 = parse_val(row.get('time_thomas_float64'))
        mt_32 = parse_val(row.get('mem_thomas_float32'), is_memory=True)
        mt_64 = parse_val(row.get('mem_thomas_float64'), is_memory=True)
        
        typst_code += (
            f"    [{n}], "
            f"[{tg_32}], [{tg_64}], [{mg_32}], [{mg_64}], "
            f"[{tt_32}], [{tt_64}], [{mt_32}], [{mt_64}],\n"
        )
        
    typst_code += '''  )
)
'''
    return typst_code

def format_typst_tables(input_csv: str | Path, output_txt: str | Path, table_type: str) -> None:
    """Main routing function to load data and generate selected tables."""
    input_path = Path(input_csv)
    output_path = Path(output_txt)

    if not input_path.exists():
        print(f"Error: File {input_path} not found. Make sure to run experiment 3 first.")
        sys.exit(1)

    df = pd.read_csv(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if table_type in ['error', 'both']:
        # If 'both' has been chosen, add sufix to the filename in order to not override the previous one
        p = output_path.with_name(f"{output_path.stem}_error{output_path.suffix}") if table_type == 'both' else output_path
        p.write_text(generate_error_table(df), encoding='utf-8')
        print(f"Successfully generated Error table in: {p}")

    if table_type in ['resource', 'both']:
        p = output_path.with_name(f"{output_path.stem}_resource{output_path.suffix}") if table_type == 'both' else output_path
        p.write_text(generate_resource_table(df), encoding='utf-8')
        print(f"Successfully generated Resource table in: {p}")

if __name__ == "__main__":
    SCRIPT_DIR = Path(__file__).parent.resolve()
    PROJECT_ROOT = SCRIPT_DIR.parent
    
    parser = argparse.ArgumentParser(description="Generate Typst tables for Gauss vs Thomas comparisons.")
    
    parser.add_argument(
        "-i", "--input", 
        type=str, 
        default=str(PROJECT_ROOT / "data" / "exercise3_data.csv"),
        help="Path to the input CSV file from experiment 3"
    )
    
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default=str(SCRIPT_DIR / "exercise3_typst_table.txt"),
        help="Base path where the Typst table text file(s) will be saved"
    )
    
    parser.add_argument(
        "-t", "--type",
        choices=['error', 'resource', 'both'],
        default='both',
        help="Choose which table to generate: 'error', 'resource', or 'both' (default: both)"
    )
    
    if len(sys.argv) == 1:
        print("Using default paths and generating BOTH tables. Run with -h for more options.\n")
        
    args = parser.parse_args()
    
    print(f"Starting CSV to Typst conversion (Mode: {args.type.upper()})...")
    format_typst_tables(args.input, args.output, args.type)
    