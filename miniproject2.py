import os
os.system("cls")
from prettytable import PrettyTable

class Node:
    def __init__(self, nama_obat, dosis_obat, stok_obat, harga_obat, exp_date):
        self.next = None
        self.prev = None
        self.nama_obat = nama_obat
        self.dosis_obat = dosis_obat
        self.stok_obat = stok_obat
        self.harga_obat = harga_obat
        self.exp_date = exp_date

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, nama_obat, dosis_obat, stok_obat, harga_obat, exp_date, pos=None):
        node = Node(nama_obat, dosis_obat, stok_obat, harga_obat, exp_date)
        if pos is None:  # Jika posisi tidak ditentukan, tambahkan di akhir
            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.size += 1
        elif pos == 1:  # Jika posisi adalah 1, tambahkan di awal
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.size += 1
        elif 1 < pos <= self.size + 1:  # Jika posisi di tengah
            current = self.head
            for _ in range(1, pos - 1):
                if current is not None:
                    current = current.next
                else:
                    print("Posisi tidak valid.")
                    return
            node.next = current.next
            node.prev = current
            if current.next is not None:
                current.next.prev = node
            else:
                self.tail = node
            current.next = node
            self.size += 1
        else:
            print("Posisi tidak valid.")

    def remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.nama_obat == value:
                self.remove_node(node)
            node = node.next

    def display(self):
        tabel= PrettyTable(['nama_obat', 'dosis_obat', 'stok_obat', 'harga_obat', 'exp_date']) 
        head = self.head
        while head is not None:
            tabel.add_row([head.nama_obat, head.dosis_obat, head.stok_obat, head.harga_obat, head.exp_date])
            head = head.next
            
        print(tabel)

class historymasuk:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def add(self, nama_obat, dosis_obat, stok_obat, harga_obat, exp_date):
        node = Node(nama_obat, dosis_obat, stok_obat, harga_obat, exp_date)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def display2(self):
        if self.head is None:
            print("Linked list kosong")
        else:
            tabel= PrettyTable(['No','nama_obat', 'dosis_obat', 'stok_obat', 'harga_obat', 'exp_date']) 
            head = self.head
            x2 = 1
            while head is not None:
                tabel.add_row([x2, head.nama_obat, head.dosis_obat, head.stok_obat, head.harga_obat, head.exp_date])
                x2 += 1
                head = head.next    
        print(tabel)

history = historymasuk()
data = DoubleLinkedList()

while True:
    menu = int(input("""
    ====================================
    |      Program Pendataan Obat      |
    |       APOTEK MEDICAL FARMA       |                                    
    ====================================
    |       1. Tambah Data Obat        |
    |       2. Lihat Data obat         |
    |       3. Ubah Data Obat          |
    |       4. Hapus Data Obat         |
    |       5. Keluar                  |
    ======================================
        Masukan No. pilihan anda :  """))

    if menu == 1:
        ulang = "y"
        while ulang == "y":
            nama = str(input("Masukan nama obat : "))
            dosis = str(input("Masukan dosis : "))
            stok = int(input("Masukan stok : "))
            harga = int(input("Masukan harga: "))
            exp = input("Masukan exp date (DD/MM/YYYY): ")
            posisi = input("Masukkan posisi (1/2) & tekan enter untuk tambah data di akhir: ") #tekan enter agar data ditambah di akhir
            if posisi == '':
                posisi = None
            else:
                posisi = int(posisi)
            data.add(nama, dosis, stok, harga, exp, posisi)
            history.add(nama, dosis, stok, harga, exp)
            data.display()
            ulang = input("Apakah anda ingin memasukan data lagi (y/n) : ")
            if ulang == "n":
                break
    elif menu == 2:
        ulang = "y"
        while ulang == "y":
            data.display()
            ulang = input("Apakah anda ingin menampilkan data lagi (y/n) : ")
            if ulang == "n":
                break
    elif menu == 3:
        ulang = "y"
        while ulang == "y":
            os.system('cls')
            print(" Pastikan Anda Telah Menambahkan Data Sebelumnya Jika Ingin Melihat Data terbaru")
            print('''
        ===================================
        |          Menu Update Data       |
        ===================================
        |   1. Update Nama Obat           |
        |   2. Kembali ke Menu Utama      |
        ===================================
            ''')
            inputupdate = input("Masukkan Menu : ")
            os.system("cls")
            if inputupdate == "1":
                nama_obat_lama = input("Masukkan nama obat yang ingin diubah: ")
                nama_obat_baru = input("Masukkan nama obat baru: ")
                current = data.head
                while current:
                    if current.nama_obat == nama_obat_lama:
                        current.nama_obat = nama_obat_baru
                        print("Nama obat berhasil diperbarui.")
                        break
                    current = current.next
                else:
                    print("Obat tidak ditemukan.")
            elif inputupdate == "2":
                os.system('cls')
                break
            else:
                print('Input Salah')
                os.system('cls')
                ulang = input("Apakah anda ingin mengulang menu tersebut lagi (y/n) : ")
                if ulang == "n":
                    break
    elif menu == 4:
        ulang = "y"
        while ulang == "y":
            hapus = input("Masukan nama obat yang ingin dihapus : ")
            data.remove(hapus)
            data.display()
            ulang = input("Apakah anda ingin menghapus data lagi (y/n) : ")
            if ulang == "n":
                break
    
    elif menu == 5:
        print("Anda telah keluar dari program")
        break
        
    
    