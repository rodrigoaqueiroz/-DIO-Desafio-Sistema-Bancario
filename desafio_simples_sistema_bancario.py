def exibir_menu():
    print('Qual operacação bancária deseja realizar?')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Extrato')
    print('s - Sair')
    print('---------')

class Operacoes_bancarias:
    def __init__(self):
        self.saldo_conta = 0

    def deposito(self):
        valor_deposito = int(input('Quanto deseja depositar? '))
        self.saldo_conta += valor_deposito
        print(f'Você depositou R$ {self.saldo_conta:.2f}\n')

    def saque(self):
        QUANTIDADE_MAX_SAQUES = 3
        while QUANTIDADE_MAX_SAQUES > 0:
            valor_saque = int(input('Quanto deseja sacar? '))
            if valor_saque <= 500:
                if valor_saque <= self.saldo_conta:
                    self.saldo_conta -= valor_saque
                else:
                    print('Não tem o valor necessário na conta. Tente novamente!\n')
            else:
                print('O valor máximo permitido por saque é de R$500,00\n') 
            QUANTIDADE_MAX_SAQUES -= 1
            
    def extrato(self):
        print(f'Você tem R$ {self.saldo_conta:.2f} na conta\n')

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
        else:
            print('Opção inválida, tente novamente.')

if __name__ == "__main__":
    main()
