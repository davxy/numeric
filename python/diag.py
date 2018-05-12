def diag_solve(D, b):
    '''
    input:
      diag: vector with matrix diagonal elements
      b: known terms vector
    returns: result vector
    '''
    dlen = len(D)
    if dlen != len(b):
        print("Error: input vectors lengths mismatch")
    x = list(range(dlen))
    for i in list(range(dlen)):
        x[i] = float(b[i])/D[i]
    return x

# Usage example
if __name__ == '__main__':
    D = [3,5,7,3,1,7,9,10,1,2]
    b = [4,8,1,4,3,9,10,12,11,7]
    x = diag_solve(D, b)
    print(x)

