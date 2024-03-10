class Node:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, nama, harga, jumlah):
        if not self.head:
            self.head = Node(nama, harga, jumlah)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(nama, harga, jumlah)

    def tampilkan_pesanan(self):
        current = self.head
        if not current:
            print("Keranjang kosong")
        else:
            index = 1
            while current:
                print(f"{index}. {current.nama} ({current.jumlah}x) {current.harga * current.jumlah} rupiah")
                current = current.next
                index += 1

    def hitung_total(self):
        total = 0
        current = self.head
        while current:
            total += current.harga * current.jumlah
            current = current.next
        return total

    def rangkuman_pesanan(self):
        pesanan = {}
        current = self.head
        while current:
            if current.nama in pesanan:
                pesanan[current.nama] += current.jumlah
            else:
                pesanan[current.nama] = current.jumlah
            current = current.next
        print("\nRangkuman pesanan:")
        for nama, jumlah in pesanan.items():
            print(f"{nama.capitalize()} ({jumlah}x)")
        print(f"Total biaya yang harus dibayarkan adalah {self.hitung_total()} rupiah, terima kasih sudah memesan")

# Inisialisasi menu Miexue
menu = {
    "miexue ice cream": 5000,
    "boba shake": 16000,
    "mi sundae": 14000,
    "mi ganas": 11000,
    "creamy mango boba": 22000
}

# Menampilkan menu Miexue
print("Menu Miexue:")
for nama, harga in menu.items():
    print(f"{nama.capitalize()} -> {harga} rupiah")

# Inisialisasi linked list untuk menyimpan pesanan
keranjang = LinkedList()

while True:
    print("\nPilih aksi:")
    print("1. Pesan menu Miexue")
    print("2. Tampilkan pesanan")
    print("3. Bayar pesanan")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ").lower()

    if pilihan == '1':
        pesanan = input("Masukkan nama menu: ").lower()
        if pesanan in menu:
            jumlah = int(input("Masukkan jumlah: "))
            keranjang.tambah_pesanan(pesanan.capitalize(), menu[pesanan], jumlah)
            print(f"{jumlah} {pesanan.capitalize()} sudah ditambahkan ke keranjang")
        else:
            print("Menu tidak tersedia")
    elif pilihan == '2':
        print("Pesanan yang sudah ditambahkan:")
        keranjang.tampilkan_pesanan()
    elif pilihan == '3':
        break
    elif pilihan == '4':
        exit()
    else:
        print("Pilihan tidak valid")

# Menampilkan daftar pesanan setelah selesai memesan
print("\nDaftar pesanan:")
keranjang.tampilkan_pesanan()

# Menampilkan rangkuman pesanan setelah selesai memesan
keranjang.rangkuman_pesanan()
