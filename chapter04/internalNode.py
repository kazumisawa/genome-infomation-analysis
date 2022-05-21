#import node

#class internalNode( node.node) :
class internalNode():
    children = None
    OTUname = None
    sequence = None
    def __init__(self, OTUname):
        self.OTUname = OTUname
        self.children = []

    def addKid(self, newNode):
        self.children.append(newNode)

    def getSequence(self):
        sequence = list()
        for i in self.children:
            tmp = i.getSequence()
            for k in tmp:
                sequence.append(k)
        return sequence

    def nodeNewick(self):
        leaf=False
        if len(self.children)==0:
            result = self.OTUname
        else:
            nodeList=[]
            for kid in self.children:
                tmp = kid.nodeNewick()
                if tmp!=None:
                    nodeList.append( tmp )
            result = ",".join(nodeList)
            if len(nodeList)>1:
                result = "(" + result + ")"
        return result
