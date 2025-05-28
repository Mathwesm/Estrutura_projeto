from typing import List

import pandas as pd


def contact_data_frame(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
