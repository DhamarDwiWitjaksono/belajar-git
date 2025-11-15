class Siswa():
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def sapa(self):
        print(f"Hallo! nama saya {self.nama}")
        print(f"Umur saya {self.umur}")