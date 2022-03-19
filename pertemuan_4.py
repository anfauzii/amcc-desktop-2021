# Make class

"Membuat analogi class member AMCC yang memiliki"


class member_amcc():
    nama = None
    nim = None

x = member_amcc()
x.nama = "Ahmad Nur Fauzi"
x.nim = "21.11.4505"
print(x.nama, x.nim)

# buat kelas Mahasiswa
class Mahasiswa:
    nama  = None
    asal = None

    def perkenalan(self):
        print(f'Perkenalkan saya {self.nama} dari {self.asal}')

fauzi = Mahasiswa()
fauzi.nama = "Ahmad Nur Fauzi"
fauzi.asal = "Yogyakarta"

fauzi.perkenalan()

# CONSTRUCTOR
class Mahasiswa:
  def __init__(self, nama, asal):
    self.nama = nama
    self.asal = asal
  def perkenalan (self):
    print(f'Perkenalkan saya {self.nama} dari {self.asal}')

deni = Mahasiswa('Deni', 'Sulawesi')
fauzi = Mahasiswa(asal = 'Yogyakarta', nama = 'Ahmad Nur Fauzi')
deni.perkenalan()
fauzi.perkenalan()

# Atribut Kelas yang Merupakan Instance dari Kelas Lainnya
class Kucing:
  def __init__(self, warna, usia):
    self.warna = warna
    self.usia = usia
class Mahasiswa:
  def __init__(self, nama, asal, kucing):
    self.nama = nama
    self.asal = asal
    self.kucing = kucing
  def perkenalan(self):
    print(f'Perkenalkan saya {self.nama} dari {self.asal}')
    print(f'Saya memiliki kucing berwarna {self.kucing.warna} usia {self.kucing.usia}')

deni = Mahasiswa(
    nama='Fauzi',
    asal='Yogyakarta',
    kucing=Kucing(
        warna='Oren',
        usia='69 bulan'
    )
)
deni.perkenalan()

# METHOD
class Konversi:
  @staticmethod
  def satuan_ke_lusin(n):
    return n / 12

print(Konversi.satuan_ke_lusin(24))

print(Konversi.satuan_ke_lusin(36))


konverter = Konversi()
print(konverter.satuan_ke_lusin(42))

# CLASS METHOD
class Manusia:
  jumlah_tangan = 2 # class variable
  def __init__(self, nama):
    self.nama = nama # instance variable
  @classmethod
  def pengertian(cls):
    print(f'Manusia memilki {cls.jumlah_tangan} tangan')

# panggil secara langsung
Manusia.pengertian()
# panggil via objek
seseorang = Manusia('Tanpa Nama')
seseorang.pengertian()

# INHERITANCE (PEWARISAN)
class Orang:
  def __init__ (self, nama, asal):
    self.nama = nama
    self.asal = asal
  def perkenalan (self):
    print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')

andi = Orang('Andi', 'Surabaya')
andi.perkenalan()

# CHILD (OBJEK TURUNAN)
class Pelajar (Orang):
  pass
class Pekerja (Orang):
  pass

andi = Orang('Andi', 'Surabaya')
andi.perkenalan()
deni = Pelajar('Deni', 'Makassar')
deni.perkenalan()
budi = Pekerja('Budi', 'Pontianak')
budi.perkenalan()