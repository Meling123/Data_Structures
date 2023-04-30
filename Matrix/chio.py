#the chio method for calculating the determinant of a matrix 

from matrix import Matrix


def calc_det_2x2(a) -> int:
    return a[0][0] * a[1][1] - a[1][0]* a[0][1]


def chio(matrix, a11 = 1) -> int:
    new_matrix = Matrix((matrix.size()[0] - 1, matrix.size()[1] - 1))
    
    if matrix[0][0] == 0:
        for i in range(1,matrix.size()[0]):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
                a11 *= -1
                break
    
    if matrix.size()[0] == 2:
        return a11 * calc_det_2x2(matrix)
    else:
        for i in range(new_matrix.size()[0]):
            for j in range(new_matrix.size()[1]):
                new_matrix[i][j] = calc_det_2x2([[matrix[0][0], matrix[0][i+1]],[matrix[j+1][0], matrix[j+1][i+1]]])
        a11 *= 1/(matrix[0][0]**(matrix.size()[0]-2))
        return chio(new_matrix, a11)

    

def main():
    m1 = Matrix(  [
        [0 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
        ])


    m2 = Matrix([

    [5 , 1 , 1 , 2 , 3],

    [4 , 2 , 1 , 7 , 3],

    [2 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]

    ])

    print(chio(m1))
    print(chio(m2))

main()