import os
import json

FILE_LENGTH = {}

BASE_DIR = os.getcwd()

def appendLength(json_file : str) -> None:
    with open(json_file,'r',encoding='utf-8') as f:
        json_encoded = json.loads(f.read())
        FILE_LENGTH[json_file] = len(json_encoded)


for file in os.listdir():
    os.chdir(BASE_DIR)
    if os.path.isdir(file):
        os.chdir(os.path.join(BASE_DIR,file))
        for json_file in os.listdir():
            if (not json_file.endswith('.json')):
                continue
            appendLength(json_file)
    else:
        if (not file.endswith('.json')):
            continue
        appendLength(file)


print(FILE_LENGTH)