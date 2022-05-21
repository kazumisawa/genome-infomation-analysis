def kmerDistance(data1, data2):
    result = 0
    pair = data1.keys() | data2.keys() #union
    for i in pair:
        c1, c2 = 0,0
        if i in data1.keys():
            c1 = data1[i]
        if i in data2.keys():
            c2 = data2[i]
        result += abs( c1 - c2 )
    return result

