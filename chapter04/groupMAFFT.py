import peak
import correlation2D as c2
import candidateRegions as ca
import putGroupGap as pg
import FFTblock as fb
from Bio import SeqIO
import readVectors
import fastaOutput as fa
import sys
import groupPV
import miyataYasunaga as ys
import traceBack
import affineGapMatchMatrix as am
import putGap
import time

def groupMAFFT(reference, target, p, v):
    lap1 = time.time()
    # reference, targetに含まれるOTUの数をm,nとする 
    m, n = len( reference ), len( target )
    # 配列の長さを代入
    len1, len2 = len( reference[0] ), len( target[0] )
    # reference groupをベクトルに
    refPV = groupPV.groupPV(reference, p, v, [0, len1])
    # target groupをベクトルに
    tarPV = groupPV.groupPV(target,    p, v, [0, len2] )
    # 相互相関関数を求める
    cr = c2.correlationPV(refPV, tarPV)
    # peakを求める
    corrPeak = peak.peak( cr )
    # 領域に分ける
    region = ca.regions(corrPeak , refPV, tarPV)
    range1, range2 = fb.FFTblock(region, len1, len2)
    # 領域ごとのアラインメントを行う
    segmentList1, segmentList2 = list(), list()
    for i in range( len(range1) ):
        # スコア行列を求める 
        S = ys.miyataYasunaga(refPV, range1[i], tarPV, range2[i] )
        GOP, GEP = 20, 1
        direction = am.affineGapMatchMatrix(S, GOP, GEP)
        path1, path2 = traceBack.traceBack( direction )
        # この領域のアラインメント
        segment1 = pg.putGroupGap(reference, path1, range1[i])
        segment2 = pg.putGroupGap(target, path2, range2[i])
        segmentList1.append(segment1)
        segmentList2.append(segment2)
    #segmentは逆順で出ているので順序を逆にする。
    reverse1, reverse2 = segmentList1[::-1], segmentList2[::-1]
    #segmentの数をsegmentSizeに
    segmentSize = len(reverse1)
    #配列出力準備
    result = list()
    # reference側のアラインメント結果を追加
    for i in range(m):
       result.append( "".join([ reverse1[k][i] for k in range(segmentSize) ] ) )
    # target側のアラインメント結果を追加
    for i in range(n):
       result.append( "".join([ reverse2[k][i] for k in range(segmentSize) ] ) )
    return result

