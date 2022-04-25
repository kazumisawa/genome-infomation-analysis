def inverseBWT(L, LF):
    result = list()
    start = L.find("$")
    c, i = L[start], LF[start]
    for j in range( len(L) ):
        c = L[i]
        i = LF[i]
        result.append(c)
    return "".join(result)[::-1]
