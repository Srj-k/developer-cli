import json

def load_json(path, default = []):
    try:
        with open(path, "r", encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {path}")


def save_json(data, path):

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    except OSError as e:
        raise IOError(f"Failed to write into file {path} : {e}")
    