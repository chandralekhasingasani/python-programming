#How to delete the repeated elements in an integer array?

def deleteRepeatedElements(list):
    dict={}
    for i in range(0,len(list)):
        if list[i] in dict:
            list.pop(i)
        else:
            dict[i]=1
    return list

print(deleteRepeatedElements([2,3,4,2,4]))


