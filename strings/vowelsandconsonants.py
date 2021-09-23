#How to calculate the number of vowels and consonants in a string?

def calculate(str):
    vowels=0
    consonants=0
    for i in str:
        if i in ['a','e','i','o','u']:
            vowels+=1
        else:
            consonants+=1
    return (vowels,consonants)

print(calculate("nitish"))