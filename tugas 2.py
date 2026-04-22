# # P#pogram Tabel Perkalian

# Langkah 1: Meminta nama pendek
nama = input("Masukkan nama anda : ")

# Langkah 2: Validasi nama (sederhana: tidak boleh kosong)
if nama.strip() == "":
    print("silahkan coba lagi")
else:
    # Langkah 3: Meminta angka dari user
    angka = int(input("Masukkan angka: "))
    
    # Langkah 4: Menampilkan tabel perkalian 1 sampai 10
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")