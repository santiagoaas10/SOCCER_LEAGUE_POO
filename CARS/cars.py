from abc import ABC, abstractmethod


class Motocicleta(ABC):
    def __init__(self,year,kms,cantidad_ruedas):
        self.year = year
        self.kms=kms
        self.cantidad_ruedas=cantidad_ruedas

    @classmethod
    @abstractmethod
    def acelerar(self,velocidad):
        "lo deben implementar las subclases"
        pass



class Moto(Motocicleta):
    def __init__(self,year,kms,cantidad_ruedas,marca,velocidad):
        super().__init__(year,kms,cantidad_ruedas)
        self.marca=marca
        self.velocidad=velocidad

    def acelerar(self, velocidad):
        self.velocidad = velocidad
        return f"la nueva velocidad es de  {self.velocidad}"
    
class Automovil:
    def __init__(self, kms, brand, year=None): #el año es opcional
        self.year = year
        self.kms = kms
        self._brand=brand
    
    def frenar(self):
        return "frenando"
    
    @property
    def brand(self):
        return self._brand
    
    #'setter para brand con validación'
    @brand.setter
    def brand(self,new_brand):
        if isinstance(new_brand,str) and new_brand:
            self._brand = new_brand
        else:
            raise ValueError("brand debe ser un string no vacío")




class Carro(Automovil):
    def __init__(self, kms, brand, gama ,marca):
        super().__init__(kms, brand) #no pasamos year
        self.gama = gama
        self.marca = marca
    
    def frenar(self):
        return f"el carro {self.marca} de gama {self.gama} esta frenando"

auto1=Automovil(1000,"Toyota",2021)
carro = Carro(5000, "Alta", "BMW", "marca colombiana")

print(carro.kms)
print(carro.gama)
print(carro.brand)
print(carro.marca)
carro.brand = "Audi"

print(carro.frenar())


auteco=Moto(2020,100,2,'Auteco',120)

print(auteco.acelerar(300))


'''
print(carro.frenar())  # ✔️ "El carro BMW de gama Alta está frenando"
print(carro.brand)  # ✔️ "BMW"
print(carro.year)  # ✔️ "2022"

'''