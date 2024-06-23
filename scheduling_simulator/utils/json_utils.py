import json
from typing import List, Dict

def read_json_file(file_path: str) -> Dict:
    with open(file_path, "r") as file:
        return json.load(file)
    
def save_json_file(file_path: str, data: Dict):
    with open(file_path, "w") as file:
        json.dump(data, file)

