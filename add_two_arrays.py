from array import *
Number = int(input("Number of rows and columns of matrix 1:"))
matrix_1 = [ ]
print("Enter the values:")
for i in range(Number):         
    a =[ ]
    for j in range(Number):     
            a.append(int(input()))
    matrix_1.append(a)
for i in range(Number):
    for j in range(Number):
        print(matrix_1[i][j], end = " ")
    print( )
Number = int(input("Number of rows and columns of matrix 1:"))
matrix_2 = [ ]
print("Enter the values:")
for i in range(Number):         
    a =[ ]
    for j in range(Number):     
            a.append(int(input()))
    matrix_2.append(a)
for i in range(Number):
    for j in range(Number):
        print(matrix_2[i][j], end = " ")
    print( )
Res_matrix=[]
for i in range(Number):
    result=[]
    for j in range(len(matrix_2[0])):
        result.append(matrix_1[i][j]+matrix_2[i][j])
    Res_matrix.append(result)
for i in range (Number):
    for j in range (Number):
        print(Res_matrix[i][j], end =" ")
    print( )
