def matchingcharacters(str):
    char={}
    for i in str:
        if i in char.keys():
            char[i]=char[i]+1
        else:
            char[i]=1

    for i in char.keys():
        if char[i] > 1:
            print(i)

matchingcharacters("nitish")
