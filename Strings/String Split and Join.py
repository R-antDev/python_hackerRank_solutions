def split_and_join(line):
    splitLine = line.split(' ')
    return '-'.join(splitLine)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)