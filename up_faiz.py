# pengelolaan stok barang 

print ("=====================================")
print ("    SITEM PENGOLAAN STOK BARANG")
print ("=====================================")

# input data barang
nama_bang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

# perulangan transaksi
while True:
    print("\n======================================")
    print("             MENU TRANSAKSI")
    print("======================================")
    print("1. Barang masuk")
    print("2. Barang keluar")
    print("3. Tampilkan stok")
    print("4. Selesai")

    pilihan = input("Pilih transaksi (1-4): ")

    # proses transaksi 
    if pilihan == "1":
        jumlah = int(input("masukkan jumlah barang masuk: "))

        if jumlah > 0:
            stok += jumlah
            print("Barang berhasil ditambahkan!")
        else:
            print("Jumlah barang harus lebih dari 0!:")

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah barang keluar: "))

        # cek ketersediaan stok
        if jumlah <= 0:
            print("Jumlah barang harus lebih dari nol 0!")
        elif jumlah <= stok:
            stok -= jumlah
            print ("Barang berhasil dikeluarkan!")
        else:
            print("Stok tidak mencukupi!")

    elif pilihan == "3":
        print("\nNama Barang :", nama_bang)
        print("Stok Tersedia:", stok)

    elif pilihan == "4":
        print("\n========================================")
        print("        TRANSAKSI SELESAI")
        print("========================================")
        print("Nama barang  :", nama_barang)
        print("Stok akhir   :", stok)
        print("Terimakasih!")
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi.")