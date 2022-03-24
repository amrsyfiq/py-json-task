# ==========================================
# Title:  Python Json Task
# Author: Amir Syafiq
# Date:   12 March 2021
# ==========================================

# Input: a file expected json format. Output: sum, count, average.

import json
import sys

# Initialize variable
sum = 0
loop_count = 0

# Read json file
try:
    with open('sample.json') as input:
        data = json.load(input)

    # Calculate sum, count & average
    try:
        for number in data['number']:
            sum = sum + number['int']
            loop_count += 1

            if(loop_count > len(data['number'])):
                print("\nLoop Terminated\n")
                break

        count = len(data['number'])
        average = sum / count

        print("\nSum : ", sum, "\n")
        print("Count : ", count, "\n")
        print("Average : ", average, "\n")

    except:
        print("\nOops!", sys.exc_info()[1], "occurred.\n")

except:
    print("\nOops! Something went wrong when reading the JSON file.\n")
