def reverseNum(num):
    rev=0
    while num>0:
        rev=(rev*10)+(num%10)
        num=int(num/10)
    return rev

print(reverseNum(300))
