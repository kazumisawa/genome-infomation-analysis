import numpy as np

def traceBack( direction ): #pathをたどる
    len1, len2 = direction.shape # 配列の長さ
    # スタートの位置
    x, y = len1 - 1, len2 - 1
    # 通ったpathを記録  
    path1, path2 = list(), list()
    path1.append( x )
    path2.append( y )
    # 左斜め上、上、左を使った時のコードを0, 1, 2とする。
    upleft, up, left = 0, 1, 2
    # 行列の右上から左下に向かって埋めていく
    while x > 0 and y > 0:
        status = direction[x, y] 
        # statusの値に応じて次のステップを指定
        if status == upleft:
            x, y = x - 1, y - 1
        elif status == up:
            x = x - 1
        elif status == left:
            y = y - 1
        path1.append( x )
        path2.append( y )
    return path1, path2
    
