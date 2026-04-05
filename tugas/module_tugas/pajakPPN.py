from module_tugas.komponenHarga import komponen_harga

class pajak_ppn(komponen_harga):
    def __init__(self, subtotal):
        super.__init__(subtotal)
        self.nilaipajak = self.subtotal * 0.1
        self.total_akhir += self.nilaipajak

    def tambah_item(self,)