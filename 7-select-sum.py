import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
# Ambil data berdasarkan rata-rata gaji AVG()
kursor.execute("SELECT SUM(jml_skrg) FROM FAUNA")
total = kursor.fetchone()[0] #ambil data gaji jadikan baris baru

print(f"Total populasi : {total}")

koneksi.close()