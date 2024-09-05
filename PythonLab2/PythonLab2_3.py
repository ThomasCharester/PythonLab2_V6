def matrixCheck(matrix):
    if len(matrix) != len(matrix[0]): return False
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

print(matrixCheck([[1,2,3],[2,4,5],[3,5,6]]))
print(matrixCheck([[1,2,3],[1,2,3],[1,2,3]]))
print(matrixCheck([[1,2,3],[1,2,3],[1,2,3],[1,2,3]]))