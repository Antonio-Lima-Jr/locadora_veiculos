from models.veiculo import VeiculoBuilder
from models.cliente import ClienteBuilder
from utils.print import Print
from models.locadora import Locadora
from models.locacao import Locacao
from models.locacao import LocacaoBuilder


class LocadoraService:
    def __init__(self):
        self.locadora: Locadora = Locadora()

        self.print = Print()

    def inicializar_mock(self):
        self.mock_veiculos()
        self.mock_clientes()
        self.mock_locacoes()

    def mock_veiculos(self):
        carro1 = VeiculoBuilder()\
            .set_categoria("Sedan")\
            .set_transmissao("Automática")\
            .set_combustivel("Gasolina")\
            .set_marca("Chevrolet")\
            .set_modelo("Cruze")\
            .set_ano(2018)\
            .set_placa("ABC-1234")\
            .set_valor_diaria(150)\
            .build()

        carro2 = VeiculoBuilder()\
            .set_categoria("Sport")\
            .set_transmissao("Manual")\
            .set_combustivel("Gasolina")\
            .set_marca("Chevrolet")\
            .set_modelo("Camaro")\
            .set_ano(2018)\
            .set_placa("OPG-1234")\
            .set_valor_diaria(300)\
            .build()

        carro3 = VeiculoBuilder()\
            .set_categoria("SUV")\
            .set_transmissao("Automática")\
            .set_combustivel("Gasolina")\
            .set_marca("Chevrolet")\
            .set_modelo("Tracker")\
            .set_ano(2018)\
            .set_placa("ABC-1234")\
            .set_valor_diaria(150)\
            .build()

        self.locadora.veiculos.append(carro1)
        self.locadora.veiculos.append(carro2)
        self.locadora.veiculos.append(carro3)

    def mock_clientes(self):
        cliente1 = ClienteBuilder()\
            .set_nome("João")\
            .set_cpf("123.456.789-10")\
            .set_rg("12.345.678-9")\
            .build()

        cliente2 = ClienteBuilder()\
            .set_nome("Maria")\
            .set_cpf("123.456.789-11")\
            .set_rg("12.345.679-9")\
            .build()
            
        cliente3 = ClienteBuilder()\
            .set_nome("José")\
            .set_cpf("123.456.789-12")\
            .set_rg("12.345.680-9")\
            .build()
        
        cliente4 = ClienteBuilder()\
            .set_nome("Joana")\
            .set_cpf("123.456.789-13")\
            .set_rg("12.345.681-9")\
            .build()

        self.locadora.clientes.append(cliente1)
        self.locadora.clientes.append(cliente2)
        self.locadora.clientes.append(cliente3)
        self.locadora.clientes.append(cliente4)

    def mock_locacoes(self):
        locacao1 = LocacaoBuilder()\
            .set_cliente(self.locadora.clientes[0])\
            .set_veiculo(self.locadora.veiculos[0])\
            .set_data_inicio("01/01/2020")\
            .set_dias_aluguel(10)\
            .build()

        locacao2 = LocacaoBuilder()\
            .set_cliente(self.locadora.clientes[1])\
            .set_veiculo(self.locadora.veiculos[1])\
            .set_data_inicio("01/01/2020")\
            .set_dias_aluguel(30)\
            .build()

        self.locadora.locacoes.append(locacao1)
        self.locadora.locacoes.append(locacao2)

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
            categoria, transmissao, combustivel, marca, modelo, ano, placa, valor_diaria = self.print.input_veiculo()

            carro = VeiculoBuilder()\
                .set_categoria(categoria)\
                .set_transmissao(transmissao)\
                .set_combustivel(combustivel)\
                .set_marca(marca)\
                .set_modelo(modelo)\
                .set_ano(ano)\
                .set_placa(placa)\
                .set_valor_diaria(valor_diaria)\
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

    def realizar_locacao(self):
        self.print.print_title("Realizar locação")
        self.print.print_input("Digite o CPF do cliente")
        cpf = input()
        listCliente = [
            cliente for cliente in self.locadora.clientes if cliente.cpf == cpf]
        if len(listCliente) == 0:
            self.print.print_error("Cliente não encontrado")
            return
        self.print.print_success("Cliente encontrado")
        cliente = listCliente[0]
        self.print.print_input("Digite a placa do veiculo")
        placa = input()
        listVeiculo = [
            veiculo for veiculo in self.locadora.veiculos if veiculo.placa == placa]
        if len(listVeiculo) == 0:
            self.print.print_error("Veiculo não encontrado")
            return
        self.print.print_success("Veiculo encontrado")
        veiculo = listVeiculo[0]
        if veiculo.placa in [locacao.veiculo.placa for locacao in self.locadora.locacoes]:
            self.print.print_error("Veiculo já alugado")
            return
        self.print.print_input("Digite a data de início da locação")
        data_inicio = input()
        self.print.print_input("Quantos dias deseja alugar?")
        dias_aluguel = input()
        self.locadora.locacoes.append(
            LocacaoBuilder()
            .set_cliente(cliente)
            .set_veiculo(veiculo)
            .set_data_inicio(data_inicio)
            .set_dias_aluguel(int(dias_aluguel))
            .build())
        self.print.print_success("Locação realizada com sucesso")

    def relatorio_locacao(self):
        self.print.print_title("Relatório de locações")
        self.print.print_todas_locacoes(self.locadora.locacoes)
