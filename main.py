"Program Manajemen Kontak"

def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}.{item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong")
        return 1
def menambah_kontak():
    nama = input("Masukkan nama kontak yang baru : ")
    HP = input("Masukkan HP kontak yang baru : ")
    email = input("Masukkan email kontak yang baru : ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan")
def menghapus_kontak():
    if(melihat_kontak()==1):
        return
    else:
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimaksud sudah dihapus")

kontak1={'nama':'Andi','HP':'109989303','email':'Andi@python.com'}
kontak2={'nama':'Ani','HP':'933953335','email':'Ani@python.com'}
kontak=[kontak1,kontak2]

print("\nMenu Kontak")
print("1. Melihat Semua kontak")
print("2. Menambah Kontak baru")
print("3. Menghapus Kontak")
print("4. Keluar dari Kontak")

while True:
    pilihan=input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")
    if pilihan=='1':
        melihat_kontak()
    elif pilihan=='2':
        menambah_kontak()
    elif pilihan=='3':
        menghapus_kontak()
    elif pilihan=='4':
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
