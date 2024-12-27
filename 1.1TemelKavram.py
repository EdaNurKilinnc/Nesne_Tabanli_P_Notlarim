class Student:

    #Özellikler (attributes)
    def __init__(self, name ,grade):
        self.name=name
        self.grade=grade
    

    #metotlar(methods)
    def bilgileri_goster(self):                                  #self, bir sınıfın metotlarında, o metodu çağıran nesneye ait özelliklere ve diğer metotlara erişimi sağlar.
        return f"İsim: {self.name}, Notu:{self.grade}"   # Eğer self kullanmasaydık, her metotta hangi nesne üzerinde işlem yapıldığını belirtmek mümkün olmazdı.
    

    #Öğrencinin gecip gecmedıgını kontrol eden bir metot
    def is_passing(self):
        if self.grade >= 50: #eger not 50 uzerındeyse gecmıstır
            return True
        else:
            return False
    
#Öğrenci listesi (dizi)  
students = [
    Student("Ali",45),
    Student("Ayşe",75),
    Student("Mehmet",60)
]

#Döngü kullanarak öğrencilerin bilgilerini ve geçme durumlarını kontrol 
for student in students:
    print(student.bilgileri_goster())
    if student.is_passing():
        print(f"{student.name}dersi geçti")
    else:
        print(f"{student.name} dersi geçemedi")
