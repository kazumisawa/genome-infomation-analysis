def ithScore(lag, pv1, pv2, i):
    j = i - lag
    p1, v1 = pv1
    p2, v2 = pv2
    if i < 0 or j <0:
        return 0
    if i >= len(p1) or j >= len(v2) :
        return 0
    return p1[i]*p2[j] + v1[i]*v2[j]
