def hitung_persamaan_relaksasi(A, b, x1, x2, omega):
    list_hasil = []
    hasil_1 = (b[0] + ((-1 * A[0][1]) * x2)) / A[0][0]
    hasil_1_relaksasi = omega * hasil_1 + (1 - omega) * x1

    hasil_2 = (b[1] + ((-1 * A[1][0]) * hasil_1_relaksasi)) / A[1][1]
    hasil_2_relaksasi = omega * hasil_2 + (1 - omega) * x2

    list_hasil.append(hasil_1_relaksasi)
    list_hasil.append(hasil_2_relaksasi)

    return list_hasil


def hitung_error(list):
    list_error = []

    error_1 = "{:.5f}".format(abs((list[len(list) - 1][0] - list[len(list) - 2][0]) / list[len(list) - 1][0]) * 100)
    error_2 = "{:.5f}".format(abs((list[len(list) - 1][1] - list[len(list) - 2][1]) / list[len(list) - 1][1]) * 100)

    list_error.append(error_1)
    list_error.append(error_2)
    return list_error


def gauss_seidel_relaksasi(A, b, jmlIterasi, omega):
    list_x = []
    temp_x = []
    temp_error = []

    for i in range(jmlIterasi):
        if i == 0:
            x_1 = 0
            x_2 = 0
            list_x = hitung_persamaan_relaksasi(A, b, x_1, x_2, omega)
            temp_x.append(list_x)
        else:
            x_1 = list_x[0]
            x_2 = list_x[1]
            list_x = hitung_persamaan_relaksasi(A, b, x_1, x_2, omega)
            temp_x.append(list_x)

        error_rate = hitung_error(temp_x)
        temp_error.append(error_rate)

    return temp_x, temp_error


# Membaca ukuran matriks A dari input pengguna
n = int(input("Masukkan ukuran matriks A: "))

# Membaca elemen-elemen matriks A dari input pengguna
A = []
print("Inputkan Terbalik")
print("Masukkan elemen-elemen matriks A:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Membaca elemen-elemen vektor b dari input pengguna
b = list(map(float, input("Masukkan elemen-elemen vektor b: ").split()))

# Membaca jumlah iterasi dari input
jumlahIterasi = int(input("Masukkan jumlah iterasi: "))

# Membaca faktor relaksasi (omega) dari input
omega = float(input("Masukkan faktor relaksasi (omega): "))

# Memanggil fungsi gauss_seidel_relaksasi
list_x, list_error = gauss_seidel_relaksasi(A, b, jumlahIterasi, omega)

for i in range(jumlahIterasi):
    print('Iterasi', i + 1)
    print('===========================')
    print('x1 =', list_x[i][0])
    print('x2 =', list_x[i][1])
    print('---------------------------')
    print('Error Rate')
    print('---------------------------')
    print('x1 =', list_error[i][0])
    print('x2 =', list_error[i][1])
    print('===========================\n')

