import numpy as np
def connect(data):
    result = []
    keylist = list( data.keys() )
    start, end = keylist[0], keylist[0]-1
    for i in keylist:
        if i != (end+1):
            result.append( (start, end) )
            start = i
        end = i
    result.append( (start, end) )
    return result
