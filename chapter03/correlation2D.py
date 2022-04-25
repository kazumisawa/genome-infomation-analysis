import correlation

def correlationPV(pv1, pv2):
    p1, v1 = pv1[0], pv1[1]
    p2, v2 = pv2[0], pv2[1]
    pr = correlation.correlation(p1, p2)
    vr = correlation.correlation(v1, v2)
    r = pr + vr
    return r
