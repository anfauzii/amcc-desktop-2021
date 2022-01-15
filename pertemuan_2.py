# komentar
"""
Baris 1
Baris 2
Baris 3
"""

a= 'Selamat Datang' # String
b= 123
c= 3.14
d= False


# OPERATOR PERBANDINGAN

# + - penjumlahan
# - - pengurangan
# * - perkalian
# / - pembagian
# % - sisa hasil bagi
# ** - pangkat
# // - pembagian bulat

a = 5
b = 3

# penjumlahan
hasil = a + b
print("5 + 3 = ", hasil)

# pengurangan
hasil = a - b
print("5 - 3 = ", hasil)

# perkalian
hasil = a * b
print("5 * 3 = ", hasil)

# pembagian
hasil = a / b
print("5 / 3 = ", hasil)

# sisa hasil bagi
hasil = a % b
print("5 % 3 = ", hasil)

# pangkat
hasil = a ** b
print("5 ** 3 = ", hasil)

# pembagian bulat
hasil = a // b
print("5 // 3 = ", hasil)


# OPERATOR PERBANDINGAN

# == - sama dengan
# != - tidak sama dengan
# <> - tidak sama dengan
# > - lebih besar dari
# < - kurang dari
# >= - lebih besar sama dengan
# <= - kurang dari sama dengan

a = 1
b = 2

# == - sama dengan
hasil = a == b
print(a, " == ", b, " = ", hasil)

# != - tidak sama dengan
hasil = a != b
print(a, " != ", b, " = ", hasil)

# > - lebih besar dari
hasil = a > b
print(a, " > ", b, " = ", hasil)

# < - kurang dari
hasil = a < b
print(a, " < ", b, " = ", hasil)

# >= - lebih besar sama dengan
hasil = a >= b
print(a, " >= ", b, " = ", hasil)

# <= - kurang dari sama dengan
hasil = a <= b
print(a, " <= ", b, " = ", hasil)


# OPERATOR PENUGASAN

# a = 1 - memberikan / memasukan nilai ke variable
# a += 1 - # ditambah sesuai nilai variable itu sendiri
# a -= 1 - # dikurang sesuai nilai variable itu sendiri
# a *= 1 - # dikali sesuai nilai variable itu sendiri
# a /= 1 - # dibagi sesuai nilai variable itu sendiri
# a %= 1 - # sisa hasil bagi sesuai nilai variable itu sendiri
# a **= 1 - # dipangkat sesuai nilai variable itu sendiri
# a //= 1 = # dibagi bulat sesuai nilai variable itu sendiri


# OPERATOR LOGICAL

# and
hasil = (5 > 6) and (10 <= 8)
print(hasil)

#or
hasil = ('amcc' == 'amcc') or (10 <= 8)
print(hasil)

# not
hasil = not(10 < 10)
print(hasil)


# OPERATOR IDENTITAS

a = 5
b = 5

# output True
print('a is b:', a is b)

# output False
print('a is not b:', a is not b)


# STRUKTUR PERCABANGAN

# if
Diterima = 'No'
if Diterima == 'No':
    print('Sudah Jangan Sedih Yah')

# if else
jumlah = int(input('Berapa Jumlah Doi Kamu?: '))
if jumlah >= 4 :
    print ('Kamu Fucekboy ah')
else:
    print ('Gini Dong Setia')

# if elif else
nilai = int(input('Berapa Nilai Kamu?: '))
if nilai >= 81 :
    Grade = 'A'
elif nilai >= 61 :
    Grade = 'B'
elif nilai >= 51 :
    Grade = 'C'
elif nilai >= 41 :
    Grade = 'D'
else:
    Grade = 'E'
print ('Grade = ', Grade)


# STRUKTUR PERULANGAN

# perulangan for
ulang = int(input('Berapa kali diulang?: '))
for i in range(ulang):
    print('perulangan ke-'+str(i+1))

buah = ['jeruk', 'mangga', 'semangka']
for x in buah:
    print(x)

# perulangan while
jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input('Ulang lagi tidak?: ')
    
print('Total perulangan: '+str(hitung))