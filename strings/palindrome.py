#What is a palindrome string?

def reverse(text):
    rev = ''
    for i in range(len(text)-1, -1, -1):
        rev += text[i]
    return rev

def isPalindrome(str):
    if str == reverse(str):
        return True
    else:
        return False

print(isPalindrome("malayalam"))