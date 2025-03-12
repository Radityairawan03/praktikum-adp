nama = input("Nama Pembeli: ")

print("Pilih tontonan:")
print("Kode Film | Judul Film      | Total Harga")
print("---------------------------------------")
print("    1    | Captain Amerika  | Rp. 55000 ")
print("    2    | Keluarga Cemara  | Rp. 40000 ")
print("    3    | Agak Laen        | Rp. 50000 ")
print("    4    | Warkop DKI       | Rp. 45000 ")
print("    5    | Satria Dewa      | Rp. 65000 ")
print("---------------------------------------")

kode = int(input("Masukkan kode film: "))

if kode == 1:
    judul_film = "Captain Amerika"
    harga_tiket = 55000
elif kode == 2:
    judul_film = "Keluarga Cemara"
    harga_tiket = 40000
elif kode == 3:
    judul_film = "Agak Laen"
    harga_tiket = 50000
elif kode == 4:
    judul_film = "Warkop DKI"
    harga_tiket = 45000
elif kode == 5:
    judul_film = "Satria Dewa"
    harga_tiket = 65000
else:
    print("Kode film tidak valid.")
    

jumlah_tiket = int(input("Masukkan jumlah tiket: "))
harga_satuan = harga_tiket * jumlah_tiket

if harga_satuan > 250000:
    diskon = harga_satuan * 0.35
    print("Diskon 35% diberikan karena membeli lebih dari Rp. 250.000")
elif harga_satuan > 100000:
    diskon = harga_satuan * 0.15
    print("Diskon 15% diberikan karena membeli lebih dari Rp. 100.000")
else:
    diskon = 0

total_harga = harga_satuan - diskon

print("List Penonton:")
print("Nama Pembeli:", nama)
print("Judul Film:", judul_film)
print("Jumlah Tiket:", jumlah_tiket)
print("Harga Satuan: Rp.", harga_satuan)
print("Diskon: Rp.", diskon)
print("Total Harga: Rp.", total_harga)