#How to calculate the number of numerical digits in a string

def numOfDigits(str):
    count=0
    for i in str:
        if i.isdigit():
            count+=1
    return count

print(numOfDigits("Opcqa123!"))
