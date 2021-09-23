def greatestCommonFactor(a,b):
    factor=1
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            factor=i
    return factor

print(greatestCommonFactor(2,4))
