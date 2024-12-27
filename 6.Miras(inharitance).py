# class Calisan:
#     def __init__(self,isim,soyisim,maas):
#         self.isim = isim
#         self.soyisim =  soyisim
#         self.maas=maas
#         self.email = isim + soyisim +"@sirket.com"
#     def bilgiler_goster(self):
#         return "Ad: {} soyisim: {} maas: {} email {} ".format(self.isim,self.soyisim,self.maas,self.email)
# calisan1= Calisan("ali","calıskan",5000)
# calisan2= Calisan("veli","uzun",6000)

# class Yazilimci(Calisan): #calısandan miras aldık paranytezın ıcıne yazarak
#     def __init__(self, isim, soyisim, maas,bidigi_dil):
#         super().__init__(isim, soyisim, maas) # miras aldık ustten
#         self.bildigi_dil = bidigi_dil
#     zam_oranı=1.2  #overriding yaptık, yeniden tanımladık bu özelliği
#     def bilgileri_goster(self):  # burada da overrid yaptık
#         return "Ad: {} soyisim: {} maas: {} email {} dil:{} ".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
    
#     def dilini_soyle(self):
#         return f"Bildiğim dil:{self.bildigi_dil}"

# yazilimci1= Yazilimci("Ayse","yıldız",7000,"python")
# yazilimci2= Yazilimci("fatma","ay",8000,"java")

# print(yazilimci1.dilini_soyle())

"""-------------------------------------------------------------------"""
"""üstteki koda eklemeler yaptık"""

# class Calisan:
#     def __init__(self,isim,soyisim,maas):
#         self.isim = isim
#         self.soyisim =  soyisim
#         self.maas=maas
#         self.email = isim + soyisim +"@sirket.com"
#     def bilgiler_goster(self):
#         return "Ad: {} soyisim: {} maas: {} email {} ".format(self.isim,self.soyisim,self.maas,self.email)


# class Yazilimci(Calisan): #calısandan miras aldık paranytezın ıcıne yazarak
#     def __init__(self, isim, soyisim, maas,bidigi_dil):
#         super().__init__(isim, soyisim, maas) # miras aldık ustten
#         self.bildigi_dil = bidigi_dil
#     zam_oranı=1.2  #overriding yaptık, yeniden tanımladık bu özelliği
#     def bilgileri_goster(self):  # burada da overrid yaptık
#         return "Ad: {} soyisim: {} maas: {} email {} dil:{} ".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
    
#     def dilini_soyle(self):
#         return f"Bildiğim dil:{self.bildigi_dil}"
    
# class yonetici (Calisan):
#     def __init__(self, isim, soyisim, maas,calisanlar = None):
#         super().__init__(isim, soyisim, maas)
#         if calisanlar == None:
#             self.calisanlar = []
#         else:
#             self.calisanlar = calisanlar
    
#     def calisan_ekle(self,calisan):
#         if calisan not in self.calisanlar:
#             self.calisanlar.append(calisan)
    
#     def calisan_sil(self,calisan):
#         if calisan in self.calisanlar:
#             self.calisanlar.remove(calisan)

#     def calisanlari_goster(self):
#         for calisan in self.calisanlar:
#             print(calisan.bilgileri_goster())


    

# calisan1= Calisan("ali","calıskan",5000)
# calisan2= Calisan("veli","uzun",6000)

# yazilimci1= Yazilimci("Ayse","yıldız",7000,"python")
# yazilimci2= Yazilimci("fatma","ay",8000,"java")

# yonetici1= yonetici("metın","ali",10000)
# print(yonetici1.bilgiler_goster())

# yonetici1.calisan_ekle(calisan1)
# yonetici1.calisan_ekle(yazilimci1)
# yonetici1.calisanlari_goster()

class Calisan:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"

    def bilgiler_goster(self):
        return "Ad: {} soyisim: {} maas: {} email: {}".format(self.isim, self.soyisim, self.maas, self.email)


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil = bildigi_dil

    def bilgiler_goster(self):  # Override
        return "Ad: {} soyisim: {} maas: {} email: {} dil: {}".format(self.isim, self.soyisim, self.maas, self.email, self.bildigi_dil)


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, calisanlar=None):
        super().__init__(isim, soyisim, maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self, calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisanlari_goster(self):
        if not self.calisanlar:  # Liste boş mu?
            print("Hiç çalışan yok.")
        else:
            for calisan in self.calisanlar:
                print(calisan.bilgiler_goster())  # Doğru metod çağrısı


# Test
calisan1 = Calisan("Ali", "Caliskan", 5000)
yazilimci1 = Yazilimci("Ayse", "Yildiz", 7000, "Python")
yonetici1 = Yonetici("Metin", "Ali", 10000)

yonetici1.calisan_ekle(calisan1)
yonetici1.calisan_ekle(yazilimci1)

print("\nYönetici bilgileri:")
print(yonetici1.bilgiler_goster())

print("\nÇalışanlar:")
yonetici1.calisanlari_goster()
