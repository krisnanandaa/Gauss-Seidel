import numpy as np
import sys

n = int(input("Masukan Jumlah n = "))

a = np.zeros((n,n))

print("Matrix A")

for i in range(n):
    for j in range(n):
        a[i][j] = float(input("A[" + str(i) +"][" + str(j) + "] = "))

b =  np.zeros((n,1))
print("Matrix B")
for i in range(n):
    b[i] = float(input("B[" + str(i) +"] = "))

Matrix = np.column_stack((a,b))
print("Matrix")
print(Matrix)

Iterasi = int(input("Masukan Jumlah Iterasi = "))
Error = float(input("Masukan Toleransi Nilai Error = "))
Nilai = float(input("Masukan Nilai Awal = "))

NilaiAwal = np.zeros((n,1))
for i in range(n):
    NilaiAwal[i] = Nilai

print("i\t", end=" ")
for i in range(n):
    print("x[%d]\t" %(i+1),end=" ")
for i in range(n):
    print("e[%d]\t" %(i+1),end=" ")
print(" ")
print("========================================")

i = 0
print("%d" %i,end=" ")
for i in range(n):
    s = np.float_(NilaiAwal[0])
    
    print("\t", s,end=" ")

hasil = np.zeros(n)
temp = np.zeros(n)

print(" ")
for k in range(1, Iterasi+1):
    print("%d", k,end=" ")
    for i in range(n):
        sigma = 0
        for j in range(n):
            if(i != j):
                sigma = sigma + NilaiAwal[j]*Matrix[i][j]
            
            hasil[i] = (Matrix[i][n] - sigma)/Matrix[i][j]
            temp[i] = NilaiAwal[i]
            NilaiAwal[i] = hasil[i]
            print("\t%.4f" %NilaiAwal[i],end=" ")
        for i in range(n):
            print(" %.4f" %abs(temp[i] - hasil[i]),end=" ")
        print(" ")

print(" ")
print("Hasil = ")
for i in range(n):
    print("x[%d]= %.4f" %(i+1, NilaiAwal[i]))
