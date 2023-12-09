import numpy as np
import outputMatrix as om

def affineGapMatchMatrix(S, u, v):
    len1, len2 = S.shape #tate, yoko
    #Fはスコアの行列。一行１列分大きくなる
    H  = np.zeros( (len1+1, len2+1) )
    # 左斜め上、上、左を使った時のコードを0, 1, 2とする。
    upleft, up, left = 0, 1, 2
    # directionはスコアを計算した時に利用したセルの場所の記録
    direction  = np.zeros_like(H)
    # 0列目を-i*vで埋める。
    for i in range(len1+1):
        H[i,0], direction[i,0] = -v*i, up 
    # 0行目を-j*vで埋める。
    for j in range(len2+1):
        H[0,j], direction[0,j] = -v*j, left
    # PとQを作成
    P, Q  = H.copy(), H.copy()
    compare = np.zeros(3)
    for i in range(len1):
        for j in range(len2):
            P[i+1, j+1] = max( H[i,j+1]-u, P[i,j+1]-v )
            Q[i+1, j+1] = max( H[i+1,j]-u, Q[i+1,j]-v )
            compare[ upleft ] = H[i,   j  ] + S[i,j]
            compare[ up     ] = P[i,   j+1]
            compare[ left   ] = Q[i+1, j  ]
            status = np.argmax(compare)
            H[i+1,j+1] = compare[ status ]
            direction[i+1,j+1] = status
    # goalを-1にする
    goal = -1
    direction[0, 0] = goal
    return direction
