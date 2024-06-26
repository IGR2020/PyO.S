import pickle
import os

def load_data(path):
    with open(path, "rb") as file:
        data = pickle.load(file)
        file.close()
    return data

def save_data(path, data):
    with open(path, "wb") as file:
        pickle.dump(data, file)
        file.close()
    return

def getSize(path):
    total = 0
    break_down = {}
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
                break_down[entry.name] = entry.stat().st_size
            elif entry.is_dir():
                total += getSize(entry.path)
    return total, break_down
