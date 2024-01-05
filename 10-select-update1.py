#UPDATE
# SET colum1 = Value, column2 = value2, ...
# WHERE condition;
import sqlite3

#membuat koneksi ke database atau mambuat database baru jika belum ada
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# menjalankan query UPDATE
kursor.execute(f"UPDATE FAUNA SET  jml_skrg = '650' WHERE nama_fauna = 'Katak Borneo' ")
koneksi.commit()

# menampilkan pesan setelah update berhasil
if kursor.rowcount > 0:
    print(f"Data fauna berhasil diubah.")
else :
    print(f"tidak ada data fauna.")

#menutup koneksi
koneksi.close
