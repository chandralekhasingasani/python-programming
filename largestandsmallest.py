#largest and second largest number

def largestElement(list):
    max=0
    secondmax=-1
    for i in list:
        if i>max:
            secondmax=max
            max=i
        if i>secondmax and max!=i:
            secondmax=i
    return (max,secondmax)

print(largestElement[3,5,1,2])
