# Program Tabel Perkalian dengan Validasi Positif

# Langkah 1: Meminta nama pendek
nama = input("Masukkan nama anda : ")

# Langkah 2: Validasi nama
if nama.strip() == "":
    print("silahkan coba lagi")
else:
    # Langkah 3: Meminta angka dengan validasi
    while True:
        angka = int(input("Masukkan angka: "))
        
        if angka > 0:
            # Jika angka positif, keluar dari loop
            break
        else:
            # Jika angka negatif atau nol, tampilkan pesan dan ulangi
            print("Harus positif!")
    
    # Langkah 4: Menampilkan tabel perkalian
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")