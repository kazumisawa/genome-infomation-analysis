def putGap(org, reverse): #pathをたどる
    result = ""
    flag = [1] * len(org)
    for i in range( len(reverse) ):
        x, char = reverse[i], "-"
        if x>=0 and flag[x] ==1 : #未アライン
            char = org[x]
        result, flag[x] = char + result, 0
    return result
