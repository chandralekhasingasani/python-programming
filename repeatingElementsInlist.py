#How to get the matching elements in an integer array

def matchingElements(list):
    a=set()
    for i in range(0,len(list)-1):
        if list[i] == list[i+1]:
            a.add(i)
    return a

print(matchingElements([20,3,4,5,6,20]))


