"""--- CLASSMETHOD ---

sınıf uzerınde etkı eder( self gıbı o da cls kullanır ama self nesneye etkı ederken, cls sınıfın hepsıne etki eder)"""


# class Calisanlar():

#     calisanlar_listesi = []

#     def __init__(self, isim, soyisim, maas, departman):
#         self.isim       = isim
#         self.soyisim    = soyisim
#         self.maas       = maas
#         self.departman  = departman
#         self.bilgileri_kaydet()
    
#     def bilgileri_kaydet(self):
#         self.calisanlar_listesi.append(self.isim)
#         self.calisanlar_listesi.append(self.soyisim)
#         self.calisanlar_listesi.append(self.maas)
#         self.calisanlar_listesi.append(self.departman)
    
#     @classmethod
#     def bilgileri_goster(cls):
#         print(cls.calisanlar_listesi)

# calisan_1 = Calisanlar("Mert", "Kaya", 6500, "Bilgi İşlem")
# calisan_1.bilgileri_goster()
# Calisanlar.bilgileri_goster()


"""------------------------------------"""

from datetime import date
class kisi:
    zaamO= 1.1
    kisiSayısı = 0
    def __init__(self, isim,yas):
        self.isim = isim
        self.yas = yas
        kisi.kisiSayısı += 1

    def bilgilerini_soyle(self): #instance method,self sayesinde nesnenın kendi özelliklerine ve metodlarına erişilir
        return f"Ad : {self.isim} Yaş: {self.yas}"
    
    @classmethod # eger bunu yapmazsak nesne olmadan cagrılamazdı nesne methodu olurdu, bız bununla bırlıkte sınıf metodu
    def kisiSayısını_soyle(cls):
        return cls.kisiSayısı
    
    @classmethod
    def string_ile_olustur(cls,str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)
    
    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili): 
        return cls(isim,date.today().year-dogum_yili)
    
    @staticmethod
    def dogum_yili_hesapla(kisi): #kisi parametresını vermeden olusturabılcegın seyler de var statıc de
        return date.today().year-kisi.yas
    


    
kisi1 = kisi("ali",20)
kisi2 = kisi("veli",30) 
kisi3 = kisi.string_ile_olustur("Ayşe-25")
kisi4 = kisi.dogum_yili_ile_olustur("Elif",1990)

# print(kisi.kisiSayısını_soyle())

# print(kisi3.bilgilerini_soyle())

kisi5 = kisi.string_ile_olustur("Mehmet-40")
print(kisi5.bilgilerini_soyle())

# print(kisi4.bilgilerini_soyle())

# print(kisi.dogum_yili_hesapla(kisi3))


"""   ------STATİC METHOD--------"""
"""sınıftan bapımsız işlevlik sunar,statik metotlar
 ınheritence(self) ve sınıfın(cls) kendisine doğrudan erişim gerektirmaz
 classın kendisinden de içindeki değişkenlerden de bağımsız bağımsızdır ,daha genel bi metot
   """

# class Calisan:
#     calisan_sayisi = 0  # Sınıf değişkeni

#     def __init__(self, isim, maas):
#         self.isim = isim
#         self.maas = maas
#         Calisan.calisan_sayisi += 1

#     @classmethod
#     def calisan_sayisini_goster(cls):
#         # Sınıf değişkenine erişim sağlıyor ve toplam çalışan sayısını gösteriyor
#         print(f"Toplam çalışan sayısı: {cls.calisan_sayisi}")

#     @staticmethod
#     def maas_hesapla(temel_maas, prim_orani):
#         # Sınıf veya örneklem ile ilgisi yok, bağımsız bir işlem yapıyor
#         return temel_maas + (temel_maas * prim_orani)

# # Sınıftan birkaç örneklem oluşturalım
# calisan1 = Calisan("Mert", 5000)
# calisan2 = Calisan("Ayşe", 6000)

# # Sınıf metodunu hem sınıf üzerinden hem de örneklem üzerinden çağırabiliriz
# Calisan.calisan_sayisini_goster()  # Sınıf üzerinden çağrı
# calisan1.calisan_sayisini_goster()  # Örneklem üzerinden çağrı

# # Statik metodu hem sınıf üzerinden hem de örneklem üzerinden çağırabiliriz
# print(Calisan.maas_hesapla(5000, 0.1))  # 5500
# print(calisan1.maas_hesapla(4000, 0.2))  # 4800

