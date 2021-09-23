def primenumber(num):
    if num == 1 or num == 2:
        return True
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            return False
    return True

print(primenumber(7))