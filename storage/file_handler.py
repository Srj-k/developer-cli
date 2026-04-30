import json
import os

def load_json(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return ValueError(f"Invalid JSON format in file: {path}")


def save_json(data, path):

    try:
        directory = os.path.dirname(path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    except OSError as e:
        raise IOError(f"Failed to write into file {path} : {e}")
    