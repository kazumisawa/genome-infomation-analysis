def burrowsWheelerTransform(seq):
    rotation, result  = list(), list()
    #巡回
    for i in range(len(seq)):
        rotation.append( seq[i:] + seq[:i])
    #ソート
    rotation.sort()
    #最後の一文字を取り出し
    for i in range(len(rotation)):
        result.append(rotation[i][-1])
    return ("".join(result))

