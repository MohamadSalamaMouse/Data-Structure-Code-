def myword(word):
    if len(word)==1:
        return word
    if word[0]==word[1]:
        return myword(word[1:])
    return word[0]+myword(word[1:])
    

n='mohamed'#moh amed
print(myword(n))
#factorial
def factorial(num):
    if num==0:
        return 1
    else:
        for i in range(1,num):
            num=num*i
    return num
print(factorial(12))
