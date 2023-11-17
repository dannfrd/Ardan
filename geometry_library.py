import math

def volume_balok(panjang, lebar, tinggi):
    """Menghitung volume balok."""
    return panjang * lebar * tinggi

def luas_permukaan_balok(panjang, lebar, tinggi):
    """Menghitung luas permukaan balok."""
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def volume_bola(jari_jari):
    """Menghitung volume bola."""
    return (4/3) * math.pi * jari_jari**3

def luas_permukaan_bola(jari_jari):
    """Menghitung luas permukaan bola."""
    return 4 * math.pi * jari_jari**2

def volume_tabung(jari_jari, tinggi):
    """Menghitung volume tabung."""
    return math.pi * jari_jari**2 * tinggi

def luas_permukaan_tabung(jari_jari, tinggi):
    """Menghitung luas permukaan tabung."""
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

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
