import sys
import pandas as pd
from pathlib import Path

def format_typst_table(input_csv: str | Path, output_txt: str | Path) -> None:
    """
    Reads data from a CSV file and generates Typst table code.
    """
    input_path = Path(input_csv)
    output_path = Path(output_txt)

    if not input_path.exists():
        print(f"Error: File {input_path} not found. Make sure to generate the data first.")
        sys.exit(1)

    df = pd.read_csv(input_path)

    # Start of the Typst table block
    # We use figure() to allow adding a caption at the bottom of the table
    typst_code = '''#figure(
  caption: [Wyniki wyznaczone po rozwiązaniu układu równań $A_I x = b$],
  table(
    columns: (auto, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt,
    table.header(
      table.cell(colspan: 3)[*Zestawienie wyników układu równań macierzy* $A_I$],
      [], [*Precyzja float32*], [*Precyzja float64*],
      [*n*], [$||x||_"max"$], [$||x||_"max"$]
    ),
'''
    
    # Iterate over DataFrame rows and add them to the Typst table
    for _, row in df.iterrows():
        n = int(row['n'])
        
        val32 = row.get('||x||_max_float32', '')
        val64 = row.get('||x||_max_float64', '')
        
        # Format to scientific notation if values are numbers
        if isinstance(val32, (int, float)):
            val32 = f"{val32:.4e}"
        if isinstance(val64, (int, float)):
            val64 = f"{val64:.4e}"
            
        typst_code += f"    [{n}], [{val32}], [{val64}],\n"
        
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
    
    INPUT_FILE = PROJECT_ROOT / "data" / "exercise1_data.csv"
    OUTPUT_FILE = SCRIPT_DIR / "exercise1_typst_table.txt"
    
    print("Starting CSV to Typst conversion...")
    format_typst_table(INPUT_FILE, OUTPUT_FILE)
