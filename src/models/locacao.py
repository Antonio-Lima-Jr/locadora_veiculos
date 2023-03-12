from unique_id import get_unique_id


class Locacao:
    def __init__(self, cliente, veiculo, data_inicio, dias_aluguel):
        self.id: str = get_unique_id()
        self.cliente: str = cliente
        self.veiculo: str = veiculo
        self.data_inicio: str = data_inicio
        self.dias_aluguel: int = dias_aluguel
        self.valor = 0

    def __str__(self):
        return f"ID: {self.id} - Cliente: {self.cliente} - Veículo: {self.veiculo} - Data de início: {self.data_inicio} - Data de fim: {self.dias_aluguel} - Valor: {self.valor}"


class LocacaoBuilder:
    def __init__(self):
        self.locacao = Locacao("", "", "", "")

    def set_cliente(self, cliente):
        self.locacao.cliente = cliente
        return self

    def set_veiculo(self, veiculo):
        self.locacao.veiculo = veiculo
        return self

    def set_data_inicio(self, data_inicio):
        self.locacao.data_inicio = data_inicio
        return self

    def set_dias_aluguel(self, dias_aluguel):
        self.locacao.dias_aluguel = dias_aluguel
        self.set_valor(self.locacao.veiculo.valor_diaria * dias_aluguel)
        return self

    def set_valor(self, valor):
        self.locacao.valor = valor
        return self

    def build(self):
        return self.locacao
