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

    def quickSortNama(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next
        while current is not None:
            next_node = current.next
            if current.nama_obat < pivot.nama_obat:
                current.next = smaller_head
                smaller_head = current
            elif current.nama_obat == pivot.nama_obat:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node
        smaller_head = self.quickSortNama(smaller_head)
        larger_head = self.quickSortNama(larger_head)
        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head
        pivot.next = larger_head if larger_head is not None else None
        return smaller_head

    def sortAscendingNama(self):
        self.head = self.quickSortNama(self.head)

    def sortDescendingNama(self):
        self.sortAscendingNama()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def quickSortHarga(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next
        while current is not None:
            next_node = current.next
            if current.harga_obat < pivot.harga_obat:
                current.next = smaller_head
                smaller_head = current
            elif current.harga_obat == pivot.harga_obat:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node
        smaller_head = self.quickSortHarga(smaller_head)
        larger_head = self.quickSortHarga(larger_head)
        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head
        pivot.next = larger_head if larger_head is not None else None
        return smaller_head

    def sortAscendingHarga(self):
        self.head = self.quickSortHarga(self.head)

    def sortDescendingHarga(self):
        self.sortAscendingHarga()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def add(self, nama_obat, dosis_obat, stok_obat, harga_obat, exp_date, posisi=None):
        node = Node(nama_obat, dosis_obat, stok_obat, harga_obat, exp_date)
        if posisi is None:  
            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.size += 1
        elif posisi == 1:  
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.size += 1
        elif 1 < posisi <= self.size + 1:  
            current = self.head
            for _ in range(1, posisi - 1):
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
        tabel = PrettyTable(['nama_obat', 'dosis_obat', 'stok_obat', 'harga_obat', 'exp_date']) 
        head = self.head
        while head is not None:
            tabel.add_row([head.nama_obat, head.dosis_obat, head.stok_obat, head.harga_obat, head.exp_date])
            head = head.next
        print(tabel)

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
|       5. Urut Data Obat          |
|       6. Keluar                  |
====================================
    Masukan pilihan (1/2/3/4/5/6):  """))

    if menu == 1:
        ulang = "y"
        while ulang == "y":
            nama = str(input("Masukan nama obat : "))
            dosis = str(input("Masukan dosis : "))
            stok = int(input("Masukan stok : "))
            harga = int(input("Masukan harga: "))
            exp = input("Masukan exp date (DD/MM/YYYY): ")
            posisi = input("Masukkan posisi (1/2) & tekan enter untuk tambah data di akhir: ")
            if posisi == '':
                posisi = None
            else:
                posisi = int(posisi)
            data.add(nama, dosis, stok, harga, exp, posisi)
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
            print(" Pastikan Anda Telah Menambahkan Data Sebelumnya Jika Ingin Ubah Data")
            print('''
===================================
|          Menu Update Data       |
===================================
|   1. Ubah Nama Obat            |
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
        print("""
=================================
|       Urutkan Data Obat       |
=================================""")  
        print("  [1] Urutkan berdasarkan harga termurah")
        print("  [2] Urutkan berdasarkan harga termahal")
        print("  [3] Urutkan berdasarkan nama obat A-Z")
        print("  [4] Urutkan berdasarkan nama obat Z-A")

        pilih = input("  Masukkan pilihan (1/2/3/4): ")

        if pilih == "1":
            data.sortAscendingHarga()
            print("  > Data obat berhasil diurutkan berdasarkan harga termurah")
        elif pilih == "2":
            data.sortDescendingHarga()
            print("  > Data obat berhasil diurutkan berdasarkan harga termahal")
        elif pilih == "3":
            data.sortAscendingNama()
            print("  > Data obat berhasil diurutkan berdasarkan nama obat A-Z")
        elif pilih == "4":
            data.sortDescendingNama()
            print("  > Data obat berhasil diurutkan berdasarkan nama obat Z-A")
        else:
            print("  > Pilihan tidak valid. Silakan pilih kembali.")

    elif menu == 6:
        print("Anda telah keluar dari program!! Bye Bye")
        break
    else: 
        print("Input tidak valid")
