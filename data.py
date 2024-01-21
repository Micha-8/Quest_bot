import json


def save_user_data(user_data, data_path):
    with open(data_path, 'w') as f:
        json.dump(user_data, f, indent=4)


def load_user_data(data_path):
    try:
        with open(data_path, 'r') as f:
            return json.load(f)
    except:
        return {}


data_path = "user_data.json"
user_data = load_user_data(data_path)
