#How do you prove that the two strings are anagrams?
def createDictionary(str):
    dict={}
    for i in str:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    return dict

def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        string1=createDictionary(str1)
        string2=createDictionary(str2)

        for i in string1.keys():
            if i not in str2:
                return False
            if string1[i] != string2[i]:
                return False
    return True

print(isAnagram("acb","abc"))
