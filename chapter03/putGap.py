def putGap(org, reverse): #pathをたどる
    #逆順で与えられた引数をさらに逆順にして元に戻す。
    forward = reverse[::-1] 
    result = list()
    #アラインメントされたかどうか記録するlist
    sequence = "$" + org 
    notAligned = [True] * len(sequence) 
    for x in forward:
        if notAligned[x] : #未アライン
            result.append( sequence[x] )
        else: #既にアラインメントされていればギャップを入れる 
            result.append( "-" )
        notAligned[x] = False
    return "".join( result[1:] )
