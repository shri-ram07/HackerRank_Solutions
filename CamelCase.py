def camelcase(s):
    ct =1
    for x in s:
        if x.isupper():
            ct +=1
    return ct