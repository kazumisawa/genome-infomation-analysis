from Bio.Blast import NCBIWWW

seq = "WGCPGSPEMGLMGCPGVQAADALYALLRTFRWARVALVTAPQDLWVEAGHALSTALR"

result_handle = NCBIWWW.qblast('blastp', 'nr', seq)
with open ("my_blast.xml" , "w") as out_handle :
    out_handle.write(result_handle.read())
result_handle.close
