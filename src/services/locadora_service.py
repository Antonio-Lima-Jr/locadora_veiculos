from models.carro import CarroBuilder
from models.cliente import ClienteBuilder
from utils.print import Print
from models.locadora import Locadora


class LocadoraService:
    def __init__(self):
        self.locadora = Locadora()
        self.print = Print()

    def cadastrar_veiculo(self):
        # TODO: Listar veiculos cadastrados
        self.print.print_todos_veiculos(self.locadora.veiculos)

        self.print.print_title("Cadastrar veiculo")
        estaCadastrado = "n"

        if len(self.locadora.veiculos) != 0:
            self.print.print_input(
                "O carro que será cadastrado está em uma das categorias listadas acima \[y/N]?")
            estaCadastrado = input()

        if estaCadastrado == "n" or estaCadastrado == "N" or estaCadastrado == "":
            categoria, transmissao, combustivel, marca, modelo, ano, placa = self.print.input_veiculo()

            carro = CarroBuilder()\
                .set_categoria(categoria)\
                .set_transmissao(transmissao)\
                .set_combustivel(combustivel)\
                .set_marca(marca)\
                .set_modelo(modelo)\
                .set_ano(ano)\
                .set_placa(placa)\
                .build()

            self.locadora.veiculos.append(carro)

            self.print.print_success("Veiculo cadastrado com sucesso")
        elif estaCadastrado == "y" or estaCadastrado == "Y":
            self.print.print_input("Digite a placa do veiculo")
            placa = input()
            listVeiculo = [
                veiculo for veiculo in self.locadora.veiculos if veiculo.placa == placa]
            if len(listVeiculo) == 0:
                self.print.print_error("Veiculo não encontrado")
                return
            self.print.print_success("Veiculo encontrado")

            veiculoEdit = listVeiculo[0]
            categoria, transmissao, combustivel, marca, modelo, ano, placa = self.print.input_veiculo()
            veiculoEdit.categoria = categoria
            veiculoEdit.transmissao = transmissao
            veiculoEdit.combustivel = combustivel
            veiculoEdit.marca = marca
            veiculoEdit.modelo = modelo
            veiculoEdit.ano = ano
            veiculoEdit.placa = placa
            self.print.print_success("Veiculo editado com sucesso")
            return
        else:
            self.print.print_error("Opção inválida")

    def cadastrar_cliente(self):
        self.print.print_title("Cadastrar cliente")
        nome, cpf, rg = self.print.input_cliente()
        if len(self.locadora.clientes) != 0:
            listCliente = [
                cliente for cliente in self.locadora.clientes if cliente.cpf == cpf]
            if len(listCliente) != 0:
                self.print.print_error("Cliente já cadastrado")
                return
        cliente = ClienteBuilder()\
            .set_nome(nome)\
            .set_cpf(cpf)\
            .set_rg(rg)\
            .build()
        self.locadora.clientes.append(cliente)
        self.print.print_success("Cliente cadastrado com sucesso")

    def realizar_locacao(self, locacao):
        self.locadora.locacoes.append(locacao)

    def relatorio_locacao(self):
        for locacao in self.locadora.locacoes:
            print(locacao)
