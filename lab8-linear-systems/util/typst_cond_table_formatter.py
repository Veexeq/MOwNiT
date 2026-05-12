import sys
import argparse
import pandas as pd
from pathlib import Path

def format_typst_cond_table(input_csv: str | Path, output_txt: str | Path) -> None:
    """
    Reads condition number data from a CSV file and generates Typst table code.
    """
    input_path = Path(input_csv)
    output_path = Path(output_txt)

    if not input_path.exists():
        print(f"Error: File {input_path} not found. Make sure to generate the data first.")
        sys.exit(1)

    df = pd.read_csv(input_path)

    # Start of the Typst table block
    # Adjusted header structure to match the provided sketch
    typst_code = '''#figure(
  caption: [Współczynnik uwarunkowania macierzy $A_I$ oraz $A_"II"$],
  table(
    columns: (auto, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt,
    table.header(
      [], table.cell(colspan: 4)[*współczynnik uwarunkowania macierzy*],
      [], table.cell(colspan: 2)[*Macierz $A_I$*], table.cell(colspan: 2)[*Macierz $A_"II"$*],
      [*n*], [*precyzja float32*], [*precyzja float64*], [*precyzja float32*], [*precyzja float64*]
    ),
'''
    
    # Iterate over DataFrame rows and add them to the Typst table
    for _, row in df.iterrows():
        n = int(row['n'])
        
        # Fetch data using the keys from the condition number CSV
        c1_32 = row.get('cond_A1_float32', '')
        c1_64 = row.get('cond_A1_float64', '')
        c2_32 = row.get('cond_A2_float32', '')
        c2_64 = row.get('cond_A2_float64', '')
        
        # Format to scientific notation if values are numbers
        if isinstance(c1_32, (int, float)): 
            c1_32 = f"{c1_32:.4e}"
        if isinstance(c1_64, (int, float)): 
            c1_64 = f"{c1_64:.4e}"
        if isinstance(c2_32, (int, float)): 
            c2_32 = f"{c2_32:.4e}"
        if isinstance(c2_64, (int, float)): 
            c2_64 = f"{c2_64:.4e}"
            
        # Add a 5-column row
        typst_code += f"    [{n}], [{c1_32}], [{c1_64}], [{c2_32}], [{c2_64}],\n"
        
    # Close the table and figure structure
    typst_code += '''  )
)
'''

    # Ensure the output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the generated code to the output file
    output_path.write_text(typst_code, encoding='utf-8')
        
    print(f"Successfully generated Typst table code in: {output_path}")

if __name__ == "__main__":
    SCRIPT_DIR = Path(__file__).parent.resolve()
    PROJECT_ROOT = SCRIPT_DIR.parent
    
    parser = argparse.ArgumentParser(description="Convert CSV condition number data to a Typst table format.")
    
    parser.add_argument(
        "-i", "--input", 
        type=str, 
        required=True,
        help="Path to the input CSV file"
    )
    
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        required=True,
        help="Path where the Typst table text file will be saved"
    )
    
    args = parser.parse_args()
    
    print("Starting CSV to Typst conversion...")
    format_typst_cond_table(args.input, args.output)