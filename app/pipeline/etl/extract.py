import glob
import os
from typing import List

import pandas as pd

from app.ultis.ultis import log_decorador


@log_decorador
def extract_format_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    if not all_files:
        raise ValueError("No Excel " "files found")

    df_frame_list = []
    for file in all_files:
        df_frame_list.append(pd.read_excel(file))
    return df_frame_list
