def swap_case(s):
    s =list(s)
    for i,char in enumerate(s):
        if char.islower():
            s[i] = char.upper()
        elif char.isupper():
            s[i] = char.lower()
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)