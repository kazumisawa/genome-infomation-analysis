import peak
import groupMatrix as gm
import correlation2D as c2
import candidateRegions as ca
import needlemanWunsch as nw
import putGroupGap as pg
import FFTblock as fb
import nestedAlignment as ne
import groupPV


def groupMAFFT(reference, target, p, v):
    refPV = groupPV.groupPV(reference, p, v)
    tarPV = groupPV.groupPV(target, p, v)
    cr = c2.correlationPV(refPV, tarPV)
    corrPeak = peak.peak( cr )
    region = ca.regions(corrPeak, refPV, tarPV)

    seq1 = reference[0]
    seq2 = target[0]
    region = ca.regions(corrPeak , refPV, tarPV)
    len1, len2 = len(refPV[0]), len(tarPV[0])
    r1, r2 = fb.FFTblock(region, len1, len2)
    path1, path2 = ne.nestedAlignment(seq1, r1, seq2, r2, 1, 1)
    result1 = pg.putGroupGap(reference, path1)
    result2 = pg.putGroupGap(target, path2)
    result = list()
    for i in result1:
        result.append(i)
    for i in result2:
        result.append(i)
    return result


