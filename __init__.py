from geometry_library import volume_balok, luas_permukaan_balok, volume_bola, luas_permukaan_bola, volume_tabung, luas_permukaan_tabung

# Contoh penggunaan
# Menghitung volume dan luas permukaan balok
vol_balok = volume_balok(3, 4, 5)
luas_balok = luas_permukaan_balok(3, 4, 5)
print(f"Volume Balok: {vol_balok}")
print(f"Luas Permukaan Balok: {luas_balok}")

# Menghitung volume dan luas permukaan bola
vol_bola = volume_bola(2)
luas_bola = luas_permukaan_bola(2)
print(f"Volume Bola: {vol_bola}")
print(f"Luas Permukaan Bola: {luas_bola}")

# Menghitung volume dan luas permukaan tabung
vol_tabung = volume_tabung(3, 6)
luas_tabung = luas_permukaan_tabung(3, 6)
print(f"Volume Tabung: {vol_tabung}")
print(f"Luas Permukaan Tabung: {luas_tabung}")
