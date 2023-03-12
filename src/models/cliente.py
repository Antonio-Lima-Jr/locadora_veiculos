class Cliente:
    def __init__(self, nome, cpf, rg, carros):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.carros = carros


class ClienteBuilder:
    def __init__(self):
        self.cliente = Cliente("", "", "", [])

    def set_nome(self, nome):
        self.cliente.nome = nome
        return self

    def set_cpf(self, cpf):
        self.cliente.cpf = cpf
        return self

    def set_rg(self, rg):
        self.cliente.rg = rg
        return self

    def add_carro(self, carro):
        self.cliente.carros.append(carro)
        return self

    def build(self):
        return self.cliente
