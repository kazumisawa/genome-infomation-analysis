import numpy as np

def traceBack(F): #pathをたどる
    len1, len2 = F.shape
    x, y = len1-1, len2-1
    path1, path2 = list(), list()
    path1.append( x )
    path2.append( y )
    while x!=0 and y!=0:
        s, pos1, pos2 = np.zeros(3), {}, {}
        s[0], pos1[0], pos2[0] = F[x-1, y-1], x-1, y-1 # gapなし
        s[1], pos1[1], pos2[1] = F[x-1, y], x-1, y # 配列1の方にgap
        s[2], pos1[2], pos2[2] = F[x, y-1], x, y-1 # 配列2の方にgap
        argmax = np.argmax(s)
        x,y  = pos1[argmax], pos2[argmax]
        path1.append( x )
        path2.append( y )
    return path1, path2
