# generate random number

import json
from random import randint

# Data to be written
sample = {
    "note": "This file contains the sample data for the task.py",
    "number": [
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
        {"int": randint(0, 100)},
    ]
}

# Serializing json
json_object = json.dumps(sample, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    print('sample.json created.')
