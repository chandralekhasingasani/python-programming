#How to get the matching elements in an integer array

def matchingElements(list):
    a=set()
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                a.add(list[i])
    return a

print(matchingElements([20,3,4,5,6,6,20]))


