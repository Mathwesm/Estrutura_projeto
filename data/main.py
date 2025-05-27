import glob
import os

import pandas as pd

input_folder = "data/input"
output_folder = "data/output"
output_file_name = "consolidado.xlsx"


files = glob.glob(os.path.join(input_folder, "*.xlsx"))
if not files:
    raise ValueError("No Excel files found in the specified folder")

all_data = [pd.read_excel(file) for file in files]

print(all_data)

if not all_data:
    raise ValueError("No data to transform")


consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
consolidated_df.to_excel(os.path.join(output_folder, output_file_name), index=False)

print("Processamento concluído!")
