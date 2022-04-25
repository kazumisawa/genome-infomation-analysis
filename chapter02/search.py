def search(query, C, Occ, count):
    #最後の文字から始める
    c = query[-1]
    sp = C[c] + 1 #cの範囲の視点
    ep = C[c] + count[c] # cの終点はcの数を足す
    for c in reversed(query[:-1]):
        sp = C[c] + Occ[ (c, sp-1) ]+ 1
        ep = C[c] + Occ[ (c,ep) ]
        if sp>ep:
            return False
    return True
