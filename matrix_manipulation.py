import random

class pythonCode:
    def __init__(self, celerity, weight):
        self.c = celerity
        self.m = weight
        
    def energy(self):
        e = self.m * self.c ** 2
        return e
    
class printing(pythonCode):
    def __init__(self, celerity, weight):
        super().__init__(celerity, weight)
        
    def print_energy(self):
        obj_ = self.energy()
        print('-'*48)
        print(f'E = {obj_}')
        print('-'*48)
        
class matrix:
    def __init__(self, row, column):
        self.n = row
        self.m = column

class matrix_print(matrix):
    def __init__(self, row, column):
        super().__init__(row, column)
        
    def print_matrix(self):
        matx = []
        for i in range(self.n):
            mtx_add = []
            for j in range(self.m):
                mtx_add.append(random.randint(1,9))
            matx.append(mtx_add)
        return matx
    
    def matrix_with_for(self):
        our_matrix = self.print_matrix()
        print("Original Matrix\n")
        for i in our_matrix:
            print(' '.join(str(x) for x in i))
            # print(i)
        print('-'*48)
    
    def diagonal_with_zero(self):
        our_matrix = self.print_matrix()
        print("Matrix with 0 at the diagonal\n")
        for i in range(len(our_matrix)):
            for j in range(len(our_matrix)):
                our_matrix[i][i] = 0
        
        for prnt in our_matrix:
            print(' '.join(str(x) for x in prnt))
            # print(prnt)
        print('-'*48)
        return our_matrix

    def down_diagonal_with_zero(self):
        our_matrix = self.print_matrix()
        print("Matrix with 0 at the bottom of the diagonal\n")
        for i in range(len(our_matrix)):
            for j in range(len(our_matrix[i])):
                if i > j:
                    our_matrix[i][j] = 0
        
        for prnt in our_matrix:
            print(' '.join(str(x) for x in prnt))
            # print(prnt)
        print('-'*48)
        return our_matrix
    
    def up_diagonal_with_zero(self):
        our_matrix = self.print_matrix()
        print("Matrix with 0 at the top of the diagonal\n")
        for i in range(len(our_matrix)):
            for j in range(len(our_matrix[i])):
                if i < j:
                    our_matrix[i][j] = 0
        
        for prnt in our_matrix:
            print(' '.join(str(x) for x in prnt))
            # print(prnt)
        print('-'*48)
        return our_matrix
        
    def up_diagonal_with_sign_down(self):
        our_matrix = self.print_matrix()
        print("Matrix with sign at the bottom of the diagonal\n")
        for i in range(len(our_matrix)):
            for j in range(len(our_matrix[i])):
                if i < j:
                    our_matrix[i][j] = '-'
        
        for prnt in our_matrix:
            print(' '.join(str(x) for x in prnt))
            # print(prnt)
        print('-'*48)
        return our_matrix

    def up_diagonal_with_sign_up(self):
        our_matrix = self.print_matrix()
        print("Matrix with sign at the top of the diagonal\n")
        for i in range(len(our_matrix)):
            for j in range(len(our_matrix[i])):
                if i > j:
                    our_matrix[i][j] = '-'
        
        for prnt in our_matrix:
            print(' '.join(str(x) for x in prnt))
            # print(prnt)
        print('-'*48)
        return our_matrix
                
        
obj = printing(9, 3.9)
obj1 = matrix_print(12,12)
obj.print_energy()
obj1.matrix_with_for()
obj1.diagonal_with_zero()
obj1.down_diagonal_with_zero()
obj1.up_diagonal_with_zero()
obj1.up_diagonal_with_sign_up()
obj1.up_diagonal_with_sign_down()