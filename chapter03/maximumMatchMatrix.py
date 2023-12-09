import numpy as np

def maximumMatchMatrix(S, d):
    len1, len2 = S.shape #tate, yoko
    #Fはスコアの行列。一行１列分大きくなる
    F  = np.zeros( (len1+1, len2+1) )
    # 左斜め上、上、左を使った時のコードを0, 1, 2とする。
    upleft, up, left = 0, 1, 2
    # directionはスコアを計算した時に利用したセルの場所の記録
    direction  = np.zeros_like(F)
    # 0列目を-i*dで埋める。
    for i in range(len1+1):
        F[i,0], direction[i,0] = -d*i, up 
    # 0行目を-j*dで埋める。
    for j in range(len2+1):
        F[0,j], direction[0,j] = -d*j, left
    compare = np.zeros(3)
    for j in range(len2):
        for i in range(len1):
            compare[ upleft ] = F[i,  j  ] + S[i,j]
            compare[ up     ] = F[i,  j+1] - d
            compare[ left   ] = F[i+1,j  ] - d
            status = np.argmax(compare)
            F[i+1,j+1] = compare[ status ]
            direction[i+1,j+1] = status
    # goalを-1にする
    goal = -1
    direction[0, 0] = goal
    return direction
