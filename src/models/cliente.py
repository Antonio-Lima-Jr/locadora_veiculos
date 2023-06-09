class Cliente:
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def __str__(self):
        return f"Nome: {self.nome} - CPF: {self.cpf} - RG: {self.rg}"

    def get_content(self):
        return f"Nome: {self.nome} - CPF: {self.cpf}"


class ClienteBuilder:
    def __init__(self):
        self.cliente = Cliente("", "", "")

    def set_nome(self, nome):
        self.cliente.nome = nome
        return self

    def set_cpf(self, cpf):
        self.cliente.cpf = cpf
        return self

    def set_rg(self, rg):
        self.cliente.rg = rg
        return self

    def build(self):
        return self.cliente
