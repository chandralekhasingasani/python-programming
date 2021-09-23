#How to verify if two strings are a rotation mutually

def isrotated(str1,str2):
    if len(str1) == len(str2):
        return False
    else:
        org=str1+str1
        if str2 in org:
            return True
    return False

print(isrotated("abc","cba"))