class Carro:
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def emitir_som(self):
        print("vruuuuuuum...")
    
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")
        self.emitir_som()


carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2020)
carro2 = Carro(marca="Renault", modelo="Duster", ano=2024)

print(carro1.modelo)
print(carro2.modelo)
carro1.exibir_detalhes()
carro1.emitir_som()
