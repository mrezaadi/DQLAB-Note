# Definisikan class Karyawan
class Karyawan: #Class attribute, properti/atribut yang bernilai sama untuk oleh seluruh objek 
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan): #Instance variable,  properti/atribut yang nilainya berbeda-beda untuk setiap objek dari sebuah class.
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
# Buat object bernama aksara dan senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
# Cetak objek bernama aksara
print(aksara.nama + ', Usia: ' + str(aksara.usia) + ', Pendapatan ' + str(aksara.pendapatan))
# Cetak objek bernama senja
print(senja.nama + ', Usia: ' + str(senja.usia) + ', Pendapatan ' + str(senja.pendapatan))