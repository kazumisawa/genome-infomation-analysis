from Bio import SeqIO
import sys
import PAFFTcoding
import putGap
import convert
import correlation2D as c2
import candidateRegions as ca
import peak
import FFTblock
import nestedAlignment as ne
data = list()
for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    data.append(seq_record)
seq1, seq2 = data[0].seq, data[1].seq
ts, tv1 = PAFFTcoding.PAFFTcoding()
pv1 = convert.convertPV(seq1, ts, tv1)
pv2 = convert.convertPV(seq2, ts, tv1)
cr = c2.correlationPV(pv1, pv2)
corrPeak = peak.peak( cr )
region = ca.regions(corrPeak , pv1, pv2)
range1, range2 = FFTblock.FFTblock(region, len(pv1[0]), len(pv2[0]))
path1, path2 = ne.nestedAlignment(seq1, range1, seq2, range2, 0.5, 0.5)
print( ">" + data[0].id )
print( putGap.putGap( seq1, path1 ) )
print( ">" + data[1].id )
print( putGap.putGap( seq2, path2 ) )
python MAFFTalignmentDNA.py data.fas
