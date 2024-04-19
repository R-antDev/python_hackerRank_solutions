if __name__ == '__main__':
    string = input()

    print(any(ch.isalnum() for ch in string))
    print(any(ch.isalpha() for ch in string))
    print(any(ch.isdigit() for ch in string))
    print(any(ch.islower() for ch in string))
    print(any(ch.isupper() for ch in string))

