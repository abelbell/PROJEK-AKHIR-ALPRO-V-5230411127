import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

koneksi.execute('''
              CREATE TABLE FAUNA(
                id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VACHAR(50),
                jml_skrg INT(10),
                thn_ditemukan INT(10)
            )
             ''')
koneksi.close()