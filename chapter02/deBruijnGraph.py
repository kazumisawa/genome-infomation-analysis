import graphNode

class deBruijnGraph(graphNode.graphNode):
    def __init__(self, word0):
        super().__init__(word0)
        self.used = set()

    def Fleury(self, list0):
        list0.append(self.word)
        c = -1 # end of sequence
        for i in range(len(self.children)):
            if (c==-1) and (i not in self.used):
                if self.order >= self.children[i].lowlink:
                    c = i
        #crossing a bridge
        for i in range(len(self.children)):
            if (c==-1) and (i not in self.used):
                c = i
        if c >=0:
            self.used.add(c)
            self.children[c].Fleury(list0)

