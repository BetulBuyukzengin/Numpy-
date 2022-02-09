# -*- coding: utf-8 -*-
"""
B=[1 2 -3    
  3 4 -1]         
                      
A=[2 -5 1
   1 4 5
   2 -1 6]

y=[2
   -4
   1]

z=[-15
   -8
   -22]

B*A=?
A*B^T=?
A*y=?
y^T*z=?
y*z^T=?
"""
import numpy as np

# B matrix
B=np.matrix("1 2 -3 ; 3 4 -1")
print("B matrix:")
print(B)
print("\n")

# A matrix
A=np.matrix("2 -5 1 ; 1 4 5 ; 2 -1 6")
print("A matrix:")
print(A)
print("\n")

# y matrix 
y_matrix = np.array([[2],
                    [-4],
                    [1]])
print("y matrix:")
print(y_matrix)
print("\n")

# z matrix 
z_matrix = np.array([[-15],
                     [-8],
                     [-22]])
print("z matrix:")
print(z_matrix)

print("*************** islemler ********************")

print("B*A = " )
print(np.dot(B,A))
print("\n")

print( "A*B^T =")
print(np.dot(A,B.transpose()))
print("\n")

print("A*y = " )
print(np.dot(A,y_matrix))
print("\n")

print("y^T*z = " )
print(np.dot(y_matrix.transpose(),z_matrix))
print("\n")


print("y*z^T = " )
print(np.dot(y_matrix,z_matrix.transpose()))





