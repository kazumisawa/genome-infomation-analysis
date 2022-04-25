import node

class graphNode(node.node):
    def __init__(self, word0):
        super().__init__(word0)
        self.visit2 = False
        self.lowlink=0

    def DFSlowlink(self):
        self.visit2 = True
        self.lowlink = self.order
        for i in self.children:
            if i.visit2 == False:
                i.DFSlowlink()
                self.lowlink = min(self.lowlink, i.lowlink)
            else:
                self.lowlink = min(self.lowlink, i.order)
