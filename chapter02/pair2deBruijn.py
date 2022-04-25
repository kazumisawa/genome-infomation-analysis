import deBruijnGraph

def put_order(DFSresult):
    for i in range( len(DFSresult) ):
        DFSresult[i].order = i

def node2graph(pairList):
    nodeDict = dict()
    for p in pairList:
        for w in p:
            nodeDict[w] = deBruijnGraph.deBruijnGraph(w)
    for p in pairList:
        nodeDict[p[0]].addKid( nodeDict[p[1]] )
    return nodeDict
