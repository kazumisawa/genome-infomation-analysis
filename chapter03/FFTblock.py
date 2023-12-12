import traceBack
import segmentMatrix as se
import affineGapMatchMatrix as af
def FFTblock(region, len1, len2):
    end1, end2 = len1, len2
    range1, range2 = list(), list()
    if region != None and len(region)>0 :
        pos1, pos2, S =  se.segmentMatrix(region)
        direction = af.affineGapMatchMatrix(S, 10, 10)
        trace1, trace2 = traceBack.traceBack( direction )
        for i in range( len(trace1)-1 ):
            start1 = int(pos1[ trace1[i]-1 ])
            start2 = int(pos2[ trace2[i]-1 ])
            if start1 < len1 and start2 < len2:
                range1.append( (start1, end1) )
                range2.append( (start2, end2) )
                end1, end2 = start1, start2
    range1.append( (0, end1) )
    range2.append( (0, end2) )
    return (range1, range2)
