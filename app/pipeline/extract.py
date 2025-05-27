import glob
import os
from typing import List

import pandas as pd


def extract_format_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    df_frame_list = []
    for file in all_files:
        df_frame_list.append(pd.read_excel(file))
    return df_frame_list


if __name__ == "__main__":
    df_frame_list = extract_format_excel(path="data/input")
    print(df_frame_list)
