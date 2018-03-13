import re
import json
import sys


def JSONify(text):
    left_positions = [b.start() for b in re.finditer('{', text)]
    right_positions = [b.start() for b in re.finditer('}', text)]

    num_left = 0
    i = 0
    j = 0
    start = 0
    log = []

    while i < len(left_positions) and j < len(right_positions):
        if left_positions[i] < right_positions[j]:
            num_left += 1
            i += 1
        else:
            num_left -= 1

            if num_left == 0:
                log.append(json.loads(text[start:right_positions[j] + 1]))
                start = left_positions[i]

            j += 1

    return log

if __name__ == '__main__':
    text = ''
    with open (sys.argv[1], 'r') as f:
        for line in f:
            text += line

    print JSONify(text)
