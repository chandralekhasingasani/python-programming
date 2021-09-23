def missingNumber(list):
    sum=0
    for i in range(1,101):
        sum+=i
    actualsum=0
    for i in list:
        actualsum+=i

    return sum-actualsum

print(missingNumber(list(range(1,100))))


