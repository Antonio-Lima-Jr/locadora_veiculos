class Veiculo:
    def __init__(self, categoria, transmissao, combustivel, marca, modelo, ano, placa, valor_diaria):
        self.categoria: str = categoria
        self.transmissao: str = transmissao
        self.combustivel: str = combustivel
        self.marca: str = marca
        self.modelo: str = modelo
        self.ano: int = ano
        self.placa: str = placa
        self.valor_diaria: int = valor_diaria

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}\nCategoria: {self.categoria}\nTransmissao: {self.transmissao}\nCombustivel: {self.combustivel}"
    
    def get_content(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}"


class VeiculoBuilder:
    def __init__(self):
        self.carro = Veiculo("", "", "", "", "", 0, "", 0)

    def set_categoria(self, categoria: str):
        self.carro.categoria = categoria
        return self

    def set_transmissao(self, transmissao: str):
        self.carro.transmissao = transmissao
        return self

    def set_combustivel(self, combustivel: str):
        self.carro.combustivel = combustivel
        return self

    def set_marca(self, marca: str):
        self.carro.marca = marca
        return self

    def set_modelo(self, modelo: str):
        self.carro.modelo = modelo
        return self

    def set_ano(self, ano: int):
        self.carro.ano = ano
        return self

    def set_placa(self, placa: str):
        self.carro.placa = placa
        return self

    def set_valor_diaria(self, valor_diaria: int):
        self.carro.valor_diaria = valor_diaria
        return self

    def build(self):
        return self.carro
