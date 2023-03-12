from typing import List
from models.cliente import Cliente
from models.locacao import Locacao
from models.veiculo import Veiculo


class Locadora:
    def __init__(self):
        self.veiculos: List[Veiculo] = []
        self.clientes: List[Cliente] = []
        self.locacoes: List[Locacao] = []