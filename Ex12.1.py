import numpy
m=int(input('Nilai m = ')) # Baris
n=int(input('Nilai n = ')) # Kolom
matrix = numpy.zeros((m,n))
x=numpy.zeros((m))

vector = numpy.zeros((n))
comp = numpy.zeros((m))
error = []

print ("Metode Gauss_Siedel")
print ('Memasukan Matrix Koefisien Dan Vektor Solusi')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Matrix a["+str(r+1)+str(c+1)+"] = "))
    vector[(r)]=float(input('Matrix b['+str(r+1)+']: '))
tol = float(input("Jumlah Toleransi = "))
Itera = int(input("Jumlah Iterasi = "))

print("\n")
# print ("Método de Gauss-Seidel")

# Metode Gauss-Seidel
k=0
while k < Itera:
    suma=0
    k=k+1
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if (c != r):
                suma=suma+matrix[r,c]*x[c]               
        x[r]=(vector[r]-suma)/matrix[r,r]
        print("x["+ str(r)+"]:" + str(x[r]))
    del error[:]
    #Comprobación
    for r in range(0,m):
        suma = 0
        for c in range(0,n):
            suma = suma+matrix[r,c]*x[c]
        comp[r] = suma
        dif=abs(comp[r] - vector[r])
        error.append(dif)
        print("Error en[",r,"]", error[r])
    print("Iterasi Ke-", k)
    if all(i <= tol for i in error) == True:
        break
