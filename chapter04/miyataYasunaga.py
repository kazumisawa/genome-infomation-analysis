import numpy as np

def miyataYasunaga( refPV, range1, tarPV, range2):
    # range1, range2は範囲を示すtuple
    start1, end1 = range1
    start2, end2 = range2
    # refPVはrefのpolarity, volumeのベクトルを組にしたtuple
    pol1, vol1 = refPV[0][start1:end1], refPV[1][start1:end1]
    # tarVはtarのpolarity, volumeのベクトルを組にしたtuple
    pol2, vol2 = tarPV[0][start2:end2], tarPV[1][start2:end2]
    m, n = len(pol1), len(pol2) 
    S = np.zeros( ( m, n ) )
    for i in range(m):
        for j in range(n):
            polDiff = pol1[i] - pol2[j]
            volDiff = vol1[i] - vol2[j]
            S[i,j] = polDiff*polDiff + volDiff*volDiff
    return S
