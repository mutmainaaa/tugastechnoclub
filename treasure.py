"""
Mengungkap Pesan Tersembunyi

Di akhir petualangan, kamu menemukan kotak harta karun. 
Namun, untuk membukanya, kamu harus menemukan pesan tersembunyi di antara serangkaian kata. 
Penduduk Pulau Python memberimu sebuah daftar kata, dan kamu harus mencari kata yang paling sering muncul.

Contoh Input:
["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan"]

Contoh Output:
Kata yang paling sering muncul adalah "harta"
"""
arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]
# lanjutkan code dibawah ini

# Menghitung frekuensi setiap kata
from collections import Counter
frekuensi = Counter(arr)

# Mencari kata yang paling sering muncul
kata_tersering = frekuensi.most_common(1)[0][0]

# Menampilkan hasil
print(f'Kata yang paling sering muncul adalah "{kata_tersering}"')
