import laggedScore as ls
def windowScore(lag, pv1, pv2, w=30):
    #w is window size
    p1, v1 = pv1
    p2, v2 = pv2
    start, end, score, count = 0, 0, 0, 0
    #startup
    result = {}
    for i in range( len(p1) ):
        score += ls.ithScore(lag, pv1, pv2, i)
        count=i+1
        if i > w:
            score -= ls.ithScore(lag, pv1, pv2, i-w)
            count = w
        result[i] = score*score/count
    return result
