import os

import pandas as pd


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:

    if not os.path.exists(output_path):
        {os.makedirs(output_path)}
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"
