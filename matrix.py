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
        if self.h > 2: #***change value from 2 to 3 if determinant for 3x3 matrix is implemented***
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1: #determinant of 1x1 matrix (just the value itself)
            det = self.g[0][0]
        elif self.h == 2: #determinant of 2x2 matrix: ad-bc
            det = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        #elif self.h == 3: #determinant of 3x3 matrix: a(ei-fh) - b(di-fg) + c(dh-eg)
                           #where matrix = [[a,b,c],
                           #                [d,e,f],
                           #                [g,h,i]]
                   
        return det #return determinant
    

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        element_sum = 0 #initialize variable for sum of diagonal elements
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                if j == i:
                    element_sum += self.g[i][j]
        
        return element_sum
                    

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2: 
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1: #1x1 matrix: 1/value
            return Matrix([[1/self.g[0][0]]])
        elif self.h == 2: #2x2 matrix: (1/det(matrix))*[[],[]]
            dete = self.determinant()
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            matrix_inv = [[d,-b],[-c,a]]
            for i in range(len(matrix_inv)):
                for j in range(len(matrix_inv[i])):
                    matrix_inv[i][j] = (1.0/dete)*matrix_inv[i][j]
            return Matrix(matrix_inv)
            

        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = [] #initialize tranpose matrix list
        for i in range(len(self.g)):
            new_row = []
            for j in range(len(self.g[i])):
                new_row.append(self.g[j][i])
            matrix_transpose.append(new_row)
        
        return Matrix(matrix_transpose)
        
        
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
        #       
        result = [] #1x1 matrices are also in nested lists so the method below applies
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[i])):
                row.append(self.g[i][j] + other.g[i][j])
            result.append(row)
        
        return Matrix(result) 
                

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
        #
        result = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[i])):
                row.append(-self.g[i][j]) #negate all values in matrix
            result.append(row)
        
        return Matrix(result)       
        
        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        #Same code for __add__ but just subtract
        result = [] #1x1 matrices are also in nested lists so the method below applies
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[i])):
                row.append(self.g[i][j] - other.g[i][j])
            result.append(row)
        
        return Matrix(result) 

    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def get_row(matrix,row): #get currently called row elements
            return matrix[row]
        
        def get_column(matrix, column_number): #get currently called column elements
            column = []
            for i in range(len(matrix)):
                column.append(matrix[i][column_number])
            return column
        
        def dot_product(vector_one, vector_two): #dot product of current row and column
            new_vector = []
            for i in range(len(vector_one)):
                new_vector.append(vector_one[i]*vector_two[i])
            return sum(new_vector)
        
        self_rows = len(self.g)
        other_columns = len(other.g[0])
        result = [] #this is the result of matrix multiplication
        
        for i in range(self_rows):
            current_row = get_row(self.g, i)
            row_result = []
            for j in range(other_columns):
                current_column = get_column(other.g,j)
                element_dprod = dot_product(current_row,current_column)      
                row_result.append(element_dprod)
            result.append(row_result)
        
        return Matrix(result) 
        

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
        
        result = []
        
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            #self is matrix and other is scalar value to be multiplied by for each matrix element
            for i in range(len(self.g)):
                row = []
                for j in range(len(self.g[i])):
                    row.append(other*self.g[i][j])
                result.append(row)
        
        return Matrix(result) 
            
            
            