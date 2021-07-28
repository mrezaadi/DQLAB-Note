class Burung:
    def __init__(self, nama):
        self.nama = nama
    def fly(self):
        print(nama + ' sedang terbang')

class Ayam(Burung):
    def fly(self):
        print(self.nama + ' tidak bisa terbang')

anak_ayam = Ayam('Si Jago') #Langsung menginisialisasikan class burung, dengan nama 'Si Jago'
anak_ayam.fly()

class Mamalia:
    def __init__(self, nama):
        self.__nama = nama
    def interaksi(self):
        print('Bersuara')

class Anjing(Mamalia):
    def interaksi(self):
        print('Guk')

class Manusia(Mamalia):
    pass #menerima secara utuh parent classnya telah menggunakan keyword pass.

blacky = Anjing('Blacky')
toni = Manusia('Toni')
toni.interaksi()
blacky.interaksi()