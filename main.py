# Percabangan / Pengkondisian

# if statment

umur_budi = 20
umur_andi = 25

if umur_budi < umur_andi:
    print("Lebih tua Andi ")

# a = 12
# b = 12
#
# if a > b :
#     print('Variabel a lebih besar dari variabel b')
# if a < b :
#     print('Variabel a lebih kecil dari variabel b')
# if a == b :
#     print('Variabel a sama dengan variabel b')

i = 8

if (i % 2) == 0:
    print('Hasilnya Genap')
if(i% 2 ) == 1:
    print('HAsilnya Ganjil')

# if else statment

if (i % 2) == 1:
    print('Hasilnya Adalah Ganjil')
else:
    print('HAsilnya Genap')

nilai = 65

if nilai > 70:
    print("Selamat Anda Lulus")
else :
    print('Anda Tidak Lulus')

j = 200
k = 33

if k > j :
    print('K lebih besar dari j')
elif j == k :
    print('J sama dengan K')
else:
    print('J lebih besar dari K')

# if else diletakkan sebelum output/ ditengah
nilai_a = 15
nilai_b = 20

print("A") if nilai_a < nilai_b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 30
c = 500
if a > b and c > a:
    print('Kondisi ini terpenuhi')
if a > b or a > c:
    print("At least one of the conditions is True")

nilai = 'D'

if nilai == 'A':
    print('Pertahankan')
elif nilai == 'B':
    print('Harus Lebih Baik Lagi')
elif nilai == 'C':
    print('Perbanyak Belajar Lagi')
elif nilai == 'D':
    print('Jangan Keseringan Main Game')
elif nilai == 'E':
    print('Kebanyakan Bolos...')
else:
    print('Maaf, format tidak sesuai')

nilai = 20
print('Nilai', nilai)

if nilai >= 90:
  print('Pertahankan')
elif (nilai >= 80) and (nilai < 90):
  print('Harus lebih baik lagi')
elif (nilai >= 60) and (nilai < 80):
  print('Perbanyak belajar')
elif (nilai >= 40) and (nilai < 60):
  print('Jangan keseringan main')
elif nilai < 40:
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')