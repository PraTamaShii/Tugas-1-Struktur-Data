class Peta:
    def __init__(self):
        self.cityList = {}
      
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
      
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:

                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False

    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False

    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False

petaJatim = Peta()
petaJatim.tambahkanKota("Pasuruan")
petaJatim.tambahkanKota("Surabaya")
petaJatim.tambahkanKota("Sidoarjo")
petaJatim.tambahkanKota("Malang")
petaJatim.tambahkanKota("Kepanjen")
petaJatim.tambahkanKota("Kota Mojokerto")
petaJatim.tambahkanKota("Blitar")
petaJatim.tambahkanKota("Kediri")
petaJatim.tambahkanKota("Tulungagung")
petaJatim.tambahkanKota("Nganjuk")
petaJatim.tambahkanKota("Trenggalek")
petaJatim.tambahkanKota("Bojonegoro")
petaJatim.tambahkanKota("Madiun")
petaJatim.tambahkanKota("Ponorogo")
petaJatim.tambahkanKota("Ngawi")
#jalur antar kota
petaJatim.tambahkanJalan("Pasuruan","Kota Mojokerto")
petaJatim.tambahkanJalan("Pasuruan","Malang")
petaJatim.tambahkanJalan("Sidoarjo","Kota Mojokerto")
petaJatim.tambahkanJalan("Sidoarjo","Malang")
petaJatim.tambahkanJalan("Kepanjen","Malang")
petaJatim.tambahkanJalan("Kepanjen","Blitar")
petaJatim.tambahkanJalan("Surabaya","Kota Mojokerto")
petaJatim.tambahkanJalan("Surabaya","Sidoarjo")
petaJatim.tambahkanJalan("Surabaya","Bojonegoro")
petaJatim.tambahkanJalan("Kota Mojokerto","Nganjuk")
petaJatim.tambahkanJalan("Kota Mojokerto","Kediri")
petaJatim.tambahkanJalan("Malang","Blitar")
petaJatim.tambahkanJalan("Blitar","Tulungagung")
petaJatim.tambahkanJalan("Tulungagung","Trenggalek")
petaJatim.tambahkanJalan("Trenggalek","Ponorogo")
petaJatim.tambahkanJalan("Nganjuk","Madiun")
petaJatim.tambahkanJalan("Madiun","Ponorogo")
petaJatim.tambahkanJalan("Madiun","Ngawi")
petaJatim.tambahkanJalan("Ngawi","Bojonegoro")

petaJatim.printPeta()
print('------------------------------')
petaJatim.hapusKota("Kepanjen")
petaJatim.printPeta()
