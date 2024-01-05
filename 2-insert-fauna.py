import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
#insert data ke tabel

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Harimau Jawa', 'Mamalia', 'Jawa', '40', '2019')
                ''')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Kuskus Beruang', 'Mamalia', 'Sulawesi', '30', '2021')
                ''')


koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Beruang Madu', 'Mamalia', 'Sumetera', '1000', '2020')
                ''')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Pesut Mahakam', 'Mamalia', 'Klimantan', '100', '2021')
                ''')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Burung Maleo', 'Burung', 'Sulawesi', '7000', '2023')
                ''')


koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Dahlan Macan', 'Mamalia', 'Sumatera', '400', '2020')
                ''')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Kancil', 'Mamalia', 'Jawa', '60', '2022')
                ''')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
                ''')

koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Elang Jawa', 'Burung', 'Jawa', '200', '2021')
                ''')


koneksi.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrg,
                thn_ditemukan)
                VALUES('Katak Borneo', 'Amfibi', 'Kalimantan', '2000', '2023')
                ''')


koneksi.commit()
koneksi.close()
