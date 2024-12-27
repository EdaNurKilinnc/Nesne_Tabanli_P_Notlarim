from abc import ABC, abstractmethod

# Soyut Öğrenci sınıfı
class Öğrenci(ABC):
    def __init__(self, adi, soyadi, yasi, sinifi, velitelno, öğretmeni):
        self.__adi = adi
        self.__soyadi = soyadi
        self.__yasi = yasi
        self.__sinifi = sinifi
        self.__velitelno = velitelno
        self.__öğretmeni = öğretmeni

    # Getter metotları
    def get_adi(self):
        return self.__adi

    def get_soyadi(self):
        return self.__soyadi

    def get_yasi(self):
        return self.__yasi

    def get_sinifi(self):
        return self.__sinifi

    def get_velitelno(self):
        return self.__velitelno

    def get_öğretmeni(self):
        return self.__öğretmeni

    # Soyut metot (alt sınıflarda implement edilmesi zorunlu)
    @abstractmethod
    def get_info(self):
        pass


# Polimorfik metot: Öğrencinin türüne özgü ek bilgi sağlama
    @abstractmethod
    def öğrenci_türü_bilgi(self):
        pass


# Öğrencilerin sınıf türlerine göre farklı sınıflar oluşturuluyor
class KelebekSinifi(Öğrenci):
    def get_info(self):
        return f"Kelebek Sinifi: {self.get_adi()} {self.get_soyadi()}, Yaş: {self.get_yasi()}, Sınıf: {self.get_sinifi()}, Veli Tel: {self.get_velitelno()}, Öğretmen: {self.get_öğretmeni()}"

    def öğrenci_türü_bilgi(self):
        return "Kelebek öğrencileri, en küçük yaş grubu öğrencileridir."
    
class AslanSinifi(Öğrenci):
    def get_info(self):
        return f"Aslan Sinifi: {self.get_adi()} {self.get_soyadi()}, Yaş: {self.get_yasi()}, Sınıf: {self.get_sinifi()}, Veli Tel: {self.get_velitelno()}, Öğretmen: {self.get_öğretmeni()}"

    def öğrenci_türü_bilgi(self):
        return "Aslan öğrencileri,4 yaş üstün zekalı öğrencileridir."
    

class SincapSinifi(Öğrenci):
    def get_info(self):
        return f"Sincap Sinifi: {self.get_adi()} {self.get_soyadi()}, Yaş: {self.get_yasi()}, Sınıf: {self.get_sinifi()}, Veli Tel: {self.get_velitelno()}, Öğretmen: {self.get_öğretmeni()}"

    def öğrenci_türü_bilgi(self):
        return "Sinap öğrencileri,4 yaş üstün zekalı  öğrencileridir."
    
class PandaSinifi(Öğrenci):
    def get_info(self):
        return f"Panda Sinifi: {self.get_adi()} {self.get_soyadi()}, Yaş: {self.get_yasi()}, Sınıf: {self.get_sinifi()}, Veli Tel: {self.get_velitelno()}, Öğretmen: {self.get_öğretmeni()}"
    
    def öğrenci_türü_bilgi(self):
        return "Panda öğrencileri,4 yaş grubu öğrencileridir."
    
class ZürafaSinifi(Öğrenci):
    def get_info(self):
        return f"Zürafa Sinifi: {self.get_adi()} {self.get_soyadi()}, Yaş: {self.get_yasi()}, Sınıf: {self.get_sinifi()}, Veli Tel: {self.get_velitelno()}, Öğretmen: {self.get_öğretmeni()}"

    def öğrenci_türü_bilgi(self):
        return "Zürafa öğrencileri,5 yaş üstün zekalı öğrencileridir."
    
class CeylanSinifi(Öğrenci):
    def get_info(self):
        return f"Ceylan Sinifi: {self.get_adi()} {self.get_soyadi()}, Yaş: {self.get_yasi()}, Sınıf: {self.get_sinifi()}, Veli Tel: {self.get_velitelno()}, Öğretmen: {self.get_öğretmeni()}"

    def öğrenci_türü_bilgi(self):
        return "Ceylan öğrencileri,5 yaş grubu öğrencileridir."
    
# Öğrenciler listesi
Öğrenciler = [
    KelebekSinifi("Arda", "Beniz", 3, "Kelebek", "05245961875", "Egemen Yalçın"),
    KelebekSinifi("Ekrem", "Bilim", 3, "Kelebek", "05425631548", "Egemen Yalçın"),
    KelebekSinifi("Ceren", "Aksoy", 3, "Kelebek", "05472853695", "Egemen Yalçın"),
    AslanSinifi("Ayşe", "Ensar", 4, "Aslan", "0574261549", "Jale Kale"),
    AslanSinifi("Ayşegül", "Ümit", 4, "Aslan", "05418536941", "Jale Kale"),
    AslanSinifi("Emirhan", "İlim", 4, "Aslan", "05782499657", "Jale Kale"),
    AslanSinifi("Enes", "Yiğit", 4, "Aslan", "05371980382", "Jale Kale"),
    SincapSinifi("Nilay", "Kök", 4, "Sincap", "0546280482", "Emir Yanıt"),
    SincapSinifi("Suna", "Bayram", 4, "Sincap", "05374828123", "Emir Yanıt"),
    SincapSinifi("Halil", "Ker", 4, "Sincap", "05468279475", "Emir Yanıt"),
    PandaSinifi("Can", "Dinç", 5, "Balık", "0546286474", "Hilal Ekin"),
    PandaSinifi("Kerem", "Kısım", 5, "Balık", "0534858933", "Hilal Ekin"),
    PandaSinifi("Emin", "Tunç", 5, "Balık", "05472475824", "Hilal Ekin"),
    PandaSinifi("Emine", "Tunç", 5, "Balık", "05364789254", "Hilal Ekin"),
    ZürafaSinifi("Nil", "Umut", 5, "Panda", "053894320345", "Mustafa Akın"),
    ZürafaSinifi("Emre", "Alptek", 5, "Panda", "05345665432", "Mustafa Akın"),
    ZürafaSinifi("İpek", "Esin", 5, "Panda", "05422309873", "Mustafa Akın"),
    CeylanSinifi("Yunus", "Zen", 6, "Zürafa", "05436284647", "Nuray Demir"),
    CeylanSinifi("Erva", "Zen", 6, "Zürafa", "05345627367", "Nuray Demir"),
    CeylanSinifi("Eda", "Akın", 6, "Zürafa", "0546374583", "Nuray Demir"),
    CeylanSinifi("Ahmet", "Aysü", 6, "Zürafa", "05345634873", "Nuray Demir"),
    CeylanSinifi("Naz", "Keman", 6, "Zürafa", "05463744842", "Danla Kılçık"),
    CeylanSinifi("Zeynep", "Anka", 6, "Ceylan", "05364738823", "Danla Kılçık"),
    CeylanSinifi("Naz", "Parla", 6, "Ceylan", "053452678338", "Danla Kılçık"),
    CeylanSinifi("Merve", "İclal", 6, "Ceylan", "05345672446", "Danla Kılçık")
]

# Öğrenci bilgisi bulma fonksiyonu
def ogrenci_bilgisi_bul(adi):
    for öğrenci in Öğrenciler:
        if öğrenci.get_adi() == adi:
            return öğrenci.get_info()
    return "Öğrenci bulunamadı."

# Yeni öğrenci ekleme fonksiyonu
def yeni_ogrenci_ekle():
    isim = input("Öğrencinin ismini girin: ")
    soyisim = input("Öğrencinin soyismini girin: ")
    telno = input("Velinin telefon numarasını girin: ")
    yas = int(input("Öğrencinin yaşını girin: "))
    sinifadi = input("Öğrencinin sınıf adını girin: ")
    öğretmeni = input("Öğretmeninin ismini giriniz: ")

    # Öğrencinin sınıfını seçme
    ogrenci_turu = input("Öğrenci türünü seçin (Kelebek, Aslan, Sincap, Panda, Zürafa, Ceylan): ").lower()

    if ogrenci_turu == "kelebek":
        yeni_ogrenci = KelebekSinifi(isim, soyisim, yas, sinifadi, telno, öğretmeni)
    elif ogrenci_turu == "aslan":
        yeni_ogrenci = AslanSinifi(isim, soyisim, yas, sinifadi, telno, öğretmeni)
    elif ogrenci_turu == "sincap":
        yeni_ogrenci = SincapSinifi(isim, soyisim, yas, sinifadi, telno, öğretmeni)
    elif ogrenci_turu == "panda":
        yeni_ogrenci = PandaSinifi(isim, soyisim, yas, sinifadi, telno, öğretmeni)
    elif ogrenci_turu == "zürafa":
        yeni_ogrenci = ZürafaSinifi(isim, soyisim, yas, sinifadi, telno, öğretmeni)
    elif ogrenci_turu == "ceylan":
        yeni_ogrenci = CeylanSinifi(isim, soyisim, yas, sinifadi, telno, öğretmeni)
    else:
        print("Geçersiz öğrenci türü.")
        return

    Öğrenciler.append(yeni_ogrenci)
    print(f"{isim} {soyisim} başarıyla eklendi.")

# Yeni öğrenci eklemek için kullanıcıya soru sorma
def yeni_ogrenci_ekle_sorgu():
    while True:
        cevap = input("Yeni bir öğrenci eklemek ister misiniz? (evet/hayır): ").lower()
        if cevap == "evet":
            yeni_ogrenci_ekle()
        elif cevap == "hayır":
            print("Yeni öğrenci eklenmedi.")
        else:
            print("Geçersiz cevap. Lütfen 'evet' veya 'hayır' girin.")
            continue
        break

# Öğrenci silme fonksiyonu
def ogrenci_sil(adi):
    global Öğrenciler
    for öğrenci in Öğrenciler:
        if öğrenci.get_adi() == adi:
            Öğrenciler.remove(öğrenci)
            return f"{adi} başarıyla silindi."
    return "Öğrenci bulunamadı."

# Ana döngü
while True:
    # Yeni öğrenci ekleme işlemi
    yeni_ogrenci_ekle_sorgu()

    # Öğrenci bilgisi sorgulama
    adi = input("Bilgilerini öğrenmek istediğiniz öğrencinin adını girin: ")
    print(ogrenci_bilgisi_bul(adi))

    # Öğrenci silme işlemi
    silme_adi = input("Silmek istediğiniz öğrencinin adını girin: ")
    print(ogrenci_sil(silme_adi))  # Öğrenci silme fonksiyonunu çağırıyoruz

    # Başka işlem yapmak isteyip istemediğini soruyoruz
    devam = input("Başka bir işlem yapmak ister misiniz? (evet/hayır): ").lower()
    if devam == "hayır":
        break

    # Tüm öğrencilerin bilgilerini ekrana yazdırma
    print("\nTüm Öğrenciler:")
    for öğrenci in Öğrenciler:
        print(öğrenci.get_info())
