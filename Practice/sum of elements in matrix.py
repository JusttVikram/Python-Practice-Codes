# Given a non null integer matrix Grid of dimensions NxM.Calculate the sum of its elements.

def sumOfMatrix(N, M, Grid):
    sum = 0
    for i in range(N):
        for j in range(M):
            sum += Grid[i][j]
    return sum