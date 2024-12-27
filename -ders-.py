class dersnotu:
    def not_hesap(self):
        raise NotImplementedError("bu sınıf tanımlanmadı")

class final(dersnotu):
    def __init__(self,finalnotu):
        self.finalnotu=finalnotu
    def finalhesap(self):
        if self.finalnotu<55:
            return"bute kaldın"
        else:
           
            return self.finalnotu*60/100
    
class vize(dersnotu):
    def __init__(self,vizenotu):
        self.vizenotu=vizenotu
    def vizehesap(self):
        return self.vizenotu*30/100
    

print(final(55))


