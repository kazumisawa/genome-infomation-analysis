import graphNode

def connectedComponents(originalPair, treeDict):
    connected = dict()
    for p in originalPair:
        connected[p[0]] = False
    result = list()
    for p in originalPair:
        tag = p[0]
        if connected[tag]==False:
            nodeList = list()
            treeDict[tag].DFS(nodeList)
            for OTU in nodeList:
                connected[OTU.word] = True
            result.append(nodeList)
    return result

