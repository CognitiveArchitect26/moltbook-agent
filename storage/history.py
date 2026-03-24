import os
import json


HISTORY_FILE = "output/history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as file:
        return json.load(file)


def save_history(entry):
    history = load_history()
    history.append(entry)

    os.makedirs("output", exist_ok=True)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=2)

    return HISTORY_FILE