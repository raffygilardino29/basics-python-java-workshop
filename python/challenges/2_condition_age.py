# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
umur = int(input("masukan umur anda : "))
# 2. TODO Tentukan kategori berdasarkan usia
keterangan = ""
if umur <= 12:
    keterangan = "anak - anak"
elif umur <= 20:
    keterangan = "remaja"
elif umur <= 30:
    keterangan = "dewasa"
else:
    keterangan = "bau tanah"

print(keterangan)