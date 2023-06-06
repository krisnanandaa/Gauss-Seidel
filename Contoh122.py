import numpy as np

m = int(input('Nilai m = '))  # Baris
n = int(input('Nilai n = '))  # Kolom
matrix = np.zeros((m, n))
x = np.zeros(m)

vector = np.zeros(n)
comp = np.zeros(m)
error = []

print("Metode Gauss-Siedel Relaxation")
print('Memasukkan Matriks Koefisien dan Vektor Solusi')
for r in range(m):
    for c in range(n):
        matrix[r, c] = float(input("Matrix a[" + str(r + 1) + "][" + str(c + 1) + "] = "))
    vector[r] = float(input('Matrix b[' + str(r + 1) + ']: '))
tol = float(input("Jumlah Toleransi = "))
Itera = int(input("Jumlah Iterasi = "))
relaxation_factor = float(input("Faktor Relaksasi = "))

print("\n")

# Metode Gauss-Siedel Relaxation
k = 0
while k < Itera:
    k = k + 1
    for r in range(m):
        old_x = x.copy()
        suma = 0
        for c in range(n):
            if c != r:
                suma += matrix[r, c] * x[c]
        x[r] = (1 - relaxation_factor) * x[r] + (relaxation_factor / matrix[r, r]) * (vector[r] - suma)
        print("x[" + str(r) + "]: " + str(x[r]))
    del error[:]
    # Comprobación
    for r in range(m):
        suma = 0
        for c in range(n):
            suma = suma + matrix[r, c] * x[c]
        comp[r] = suma
        dif = abs(comp[r] - vector[r])
        error.append(dif)
        print("Error en[", r, "]:", error[r])
    print("Iterasi Ke-", k)
    if all(i <= tol for i in error):
        break
