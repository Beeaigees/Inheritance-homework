from module_tugas.pajakPPN import pajak_ppn

class transaksi_pos(pajak_ppn):
    def __init__(self, pelanggan, meja):
        super().__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftar_pesanan = []

    def hitung_total(self):
        self.nilaipajak = self.subtotal * 0.1 #Subtotal tadi itu nanti kita kalikan 0.1 buat pajak
        self.total_akhir = self.subtotal + self.nilaipajak #Abis itu total akhirnya nanti si subtotal ditambah sama subtotal yang udah ditambahin ama pajak
    
    def tambah_item(self, nama_item, harga, jumlah):
        self.daftar_pesanan.append((nama_item,harga,jumlah))
        self.subtotal += harga * jumlah #Kita dapetin dlu subtotal disini

        self.hitung_total()

    def cetak_struk(self):
        self.hitung_total()
        print("=" * 40)
        print(f"\t  STRUK PEMBAYARAN - MEJA {self.meja}")
        print("=" * 40)
        print(f"Pelanggan: {self.pelanggan}")
        
        print("-" * 40)
        for nama_item, harga, jumlah in self.daftar_pesanan:
            total = harga * jumlah
            print(f"{nama_item:<24} x {jumlah:<2} Rp {total:>8,.0f}")#ini biar keliatan rapih aja, kek sesuai sama yang ada di guidenya
        print("-" * 40)

        print(f"{'Subtotal':<25} : Rp {self.subtotal:>8,.0f}")
        print(f"{'PPN (10%)':<25} : Rp {self.nilaipajak:>8,.0f}")
        print(f"{'Total Akhir':<25} : Rp {self.total_akhir:>8,.0f}")
        print("=" * 40)

    def proses_pembayaran(self):
        # Bagian kina disini, method ini cuman buat ngecheck, digunakan untuk menghitung apakah ada lebih bayar atau kurang bayar
        pass