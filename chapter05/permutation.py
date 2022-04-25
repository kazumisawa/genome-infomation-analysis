import random as r

def permutation(seq):
    return "".join(  r.sample( list(seq), len(seq) )  )
