import pandas as pd

from app.pipeline.trasnform import contact_data_frame

df_1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df_2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})


def test_concat_list_dataFrame():
    data_frame_list = [df_1, df_2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    df = contact_data_frame(data_frame_list)

    assert df.shape == (4, 2)
    assert data_frame.equals(df)
    assert df.shape != (5, 2)
