import scoreMatrix as sc
import affineGapMatchMatrix as am
import putGap
import traceBack
#import needlemanWunsch as nw
#import gotoh82
def nestedAlignment(seq1, range1, seq2, range2, v, w):
    #aligned sequences
    result1, result2 = list(), list()
    for i in range( len(range1) ):
        S = sc.scoreMatrix(seq1, range1[i], seq2, range2[i] )
        direction = am.affineGapMatchMatrix(S, v, w)
        path1, path2 = traceBack.traceBack( direction )
        print(range1)
        partial1 = seq1[ range1[i][0]:range1[i][1] ]
        partial2 = seq2[ range2[i][0]:range2[i][1] ]
        segment1 =  putGap.putGap( partial1, path1 )
        segment2 =  putGap.putGap( partial2, path2 )
        result1.append(segment1)
        result2.append(segment2)
    return "".join( result1[::-1] ), "".join( result2[::-1] )
