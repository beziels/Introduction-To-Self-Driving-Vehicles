import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def get_row(matrix, row):
    """
        Get the row from a matrix
        Adapted from Udacity's Coding Matrices Section
    """
    return matrix[row]

def get_column(matrix, column_number):
    """
        Get the column from a matrix
        Adapted from Udacity's Coding Matrices Section
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column
    
def dot_product(vector_one, vector_two):
    """
        Dot product of two vectors
        Adapted from Udacity's Coding Matrices Section
    """
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if (self.h * self.w) ==1:
            return self.g[0][0]
        elif self.h == 2 & self.w == 2:
            return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        size = self.h
        determinant_sum = 0
        
        for i in range(size):
            determinant_sum += self.g[i][i]
            
        return determinant_sum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        matrix_inverse = zeroes(self.h, self.w)
        inverse_determinant = 1/self.determinant()
        
        if(self.h==1):
            matrix_inverse[0][0] = inverse_determinant
        elif self.h==2:
            matrix_inverse[0][0] = self.g[1][1] * inverse_determinant
            matrix_inverse[0][1] = -self.g[0][1] * inverse_determinant
            matrix_inverse[1][0] = -self.g[1][0] * inverse_determinant
            matrix_inverse[1][1] = self.g[0][0] * inverse_determinant
        return matrix_inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = zeroes(self.w, self.h)
        for i in range(self.h):
            for j in range(self.w):
                matrix_transpose.g[j][i] = self.g[i][j]
        return matrix_transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        matrix_sum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            matrix_sum.append(row)
        return Matrix(matrix_sum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        matrix_negative = []
        for i in range(self.h):
            dum = self.g[i]
            row = []
            for j in range(self.w):
                val_ij = self.g[i][j]
                neg  = (-1 * val_ij)
                row.append(neg)
            matrix_negative.append(row)
            
        return Matrix(matrix_negative)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        matrix_subtract = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            matrix_subtract.append(row)
        return Matrix(matrix_subtract)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        matrix_rows = self.h
        matrix_columns = other.w
        mat_mul = []
        for i in range(matrix_rows):
            row = []
            rowA = get_row(self.g, i)
            for j in range(matrix_columns):
                colB = get_column(other.g, j)
                dot_prod = dot_product(rowA, colB)
                row.append(dot_prod)
            mat_mul.append(row)
        return Matrix(mat_mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            scalar_multiply = []
            for r in self.g:
                new_val = []
                for item in r:
                    rmul = item * other
                    new_val.append(rmul)
                scalar_multiply.append(new_val)
            return Matrix(scalar_multiply)
            