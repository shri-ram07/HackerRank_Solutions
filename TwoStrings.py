def twoStrings(s1, s2):
    co = set(s1)&set(s2)
    if co:
        return "YES"
    else:
        return "NO"