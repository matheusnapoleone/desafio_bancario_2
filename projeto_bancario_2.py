# projeto_bancario_2.py

import textwrap

# Projeto Bancário - Sistema de Gerenciamento de Contas
# Este é um sistema simples de gerenciamento de contas bancárias que permite realizar saques, depósitos e consultar extratos.

def menu():
    menu = """
    =============MENU============
    1 - Sacar
    2 - Depositar   
    3 - Extrato
    4 - Nova conta
    5 - Listar contas
    6 - Novo usuario
    7 - Sair
    =============================
    """
    return input(textwrap.dedent(menu))

def sacar(*, saque_mxm: float, limite_saque: int, saques_feitos: int, saldo: float, extrato: str):
    valor_saque = float(input("Digite o valor desejado para o saque: "))
    if valor_saque <= 0:
        print("Valor inválido.")
    elif valor_saque > saque_mxm:
        print(f"Valor inválido.\nVocê só pode sacar até R${saque_mxm:.2f} por vez.")
    elif saques_feitos >= limite_saque:
        print("Limite diário de saques atingido.")
    elif valor_saque > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor_saque
        saques_feitos += 1
        extrato += f"Saque: -R${valor_saque:.2f}\n"
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso! Saldo: R${saldo:.2f}")
    return saldo, saques_feitos, extrato

def depositar(saldo: float, extrato: str):
    deposito = float(input("Digite o valor do depósito: "))
    if deposito <= 0:
        print("Depósito inválido.")
    else:
        saldo += deposito
        extrato += f"Depósito: +R${deposito:.2f}\n"
        print(f"Depósito de R${deposito:.2f} realizado com sucesso! Saldo: R${saldo:.2f}")
    return saldo, extrato

def mostrar_extrato(extrato: str, saldo: float):
    print("\n=== EXTRATO ===")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R${saldo:.2f}")

def nova_conta():
    print("Função 'Nova conta' ainda não implementada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n== Conta criada com sucesso! ==")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@")
    return None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@ Já existe usuário com esse CPF! @@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("== Usuário criado com sucesso! ==")

def main():
    print("Bem-vindo ao Sistema Bancário!")
    print("Por favor, escolha uma opção do menu.")
    saques_feitos = 0
    limite_saque = 3
    saque_mxm = 500
    saldo = 5000.0
    extrato = ""
    usuarios = []
    contas = []
    agencia_padrao = "0001"
    numero_conta = 1

    while True:
        operacao = int(menu())

        if operacao == 1:
            saldo, saques_feitos, extrato = sacar(
                saque_mxm=saque_mxm,
                limite_saque=limite_saque,
                saques_feitos=saques_feitos,
                saldo=saldo,
                extrato=extrato
            )
        elif operacao == 2:
            saldo, extrato = depositar(saldo, extrato)
        elif operacao == 3:
            mostrar_extrato(extrato, saldo)
        elif operacao == 4:
            conta = criar_conta(agencia_padrao, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        elif operacao == 5:
            listar_contas(contas)
        elif operacao == 6:
            criar_usuario(usuarios)
        elif operacao == 7:
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
