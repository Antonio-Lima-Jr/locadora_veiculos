class Carro:
    def __init__(self, categoria, transmissao, combustivel, marca, modelo, ano, placa):
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


class CarroBuilder:
    def __init__(self):
        self.carro = Carro("", "", "", "", "")

    def set_categoria(self, categoria):
        self.carro.categoria = categoria
        return self

    def set_transmissao(self, transmissao):
        self.carro.transmissao = transmissao
        return self

    def set_combustivel(self, combustivel):
        self.carro.combustivel = combustivel
        return self

    def set_marca(self, marca):
        self.carro.marca = marca
        return self

    def set_modelo(self, modelo):
        self.carro.modelo = modelo
        return self

    def set_ano(self, ano):
        self.carro.ano = ano
        return self

    def set_placa(self, placa):
        self.carro.placa = placa
        return self

    def build(self):
        return self.carro

