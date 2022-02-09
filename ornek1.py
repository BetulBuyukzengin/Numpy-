# -*- coding: utf-8 -*-
"""
 A=[3 4     
   -1 2]
                
B=[5 2
  8 -3]

A*B+2*B^2-I =?
"""
import numpy as np

#I birim matris
I=np.eye(2)
print("I matrix:")
print(I)
print("\n")

#A matrix
A=np.matrix("3 4 ; -1 2")
print("A matrix:")
print(A)
print("\n")

#B matrix
B=np.matrix("5 2 ; 8 -3")
print("B matrix:")
print(B)
print("\n")

# K=A*B
K=np.dot(A,B)
print("K=A*B=")
print(K)
print("\n")

# L=2*B**2
L=2*(np.dot(B,B))
#L=2*(np.power(B,2))
print("L=2*B**2=")
print(L)
print("\n")
#topl=K+L
# sonuc=K+L-I =A*B+2*B**2-I

topl=np.add(K,L)
print("A*B+2*B^2= ")
print(topl)
print("\n")

sonuc=np.subtract(topl,I)
print("A*B+2*B^2-I=")
print(sonuc)
#  parçalayarak yaptıgım işlemin, tek satırda yazilmiş hali :
    
#sonuc=np.subtract(np.add(np.dot(A,B),2*(np.dot(B,B))),I)
#print(sonuc)

