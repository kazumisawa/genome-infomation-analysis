import groupMAFFT
import fastaOutput as fa

class sequenceNode:
    children = None
    OTUname = None
    sequenceList = None
    aligned = False

    def __init__(self, OTUname, sequence):
        self.OTUname = OTUname
        self.sequenceList = list()
        self.sequenceList.append(sequence)
        self.children = list()
        self.aligned = True

    def addKid(self, newNode):
        self.children.append(newNode)
        self.aligned = False

    def getList(self):
        if self.aligned == True:
            return self.sequenceList
        else:
            sequence = list()
            for i in self.children:
                tmp = i.getList()
                for k in tmp:
                    sequence.append(k)
        return sequence

    def alignment(self, p, v):
        if self.aligned == False:
            tmp = list()
            for i in self.children:
                tmp.append( i.alignment(p,v) )
            result = groupMAFFT.groupMAFFT(tmp[0], tmp[1], p, v)
            self.sequenceList = result
            self.aligned = True
        return self.sequenceList

    def show(self):
        for i in self.children:
            i.show()
        if len(self.sequenceList)==1:
            fa.fastaOutput( self.OTUname, self.sequenceList[0] )
