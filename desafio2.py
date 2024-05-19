import textwrap

def menu():
    
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [7] Sair

    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, saques_limites): #UTILIZAÇÃO DOS PARAMETROS POSICIONAIS, NOMEADOS E HIBRIDOS. 
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saques >= saques_limites
    
    if saldo_excedido:
        print("Saldo insuficiente.")
    elif limite_excedido:
        print("O valor do saque excede o limite.")
    elif saque_excedido:
        print("Número de saques excedido. Em caso de dúvida entre em contato com a central do banco")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
        return saldo, extrato #Retorna saldo e extrato (Não esquecer)

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def user_create(usuarios):
    usuario = filtrar_usuario(cpf, usuarios)
    cpf = input("Informe o CPF (Apenas Números): ")

    if usuario:
        print("Usuário existente! Por gentileza tente novamente")
        return 
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereco (Rua, numero - bairro - cidade/UF do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado!")

def filtrar_usuario(cpf, usuarios):
    filtro_usuarios = [usuario for usuario in usuarios if usuarios ["cpf"] == cpf]
    return filtro_usuarios[0] if filtro_usuarios else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def menu_1():
    SAQUES_LIMITES = 2
    AGENCIA = "0008"

    saldo = 8300
    limite = 1200
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Por favor, informe o valor de depósito: "))
            
        elif opcao == "2":
            valor = float(input("Por favor, informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                saques_limites=SAQUES_LIMITES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            user_create(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione a opção correta!")


menu_1()