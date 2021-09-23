#Compute the first five Fibonacci numbers.

def fibbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    list=[0,1]
    for i in range(1,n-2+1):
        list.append(list[i]+list[i-1])
    return list

print(fibbo(10))
