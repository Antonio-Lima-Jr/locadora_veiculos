
from typing import List
from rich.console import Console
from rich.theme import Theme
from rich.columns import Columns
from rich.panel import Panel

from models.veiculo import Veiculo


class Print:
    def __init__(self):
        custom_theme = Theme({
            "title": "#ccc010 bold",
            "options": "#B900E0 bold ",
            "input": "bold blue",
            "error": "bold red",
            "success": "bold green",
        })
        self.console = Console(theme=custom_theme)

    def print_title(self, title):
        print("")
        self.console.print(
            title,
            style="title",
            justify="center",
            emoji=True,
        )
        print("")

    def print_options(self, options):
        self.console.print(
            options,
            style="options",
            justify="left",
            emoji=True,
        )

    def print_input(self, input):
        self.console.print(
            input,
            style="input",
            justify="left",
            emoji=True,
        )

    def print_error(self, error):
        self.console.print(
            error,
            style="error",
            justify="left",
            emoji=True,
        )

    def print_success(self, success):
        self.console.print(
            success,
            style="success",
            justify="center",
            emoji=True,
        )

    def print_todos_veiculos(self, veiculos: List[Veiculo]):
        self.print_title("Veiculos cadastrados")
        if len(veiculos) == 0:
            self.print_success("Nenhum veiculo cadastrado")
            return
        veiculos_render = [Panel(veiculo.get_content(), expand=True) for veiculo in veiculos]
        columns = Columns(veiculos_render, equal=True, align="right")
        self.console.print(columns)

    def input_veiculo(self):
        self.print_input("Digite a categoria do veiculo")
        categoria = input()
        self.print_input("Digite a transmissao do veiculo")
        transmissao = input()
        self.print_input("Digite o combustivel do veiculo")
        combustivel = input()
        self.print_input("Digite a marca do veiculo")
        marca = input()
        self.print_input("Digite o modelo do veiculo")
        modelo = input()
        self.print_input("Digite o ano do veiculo")
        ano = input()
        self.print_input("Digite a placa do veiculo")
        placa = input()
        self.print_input("Digite o valor da diaria do veiculo")
        valor_diaria = input()
        return categoria, transmissao, combustivel, marca, modelo, int(ano), placa, int(valor_diaria)

    def input_cliente(self):
        self.print_input("Digite o nome do cliente")
        nome = input()
        self.print_input("Digite o CPF do cliente")
        cpf = input()
        self.print_input("Digite o RG do cliente")
        rg = input()
        return nome, cpf, rg
