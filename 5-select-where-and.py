import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
# select all data pegawai

kursor = koneksi.cursor()
# mengambil semua data dalam tabel dan tampilkan
kursor.execute("SELECT *FROM FAUNA WHERE Jml_Skrg <= '1000' ")
# TAMPILKAN DALAM BENTUK GARIS
baris_tabel = kursor.fetchall()

#membuat format table dengan menthod format()
print("Tabel Fauna")
print("="*100)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} ".format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jml_Skrg", "Thn_Skrg"))
print("="*100)
# tampilkan data sesuai format tabel dgn perulangan
for baris in baris_tabel:
    print("{:<10} {:<20} {:<20} {:<20} {:20}".format(baris[0], baris[1], baris[2], baris[3], baris[4]))

koneksi.close()