def gameOfThrones(s):
    ct = 0
    cntr = collections.Counter(s)
    for key in cntr:
        if cntr[key]%2!=0:
            ct +=1
    if ct==0 or ct==1:
        return "YES"
    else:
        return "NO"