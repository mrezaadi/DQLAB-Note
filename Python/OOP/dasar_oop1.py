# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
# Inisiasi object yang dinyatakan dalam variabel aksara dan senja
aksara = Karyawan()
senja = Karyawan()
# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print("<<<<<<<<< PERBEDAAN AKSES MENGGUNAKAN __class__ dan TIDAK <<<<<<<<<")
print("Aksara dengan __class__ :",aksara.__class__.nama_perusahaan) #Akses dalam scope class
print("Senja tanpa __class__:", senja.nama_perusahaan,"\n") #Akses diluar scope class

# Ubah nama_perusahaan menjadi 'DEF'
print("<<<<<<<<< UBAH ATRIBUT KELAS TANPA MENGGUNAKAN __class__ <<<<<<<<<")
aksara.nama_perusahaan = 'DEF'
print("Print dengan __class__:",aksara.__class__.nama_perusahaan) #Walaupun sudah diubah diatasnya, tetapo jika menggunakan keyword __class__, yang dimunculkan merupakan default nama perusahaan yang ada di class Karyawan
print("Print tanpa __class__:",aksara.nama_perusahaan,"\n")

print("<<<<<<<<< UBAH ATRIBUT MENGGUNAKAN __class__ <<<<<<<<<")
senja.__class__.nama_perusahaan = "BARU"
print("Senja dengan __class__:",senja.__class__.nama_perusahaan)
print("Senja tanpa __class__:",senja.nama_perusahaan,"\n")
print("Kesimpulan : Jika menggunaka __class__ yang diubah semuanya")
