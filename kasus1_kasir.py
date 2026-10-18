class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga, jumlah):
        self.pelanggan = pelanggan
        self.barang = barang
        self.harga = harga
        self.jumlah = jumlah 
        
    def subtotal(self):
        return self.harga * self.jumlah
    
    def diskon(self):
        total = self.subtotal()
        if total >= 500000:
            return 15
        elif total >= 250000:
            return 10
        elif total >= 100000:
            return 5
        return 0
    
    def tampilkan_struk(self):
        total = self.subtotal()
        potongan = total * self.diskon() / 100
        
        print("STRUK PEMBAYARAN")
        print("Pelanggan:", self.pelanggan)
        print("Barang:", self.barang)
        print(f"Subtotal: Rp{total:,.0f}")
        print(f"Diskon: {self.diskon()}%")
        print(f"Potongan: Rp{potongan:,.0f}")
        print(f"Total bayar: Rp.{total-potongan:,.0f}")
try:
    print("KASIR MARKET")
    pelanggan = input("Nama pelanggan: ")
    barang = input("Nama barang: ")
    harga = int(input("Harga barang: "))  
    jumlah = int(input("Jumlah barang: "))
    
    if not pelanggan.strip() or not barang.strip():
        raise ValueError("Nama tidak boleh kosong.")
    if harga <= 0 or jumlah <= 0:
        raise ValueError("Harga dan jumlah harus positif.")
    transaksi = TransaksiKasir(pelanggan, barang, harga, jumlah)
    transaksi.tampilkan_struk()
    
except ValueError as e:
    print("Input salah:", e)  