#UPDATE
# SET colum1 = Value, column2 = value2, ...
# WHERE condition;
import sqlite3

#membuat koneksi ke database atau mambuat database baru jika belum ada
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# data yang ingin di ubah

# menjalankan query UPDATE
kursor.execute(f"UPDATE FAUNA SET asal = 'kalimantan Timur' WHERE nama_fauna = 'Pesut Mahakam'")
koneksi.commit()

# menampilkan pesan setelah update berhasil
if kursor.rowcount > 0:
    print(f"Data fauna berhasil diupdate.")
else :
    print(f"tidak ada data fauna")

#putuskan koneksi
koneksi.close
