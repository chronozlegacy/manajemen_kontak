"Program Manajemen Kontak"
import kontak
kontak_kantor = kontak.Kontak()
kontak_keluarga = kontak.Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua kontak")
    print("2. Menambah Kontak baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")
    pilihan=input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")
    if pilihan=='1':
        kontak_kantor.melihat_kontak()
    elif pilihan=='2':
        kontak_kantor.menambah_kontak()
    elif pilihan=='3':
        kontak_kantor.menghapus_kontak()
    elif pilihan=='4':
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
