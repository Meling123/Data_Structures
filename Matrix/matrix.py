class Matrix:

    def __init__(self, matrix, value = 0) -> None:
            if isinstance(matrix, tuple):
                self.matrix = [[value] * matrix[1] for i in range(matrix[0])]
            elif (isinstance(lst, list) for lst in matrix):
                self.matrix = matrix
            else:
                print("Wrong data type")
 
    
    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __add__(self, other):
        try:
            if self.size()[1] != other.size()[1] or self.size()[0] != other.size()[0]:
                raise ValueError
            new_matrix = Matrix((self.size()[0], self.size()[1]))
            for i in range(self.size()[0]):
                for j in range(len(self.matrix[i])):
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return new_matrix
        except ValueError:
            print('The shape of matrix does not match')
    

    def __mul__(self, other):
        try:
            if self.size()[0] != other.size()[1]:
                raise ValueError
            new_matrix = Matrix((self.size()[0], other.size()[1]))
            for i in range(self.size()[0]):                
                for j in range(other.size()[1]):
                    for k in range(other.size()[0]):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]                   
            return new_matrix
        except ValueError:
            print('The shape of matrix does not match')
    
    
    def __str__(self):
        return '\n'.join(str(row).replace('[','|').replace(']','|').replace(',', ' ') for row in self.matrix)

    
    def size(self) -> int:
        return len(self.matrix), len(self.matrix[0])


def transpose(matrix) -> Matrix:
    new_matrix = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def test():
    A = Matrix([[1, 0, 2],
                [-1, 3, 1]])
    B = Matrix((2, 3), value=1)
    C = Matrix([[3, 1],
                [2, 1],
                [1, 0]])

    print("Transposed matrix:")
    print(transpose(A))
    print("A + B")
    print(A + B)
    print("A * C")
    print(A * C)

