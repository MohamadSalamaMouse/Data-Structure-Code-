def parmut(string,l=0):
    if l==len(string)-1:
        print(string)
    else:
        for i in range(l,len(string)):
            str_copy=[char for char in string]
            str_copy[l],str_copy[i]=str_copy[i],str_copy[l]
            parmut(str_copy,l+1)
parmut('ABC')