
from rich.console import Console
from rich.theme import Theme
from rich.columns import Columns
from rich.panel import Panel


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
            justify="left",
            emoji=True,
        )

    def print_todos_veiculos(self, veiculos):
        self.print_title("Veiculos cadastrados")
        if len(veiculos) == 0:
            self.print_success("Nenhum veiculo cadastrado")
            return
        veiculos_render = [Panel(self.get_content(
            veiculo), expand=True) for veiculo in veiculos]
        columns = Columns(veiculos_render, equal=True, align="right")
        self.console.print(columns)

    def get_content(self, veiculo):
        return f"Marca: {veiculo.marca}\nModelo: {veiculo.modelo}\nAno: {veiculo.ano}\nPlaca: {veiculo.placa}"
    
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
        return categoria,transmissao,combustivel,marca,modelo,ano,placa
