# Input: a file expected json format. Output: sum, count, average.

import json
import sys

# Initialize variable
sum = 0

# Read json file
try:
    with open('sample.json') as input:
        data = json.load(input)

    # Calculate sum, count & average
    try:
        for number in data['number']:
            sum = sum + number['int']
            count = len(data['number'])
            average = sum / count

        print("Sum : ", sum)
        print("Count : ", count)
        print("Average : ", average)

    except:
        print("Oops!", sys.exc_info()[0], "occurred.")

except:
    print("Oops! Something went wrong when reading the JSON file.")
