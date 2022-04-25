def Occ(bwted):
    Occ, count =  dict(), dict()
    size = len(bwted)
    s = set(bwted)
    for c in s:
        count[c] = 0

    for i in range(size):
        c = bwted[i]
        #count[c]は文字cの数
        count[c] += 1
        #Occ[(c,i)]はi番目の文字がc中では何番目か
        Occ[ (c, i) ] = count[c]
    for c in count.keys():
        prev = 0
        for i in range(size):
            if (c,i) not in Occ:
                Occ[ (c,i)] = prev
            else:
                prev = Occ[ (c,i) ]
    return Occ, count
