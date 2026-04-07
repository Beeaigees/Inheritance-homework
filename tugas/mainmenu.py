from module_tugas.transaksiPOS import transaksi_pos

print("="*40)
print("\tSISTEM KASIR RESTORAN OOP")
print("="*40)

nama = input("Nama Pelanggan : ")
meja = int(input("Nomor Meja     : "))

transaksi = transaksi_pos(nama, meja)

while True:
    print("--- Input Pesanan ---")
    nama_menu = input("Nama Makanan ( atau ketik 'selesai'): ")

    if nama_menu.lower() == "selesai":
        break

    harga = float(input("Harga Satuan: "))
    jumlah = int(input("Jumlah     : "))

    transaksi.tambah_item(nama_menu, harga, jumlah)

transaksi.proses_pembayaran()