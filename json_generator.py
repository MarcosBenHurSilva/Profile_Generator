import json

def save_to_json(profiles, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(profiles, json_file, ensure_ascii=False, indent=2)