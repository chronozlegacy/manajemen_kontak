import json
class Kontak:
    def __init__(self):
        self.kontak = []
    def membuka_kontak(self,path='kontak.txt'):
        with open(path, mode='r') as file:
            kontak = file.read()
        return json.loads(kontak)
    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}.{item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong")
            return 1
    def menambah_kontak(self):
        nama = input("Masukkan nama kontak yang baru : ")
        HP = input("Masukkan HP kontak yang baru : ")
        email = input("Masukkan email kontak yang baru : ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        self.menyimpan_kontak()
        print("Kontak baru berhasil ditambahkan")
    def menyimpan_kontak(self,filepath='kontak.txt'):
        with open(filepath, mode='w') as file:
            file.write(json.dumps(self.kontak))
        self.kontak = self.membuka_kontak()
    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
            del self.kontak[i_hapus - 1]
            self.menyimpan_kontak()
            self.kontak=self.membuka_kontak()
            print("Kontak yang dimaksud sudah dihapus")