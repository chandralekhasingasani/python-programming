def bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-i-1):
            if list[j] > list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

list=[5,4,3]
bubble_sort(list)
print(list)