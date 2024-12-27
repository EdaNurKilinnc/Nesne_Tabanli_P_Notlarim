#kitap sınıfı
class Book:
    def __init__(self,kitapAdı,yazar):
        self.kitapAdı=kitapAdı
        self.yazar=yazar

    def bilgileri_göster(self):
        return f"Kitap:{self.kitapAdı},Yazar:{self.yazar}"

#Kütüphane sınıfı
class Kütüphane:
    def __init__(self):
        self.kitaplar=[] #kütüphanedeki kitapları saklayan liste
    
    #kütüphaneye kitap ekleme
    def kitap_ekle(self,kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.kitapAdı} adlı kitap kütüphaneye eklendi.")

    #Kütüphaneden kitap silme
    def remove_book (self,kitapAdı):
        for m in self.kitaplar:
            if m.kitapAdı  == kitapAdı:
                self.kitaplar.remove(m)
                print(f"{m.kitapAdı} adlı kitap kütüphaneden silindi.")
                return
        print("bu isimde bir kitap bulunamadı")
    
    #kütüphanedeki kitapları listeleme
    def list_book(self):
        if not self.kitaplar:
            print("Kütüphanede hiç kitap yok.")
        else:
            print("Kütüphanedeki kitaplar:")
            for k in self.kitaplar:
                print(k.bilgileri_göster())

#Ana Program
def library_system():
    library=Kütüphane()

    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Çıkış")

        choice = input("Bir seçenek girin (1-4): ")

        if choice == "1":
            #kitap ekle
            kitapAdı = input("Kitap adı:")
            yazar = input("yaar adı:")
            kitap = Book(kitapAdı,yazar)
            library.kitap_ekle(kitap)

        elif choice == "2":
            # Kitap sil
            kitapAdı = input("Silinecek kitabın adı: ")
            library.remove_book(kitapAdı)
        
        elif choice == "3":
            # Kitapları listele
            library.list_book()

        elif choice == "4":
            # Çıkış
            print("Sistemden çıkılıyor.")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

# Programı çalıştırma
library_system()  # Yorum satırından çıkardığınızda çalışır.


"""---------------------------------------------------"""


"""daha okunaklı degısken ısmı koyarak kodun aynısı asağıda"""

# Kitap sınıfı
class Kitap:
    def __init__(self, kitap_adi, yazar_adi):
        self.kitap_adi = kitap_adi
        self.yazar_adi = yazar_adi

    def bilgileri_goster(self):
        return f"Kitap: {self.kitap_adi}, Yazar: {self.yazar_adi}"


# Kütüphane sınıfı
class Kutuphane:
    def __init__(self):
        self.kutuphane_kitaplari = []  # Kütüphanedeki kitapları saklayan liste

    # Kütüphaneye kitap ekleme
    def kitap_ekle(self, kitap):
        self.kutuphane_kitaplari.append(kitap)
        print(f"{kitap.kitap_adi} adlı kitap kütüphaneye eklendi.")

    # Kütüphaneden kitap silme
    def kitap_sil(self, kitap_adi):
        for kitap in self.kutuphane_kitaplari:
            if kitap.kitap_adi == kitap_adi:
                self.kutuphane_kitaplari.remove(kitap)
                print(f"{kitap.kitap_adi} adlı kitap kütüphaneden silindi.")
                return
        print("Bu isimde bir kitap bulunamadı.")

    # Kütüphanedeki kitapları listeleme
    def kitaplari_listele(self):
        if not self.kutuphane_kitaplari:
            print("Kütüphanede hiç kitap yok.")
        else:
            print("Kütüphanedeki kitaplar:")
            for kitap in self.kutuphane_kitaplari:
                print(kitap.bilgileri_goster())


# Ana Program
def kutuphane_yonetim_sistemi():
    kutuphane = Kutuphane()

    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Çıkış")

        secim = input("Bir seçenek girin (1-4): ")

        if secim == "1":
            # Kitap ekle
            kitap_adi = input("Kitap adı: ")
            yazar_adi = input("Yazar adı: ")
            kitap = Kitap(kitap_adi, yazar_adi)
            kutuphane.kitap_ekle(kitap)

        elif secim == "2":
            # Kitap sil
            kitap_adi = input("Silinecek kitabın adı: ")
            kutuphane.kitap_sil(kitap_adi)

        elif secim == "3":
            # Kitapları listele
            kutuphane.kitaplari_listele()

        elif secim == "4":
            # Çıkış
            print("Sistemden çıkılıyor.")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


# Programı çalıştırma
kutuphane_yonetim_sistemi()  # Yorum satırından çıkarıldığında çalışır.
