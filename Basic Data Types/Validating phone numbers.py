import re

numbers = []

for _ in range(int(input())):
    number = input()
    numbers.append(number)

numVal = r"\b[789]\d{9}\b"

for number in numbers:
    validation = re.search(numVal, number)

    if len(number) == 10 and validation:
        print('YES')
    else:
        print('NO')
