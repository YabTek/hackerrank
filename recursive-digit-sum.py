def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return n
    else:
        total = 0
        for num in n:
            total += int(num)
        return superDigit(str(total*k),1)
        