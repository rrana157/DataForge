import json, os
from typing import Any


def load_files_data(file_name: str) -> Any:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data_libraries")
    file_path = os.path.join(DATA_DIR, file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data # Return the complete job data entries
