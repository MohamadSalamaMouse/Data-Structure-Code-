from stack import stack

def per_checker(symbol_string):# (())
    s1=stack()
    balanced=True
    index=0
    while index<len(symbol_string) and balanced:
        symbol=symbol_string[index]
        if symbol=='(':
            s1.push(symbol)
        else:
            if s1.is_empty():
                balanced=False
            else:
                s1.pop()
        index+=1
    if balanced and s1.is_empty():
        return True
    else:
        return False
print(per_checker('(()'))
