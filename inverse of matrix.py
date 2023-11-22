def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(len(matrix)):
            determinant += (-1) ** i * matrix[0][i] * det(minor(matrix, 0, i))
        return determinant

def minor(matrix, i, j):
    minor_matrix = []
    for row in range(len(matrix)):
        if row != i:
            minor_row = []
            for col in range(len(matrix)):
                if col != j:
                    minor_row.append(matrix[row][col])
            minor_matrix.append(minor_row)
    return minor_matrix

def cofactor(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            sign = (-1) ** (i + j)
            minor_mat = minor(matrix, i, j)
            cofactor_row.append(sign * det(minor_mat))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix

def adjugate(matrix):
    adjugate_matrix = []
    for i in range(len(matrix)):
        adjugate_row = [matrix[j][i] for j in range(len(matrix))]
        adjugate_matrix.append(adjugate_row)
    return adjugate_matrix


def inverse(matrix):
    det_matrix = det(matrix)
    if det_matrix == 0:
        return None
    else:
        cofactor_matrix = cofactor(matrix)
        adjugate_matrix = adjugate(cofactor_matrix)
        inverse_matrix = []
        for i in range (len(adjugate_matrix)):
            inverse_matrix.append([])

        for i in range(len(adjugate_matrix)):
            for j in range(len(adjugate_matrix)):
                inverse_matrix[i].append(adjugate_matrix[i][j] / det_matrix)
            
        
        return inverse_matrix


matrix = [[1, 3,3], [4,5,6], [7,8,9]]
inverse_matrix = inverse(matrix)

if inverse_matrix is not None:
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("Inverse Matrix:")
    for row in inverse_matrix:
        print(row)
else:
    print("The matrix is not invertible")