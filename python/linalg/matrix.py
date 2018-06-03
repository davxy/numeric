def multiply(A, B):
    R = [ [] for _ in range(len(A)) ]
    for i in range(len(A)):  #loops through rows
        for j in range (len(B[0])): # loops through cols
            R[i].append(0)
            for k in range(len(B)):
                R[i][j] += A[i][k] * B[k][j]
    return R

if __name__ == "__main__":
    # 3x3 matrix
    X = [[12,7,3],
         [4 ,5,6],
         [7 ,8,9]]
    # 3x4 matrix
    Y = [[5,8,1,2],
         [6,7,3,0],
         [4,5,9,1]]
    
    R = multiply(X, Y)
    print(R)

