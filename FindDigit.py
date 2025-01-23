def findDigits(n):
    ct = 0
    a=list(str(n))
    for i in a:
        if i!="0":
            if n%int(i)==0:
                ct+=1