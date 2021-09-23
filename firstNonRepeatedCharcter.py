#How to compute the first character of a string that is not repeated?

def nonrepeating(str):
    char={}
    for i in str:
        if i in char.keys():
            char[i]=char[i]+1
        else:
            char[i]=1

    for i in str:
        if char[i] == 1:
            return i

nonrepeating("chandralelha")