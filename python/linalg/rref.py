def rref(M):
    if not M:
        return None
    R = M[:]
    lead = 0
    rows = len(R)
    cols = len(R[0])
    for r in range(rows):
        if lead >= cols:
            return R
        # Search the row with "leftest" leading value
        i = r
        while R[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return R
        # Exchange rows
        R[i],R[r] = R[r],R[i]
        # Get leading value
        lv = R[r][lead]
        R[r] = [ v / float(lv) for v in R[r] ]
        # Elimination step
        for i in range(rows):
            if i != r:
                lv = R[i][lead]
                R[i] = [ iv - lv*rv for iv,rv in zip(R[i],R[r]) ]
        lead += 1
    return R



if __name__ == "__main__":
    # Test if the reduced row echelon function
    A = [[ 1, 2, -1, -4],
         [ 2, 3, -1, -11],
         [-2, 0, -3, 22],]
    refA = rref(A)
    print(refA)


