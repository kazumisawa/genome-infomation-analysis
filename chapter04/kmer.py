def count(wordLength, seq):
    result = dict()
    for i in range( len(seq) - wordLength + 1):
        word = str(seq[i: i + wordLength])
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result

