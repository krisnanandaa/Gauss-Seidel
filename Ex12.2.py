import numpy as np

m = int(input('Nilai m = '))  # Baris
n = int(input('Nilai n = '))  # Kolom
matrix = np.zeros((m, n))
x = np.zeros(m)

vector = np.zeros(m, dtype=float)
comp = np.zeros(m, dtype=float)
error = np.zeros(m, dtype=float)

print("Metode Gauss-Seidel dengan Relaksasi")
print('Memasukan Matrix Koefisien Dan Vektor Solusi')
for r in range(m):
    for c in range(n):
        matrix[r, c] = float(input(f"Matrix a[{r + 1}{c + 1}] = "))
    vector[r] = float(input(f"Matrix b[{r + 1}]: "))
tol = float(input("Jumlah Toleransi = "))
Itera = int(input("Jumlah Iterasi = "))
omega = float(input("Nilai omega (relaksasi) = "))

print("\n")

# Metode Gauss-Seidel dengan Relaksasi
k = 0
while k < Itera:
    k += 1
    for r in range(m):
        suma = 0
        for c in range(n):
            if c != r:
                suma += matrix[r, c] * x[c]
        x_new = (vector[r] - suma) / matrix[r, r]
        x_new = omega * x_new + (1 - omega) * x[r]  # Menggunakan relaksasi
        error[r] = abs(x_new - x[r])
        x[r] = x_new
        print(f"x[{r}]: {x[r]}")
    
    # Perhitungan error per variabel x
    error_rate = [err / abs(x_val) * 100 if abs(x_val) != 0 else 0 for err, x_val in zip(error, x)]
    print("Error Rate per x:")
    for idx, err_rate in enumerate(error_rate):
        print(f"x[{idx}]: {err_rate}%")
    
    error_max = np.max(error)
    print("Error: ", error_max)
    
    if error_max <= tol:
        break
    print("Iterasi Ke-", k)
