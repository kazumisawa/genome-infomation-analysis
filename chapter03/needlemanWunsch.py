import numpy as np
import scoreMatrix
import maximumMatchMatrix
import traceBack

def NeedlemanWunsch70(score, d):
    direction = maximumMatchMatrix.maximumMatchMatrix(score, d)
    path1, path2 = traceBack.traceBack( direction )
    # 先頭に文字$を追加した分を元に戻す
    result1 = [ path1[i]-1 for i in range( len(path1) -1 ) ]
    result2 = [ path2[i]-1 for i in range( len(path2) -1 ) ]
    return result1, result2

