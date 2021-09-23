def reverselist(list):
    for i in range(0,len(list)/2):
        temp=list[i]
        list[i]=list[len(list)-i-1]
        list[len(list)-i-1]=temp
    return list

print(reverselist([3,4,5,6]))

