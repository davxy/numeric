# Diagonal linear system solver

def diagonal(D, b):
    '''
    Input:
      - D: vector with matrix diagonal elements
      - b: known terms vector
    Output:
      - x : result vector
    '''
    dlen = len(D)
    if dlen != len(b):
        raise Exception("Error: input vectors lengths mismatch")
    x = list(range(dlen))
    for i in list(range(dlen)):
        x[i] = float(b[i])/D[i]
    return x
