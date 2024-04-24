import math
import os
import random
import re
import sys


def solve(s):
    tmp = s.split(' ')
    result = []
    for word in tmp:
        result.append(word.capitalize())
    return ' '.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
