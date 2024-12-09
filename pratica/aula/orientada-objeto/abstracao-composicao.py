from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado.")
    
    @abstractmethod
    def calcular_perimetro(self):
        raise NotImplementedError("Este método deve ser implementado.")


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio


class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)



circulo1 = Circulo(raio=10)
circulo2 = Circulo(raio=2)
print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())
print(circulo2.calcular_area())

retangulo1 = Retangulo(largura=10, altura=5)
print(retangulo1.calcular_area())
print(retangulo1.calcular_perimetro())



class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True
        print("vruuuuuuuuum")


class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def exibir_detalhes(self):
        print(f"Carro {self.marca} {self.modelo}")

    def mostrar_potencia_motor(self):
        print(f"Motor de potência: {self.motor.potencia} cavalos")
        

motor1 = Motor(potencia=200)
carro1 = Carro(marca="Honda", modelo="Civic", motor=motor1)

motor1.ligar_motor()
print(motor1.potencia)
print(motor1.ligado)
carro1.exibir_detalhes()
carro1.mostrar_potencia_motor()

