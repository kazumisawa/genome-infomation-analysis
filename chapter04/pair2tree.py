import sequenceNode as SN

def pair2tree(parentOf, dataDict):
    nodes, D, root = set(), dict(), list()
    for node in parentOf.keys():
        nodes.add(node)
        nodes.add( parentOf[node] )
    for node in nodes:
        seq=""
        if node in dataDict:
            seq = dataDict[node]
        D[node] = SN.sequenceNode( node, seq )
    for node in parentOf:
        D[ parentOf[node] ].addKid(D[node])
    for node in D:
        if node not in parentOf:
            root.append(D[node])
    return root

