from typing import List

import pandas as pd

from app.ultis.ultis import log_decorador


@log_decorador
def contact_data_frame(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    if not data_frame_list:
        raise ValueError("No data to transform")

    return pd.concat(data_frame_list, ignore_index=True)
