class node:
    def __init__(self, word0):
        self.visit1 = False
        self.used = False
        self.children = list()
        self.word = word0
        self.order = 0

    def addKid(self, kid):
        self.children.append(kid)

    def DFS(self, list0):
        self.visit1 = True
        list0.append(self)
        for i in self.children:
            if i.visit1 == False:
                i.DFS(list0)
