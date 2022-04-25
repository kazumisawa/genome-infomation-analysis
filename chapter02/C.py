def C(bwted, count):
    C = dict()
    tmp = sorted(count.keys())
    C[tmp[0]] = -1
    for i in range( len(tmp) -1 ) :
        c1, c2 = tmp[i], tmp[i+1]
        C[c2] = C[c1] + count[c1]
    return C
