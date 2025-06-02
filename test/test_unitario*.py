import os

import pandas as pd
import pytest

from app.pipeline.etl import extract, load, trasnform

df1 = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
df2 = pd.DataFrame({"A": [4, 5, 6], "B": ["d", "e", "f"]})


@pytest.fixture
def mock_input_folder(tmpdir):
    input_folder = tmpdir.mkdir("input_folder")
    df1.to_excel(str(input_folder.join("file1.xlsx")), index=False)  # Corrigido: str()
    df2.to_excel(str(input_folder.join("file2.xlsx")), index=False)
    return str(input_folder)


@pytest.fixture
def mock_output_folder(tmpdir):
    return str(tmpdir.mkdir("output_folder"))


def test_extract(mock_input_folder):
    extracted_data = extract.extract_format_excel(mock_input_folder)
    assert len(extracted_data) == 2
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)


def test_extract_no_files(tmpdir):
    empty_folder = tmpdir.mkdir("empty_folder")
    with pytest.raises(ValueError, match="No Excel files found"):
        extract.extract_format_excel(str(empty_folder))


def test_transform():
    data = [df1, df2]
    consolidated_df = trasnform.contact_data_frame(data)
    assert len(consolidated_df) == 6
    assert list(consolidated_df.columns) == ["A", "B"]


def test_transform_empty_list():
    empty_list = []
    with pytest.raises(ValueError, match="No data to transform"):
        trasnform.contact_data_frame(empty_list)


def test_load(mock_output_folder):
    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    output_file_name = "consolidated.xlsx"
    output_file = os.path.join(mock_output_folder, output_file_name)

    saved_file = load.load_excel(df, mock_output_folder, output_file_name)

    assert saved_file == output_file
    assert os.path.exists(output_file)

    loaded_df = pd.read_excel(output_file)
    pd.testing.assert_frame_equal(loaded_df, df)
