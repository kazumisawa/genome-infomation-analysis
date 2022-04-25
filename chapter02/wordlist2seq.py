def wordlist2seq(wordList):
    seqlist = list(wordList[0])
    for i in range( 1, len(wordList) ):
        seqlist.append(wordList[i][-1])
    return "".join(seqlist)
