import os

import pandas as pd

from app.ultis.ultis import log_decorador


@log_decorador
def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    os.makedirs(output_path, exist_ok=True)

    full_output = os.path.join(output_path, file_name)
    data_frame.to_excel(full_output, index=False)

    return full_output
