"""
Menyeberangi Jembatan Gantung

Setelah membantu penduduk dengan makanan, mereka mengizinkanmu melintasi jembatan gantung. 
Namun, jembatan ini sangat rapuh. Hanya orang-orang dengan berat badan tertentu yang boleh menyeberang. 
Kamu harus menulis program untuk menentukan apakah kamu bisa menyeberang jembatan.

Contoh 1
Input:
weight = 50

Output:
Kamu tidak boleh menyeberang jembatan

Contoh 2
Input:
weight = 90

Output:
Kamu boleh menyeberang jembatan
"""
weight = 90
# lanjutkan code dibawah ini
# Meminta input berat badan
weight = int(input("Masukkan berat badan: "))

# Menentukan batas berat untuk menyeberang
batas_berat = 75

# Memeriksa apakah berat badan memenuhi syarat
if weight >= batas_berat:
    print("Kamu boleh menyeberang jembatan")
else:
    print("Kamu tidak boleh menyeberang jembatan")
