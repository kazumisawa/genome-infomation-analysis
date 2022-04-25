def readVectors(dataName):
    first, second, third = dict(), dict(), dict()
    with open(dataName, 'r') as dataFile:
        for line in dataFile:
            if line[0]!="#":
                itemList = line.strip().split('\t')
                nucleotide = itemList[0]
                first[nucleotide]  = float(itemList[1])
                second[nucleotide] = float(itemList[2])
                third[nucleotide]  = float(itemList[3])
        first['-'], second['-'], third['-'] = 0, 0, 0
    return first, second
