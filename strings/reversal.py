#How can you reverse a string?

def reverse(text):
    rev = ''
    for i in range(len(text)-1, -1, -1):
        rev += text[i]
    return rev

print("The reversed string is ",reverse("abcdefg"))

