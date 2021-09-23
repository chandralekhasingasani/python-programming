#Find the count for the occurrence of a particular character in a string.
def createDictionary(str,char):
    dict={}
    for i in str:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1

    return dict[char]

print(createDictionary("chandralekha",'a'))