from utils.print import Print
from services.locadora_service import LocadoraService


console = Print()
init = True
locadora = LocadoraService()

while True:
    if init:
        console.print_title(
            "Bem-vindo a Locadora Boa Viagem, escolha uma das opções abaixo :smiley:")
        init = False
    else:
        console.print_title("Escolha uma das opções abaixo :smiley:")
    console.print_options("1 .: Cadastrar um Novo Veiculo")
    console.print_options("2 .: Cadastrar um Novo Cliente")
    console.print_options("3 .: Realizar a locação de um Veículo")
    console.print_options("4 .: Relatório de locação")
    console.print_options("5 .: Sair")

    console.print_input("Digite a opção desejada: ")
    option = input()
    options = {
        "1": lambda: locadora.cadastrar_veiculo(),
        "2": "cadastrar_cliente",
        "3": "realizar_locacao",
        "4": "relatorio_locacao",
        "5": lambda: exit()
    }
    try:
        options[option]()
    except KeyError:
        console.print_error("Opção inválida")
