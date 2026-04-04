from module_tugas.pajakPPN import pajak_ppn

class transaksi_pos(pajak_ppn):
    def __init__(self, pelanggan, meja):
        super.__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftar_pesanan = []