import internalNode

class alignNode( internalNode.internalNode ):
    def __init__(self, OTUname):
        super(alignNode, self).__init__(OTUname)

    def recursiveAlign(self):
        align = []
        for kid in self.children:
            align.append( kid.recursiveAlign() )
        return  groupAlign(align)
