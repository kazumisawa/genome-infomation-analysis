def isSubset(query, count):
    target = set(query)
    if target.issubset(count.keys()):
        return True
    else:
        return False
