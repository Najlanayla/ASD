import os
from prettytable import PrettyTable
from datetime import datetime

class Obat:
    def __init__(self, nama_obat, dosis_obat, stok_obat, harga_obat, exp_date):
        self.nama_obat = nama_obat
        self.dosis_obat = dosis_obat
        self.stok_obat = stok_obat
        self.harga_obat = harga_obat
        self.exp_date = exp_date

class Data_Apotek:
    def __init__(self):
        self.daftar_obat = {}

    def tambah_obat(self, obat):
        if obat.nama_obat not in self.daftar_obat:
            self.daftar_obat[obat.nama_obat] = obat
            print(f"Obat {obat.nama_obat} berhasil ditambahkan")
        else:
            print(f"Obat {obat.nama_obat} sudah terdaftar")

    def tampil_data_obat(self):
        table = PrettyTable(["Nama Obat", "Dosis Obat", "Stok Obat", "Harga Obat", "EXP Date"])
        for obat in self.daftar_obat.values():
            table.add_row([obat.nama_obat, obat.dosis_obat, obat.stok_obat, obat.harga_obat, obat.exp_date])
        print(table)

    def ubah_obat(self, nama_obat, field, new_value):
        if nama_obat in self.daftar_obat:
            obat = self.daftar_obat[nama_obat]
            if hasattr(obat, field):
                setattr(obat, field, new_value)
                print(f"Data obat {nama_obat} berhasil diperbarui")
            else:
                print(f"Field {field} tidak valid")
        else:
            print(f"Obat {nama_obat} tidak ditemukan")

    def hapus_obat(self, nama_obat):
        if nama_obat in self.daftar_obat:
            del self.daftar_obat[nama_obat]
            print(f"Obat {nama_obat} berhasil dihapus")
        else:
            print(f"Obat {nama_obat} tidak ditemukan")

# List data obat
daftar_obat = [
    Obat("Vitamin C", "50 mg", 50, 8000, "31/03/2025"),
    Obat("Panadol", "10 mg", 50, 10000, "12/12/2026"),
    Obat("Paracetamol", "50 mg", 100, 5000, "30/06/2024"),
    Obat("Amoxicillin", "30 mg", 20, 10000, "31/12/2024")
]

# Buat objek apotek
Sistem_Apotek = Data_Apotek()

# Tampilkan pesan selamat datang
print("=============================================")
print(" |   SELAMAT DATANG DIPROGRAM PENDATAAN    |")
print(" |        OBAT APOTEK MEDICAL FARMA        |")
print("=============================================")

# Looping program
while True:
    print("1. Tampilkan Data Obat")
    print("2. Tambah Data Obat")
    print("3. Ubah Data Obat")
    print("4. Hapus Data Obat")
    print("5. Keluar")

    pilihan = int(input("Masukkan angka pilihan: "))

    if pilihan == 1:
        Sistem_Apotek.tampil_data_obat()
    elif pilihan == 2:
        nama_obat = input("Masukkan nama obat: ")
        dosis_obat = input("Masukkan dosis obat: ")
        try:
            stok_obat = int(input("Masukkan stok obat: "))
            harga_obat = int(input("Masukkan harga obat: "))
        except ValueError:
            print("Stok dan harga obat harus berupa angka.")
            continue
        exp_date = input("Masukkan EXP Date (DD/MM/YYYY): ")
        obat = Obat(nama_obat, dosis_obat, stok_obat, harga_obat, exp_date)
        Sistem_Apotek.tambah_obat(obat)
    elif pilihan == 3:
        nama_obat = input("Masukkan nama obat yang ingin diubah: ")
        if nama_obat in Sistem_Apotek.daftar_obat:
            field = input("Masukkan data yang ingin diubah: ")
            if field in ["nama_obat", "dosis_obat", "stok_obat", "harga_obat", "exp_date"]:
                new_value = input("Masukkan nilai baru: ")
                Sistem_Apotek.ubah_obat(nama_obat, field, new_value)
            else:
                print(f"Field {field} tidak valid")
        else:
            print(f"Obat {nama_obat} tidak ditemukan")
    elif pilihan == 4:
        nama_obat = input("Masukkan nama obat yang ingin dihapus: ")
        Sistem_Apotek.hapus_obat(nama_obat)
    elif pilihan == 5:
        print("Terima kasih dan Sampai Jumpa!")
        break
    else:
        print("Pilihan tidak valid!")

