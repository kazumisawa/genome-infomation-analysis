import scoreMatrix as sc
import needlemanWunsch as nw
import gotoh82
def nestedAlignment(seq1, range1, seq2, range2, v, w):
    path1, path2 = list(), list()
    for i in range( len(range1) ):
        S = sc.scoreMatrix(seq1, range1[i], seq2, range2[i] )
        rel1, rel2 =  gotoh82.gotoh82(S, v, w)
        for position in rel1:
            path1.append( range1[i][0] + position )
        for position in rel2:
            path2.append( range2[i][0] + position )
    return path1, path2
