def exibir_menu():
    print('Qual operacação bancária deseja realizar?')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Extrato')
    print('4 - Cadastrar usuário')
    print('5 - Cadastrar conta')
    print('6 - Listar contas')
    print('s - Sair')
    print('---------')

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    numero_conta = 1

    def __init__(self, usuario):
        self.agencia = '0001'
        self.numero = ContaCorrente.numero_conta
        self.usuario = usuario
        self.saldo_conta = 0
        ContaCorrente.numero_conta += 1

class Operacoes_bancarias:
    def __init__(self):
        self.saldo_conta = 0
        self.QUANTIDADE_MAXIMA_SAQUES = 3
        self.OPCOES_QUANTIDADE_SAQUES = [quantidade for quantidade in range(1, self.QUANTIDADE_MAXIMA_SAQUES + 1)]
        self.usuarios = []
        self.contas = []

    def deposito(self):
        numero_conta = int(input('Digite o número da conta: '))
        conta = self.filtrar_conta_por_numero(numero_conta)
        if conta is None:
            print('Conta não encontrada.')
            return

        valor_deposito = int(input('Quanto deseja depositar? '))
        conta.saldo_conta += valor_deposito
        print(f'Você depositou R$ {valor_deposito:.2f}.\nVocê tem R$ {conta.saldo_conta:.2f} na conta de número: {numero_conta}.\n')

    def saque(self):
        numero_conta = int(input('Digite o número da conta: '))
        conta = self.filtrar_conta_por_numero(numero_conta)
        if conta is None:
            print('Conta não encontrada.')
            return

        quantidade_saques = int(input(f'Quantos saques deseja fazer? Máximo {self.QUANTIDADE_MAXIMA_SAQUES}: '))
        while quantidade_saques not in self.OPCOES_QUANTIDADE_SAQUES:
            print('Opção inválida, tente novamente.\n')
            quantidade_saques = int(input(f'Quantos saques deseja fazer? Máximo {self.QUANTIDADE_MAXIMA_SAQUES}'))
        else:
            for _ in range(quantidade_saques):
                valor_saque = int(input('Quanto deseja sacar? '))
                if valor_saque <= 500:
                    if valor_saque <= self.saldo_conta:
                        self.saldo_conta -= valor_saque
                        print(f'O valor do saque foi de {valor_saque:.2f}.\nVocê tem R$ {self.saldo_conta:.2f} na conta.')
                    else:
                        print('Não tem o valor necessário na conta. Tente novamente!\n')
                else:
                    print('O valor máximo permitido por saque é de R$500,00\n') 

    def extrato(self):
        numero_conta = int(input('Digite o número da conta: '))
        conta = self.filtrar_conta_por_numero(numero_conta)
        if conta is None:
            print('Conta não encontrada.')
            return

        print(f'Saldo atual da conta {numero_conta}: {conta.saldo_conta}\n')

    def cadastrar_usuario(self):
        nome = input('Digite o nome do usuário: ')
        data_nascimento = input('Digite a data de nascimento do usuário: ')
        cpf = input('Digite o CPF do usuário: ')
        endereco = input('Digite o endereço do usuário (logradouro, nro - bairro - cidade/estado): ')
        cpf_existente = self.filtrar_usuario_por_cpf(cpf)
        if cpf_existente is not None:
            print('CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.')
            return

        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print('Usuário cadastrado com sucesso.\n')

    def cadastrar_contas(self):
        cpf = input('Digite o CPF do usuário dono da conta: ')
        usuario = self.filtrar_usuario_por_cpf(cpf)
        if usuario is None:
            print('CPF não encontrado. Cadastre o usuário antes de criar a conta.')
            return

        conta = ContaCorrente(usuario)
        self.contas.append(conta)
        print(f'Conta corrente criada com sucesso. Número da conta: {conta.numero}')

    def listar_contas(self):
        if len(self.contas) == 0:
            print('Não há contas cadastradas no sistema.')
        else:
            print('Contas no sistema:')
            for conta in self.contas:
                print(f'Agência: {conta.agencia} | Número: {conta.numero} | Nome do usuário: {conta.usuario.nome}')

    def filtrar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
    
    def filtrar_conta_por_numero(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta
        return None

def main():
    operacoes = Operacoes_bancarias()
    while True:
        exibir_menu()
        operacao_desejada = input("Digite o número da operação (ou 's' para sair): ")

        if operacao_desejada.lower() == 's':
            print('Obrigado por usar nosso serviço. Até a próxima!')
            break

        if operacao_desejada == '1':
            operacoes.deposito()
        elif operacao_desejada == '2':
            operacoes.saque()
        elif operacao_desejada == '3':
            operacoes.extrato()
        elif operacao_desejada == '4':
            operacoes.cadastrar_usuario()  
        elif operacao_desejada == '5':
            operacoes.cadastrar_contas()
        elif operacao_desejada == '6':
            operacoes.listar_contas()    
        else:
            print('Opção inválida, tente novamente.')

if __name__ == "__main__":
    main()
