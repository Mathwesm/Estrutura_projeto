from app.pipeline.etl.extract import extract_format_excel
from app.pipeline.etl.load import load_excel
from app.pipeline.etl.trasnform import contact_data_frame

if __name__ == "__main__":
    data_frame_list = extract_format_excel("data/input")
    data_frame = contact_data_frame(data_frame_list)
    load_excel(data_frame=data_frame, output_path="data/output", file_name="output")
