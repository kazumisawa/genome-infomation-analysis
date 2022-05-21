def tree2pair(tree):
    parentOf = dict()
    leaves = tree.get_terminals()
    for leaf in leaves:
        path = tree.get_path(leaf)
        if len(path)>0 :
            parentOf[ path[0].name ] = tree.root.name
            for i in range(len(path)-1):
                parentOf[ path[i+1].name ] = path[i].name
    return parentOf
