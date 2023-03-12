from utils.print import Print
from services.locadora_service import LocadoraService


console = Print()
init = True
locadora = LocadoraService()
locadora.inicializar_mock()

while True:
    locadoraName = "Locadora Boa Viagem"
    optionsText = "escolha uma das opções abaixo :smiley:"
    if init:
        console.print_title(
            f"Bem-vindo a {locadoraName}, {optionsText}")
        init = False
    else:
        console.print_title(optionsText.capitalize())
    console.print_options("1 .: Cadastrar um Novo Veiculo")
    console.print_options("2 .: Cadastrar um Novo Cliente")
    console.print_options("3 .: Realizar a locação de um Veículo")
    console.print_options("4 .: Relatório de locação")
    console.print_options("5 .: Sair")

    console.print_input("Digite a opção desejada: ")
    option = input()
    options = {
        "1": lambda: locadora.cadastrar_veiculo(),
        "2": lambda: locadora.cadastrar_cliente(),
        "3": lambda: locadora.realizar_locacao(),
        "4": lambda: locadora.relatorio_locacao(),
        "5": lambda: exit()
    }
    try:
        options[option]()
    except KeyError:
        console.print_error("Opção inválida")
