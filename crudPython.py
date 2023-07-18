# Função para exibir as motos do registro
def exibir_motos(motos):
    if not motos:
        print("Nenhuma moto encontrada.")
    else:
        for moto in motos:
            print(moto)

# Função para adicionar uma moto no registro
def adicionar_moto(motos):
    marca = input("Digite a marca da moto: ")
    modelo = input("Digite o modelo da moto: ")
    cor = input("Digite a cor da moto: ")
    ano = input("Digite o ano da moto: ")
    km = input("Digite a quilometragem da moto: ")
    nova_moto = {"Marca": marca, "Modelo": modelo, "Cor": cor, "Ano": ano, "Quilometragem": km}
    motos.append(nova_moto)
    print("Moto adicionada com sucesso!")

# Função para atualizar uma moto no registro
def atualizar_moto(motos):
    modelo = input("Digite o modelo da moto a ser atualizada: ")
    for moto in motos:
        if moto["Modelo"] == modelo:
            marca = input("Digite a nova marca: ")
            cor = input("Digite a nova cor: ")
            ano = input("Digite o novo ano: ")
            km = input("Digite a nova quilometragem: ")
            moto["Marca"] = marca
            moto["Cor"] = cor
            moto["Ano"] = ano
            moto["Quilometragem"] = km
            print("Moto atualizada com sucesso!")
            return
    print("Moto não encontrada.")

# Função para excluir uma moto no registro
def excluir_moto(motos):
    modelo = input("Digite o modelo da moto a ser excluída: ")
    for moto in motos:
        if moto["Modelo"] == modelo:
            motos.remove(moto)
            print("Moto excluída com sucesso!")
            return
    print("Moto não encontrada.")

# Lista para armazenar as motinhas no registro
motos = []

# Menu das opções
while True:
    print("\n======= LOJA DE MOTOS =======")
    print("1 - Exibir motos")
    print("2 - Adicionar moto")
    print("3 - Atualizar moto")
    print("4 - Excluir moto")
    print("0 - Sair")
    print("\n======= SEM GARANTIA =======")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        exibir_motos(motos)
    elif opcao == "2":
        adicionar_moto(motos)
    elif opcao == "3":
        atualizar_moto(motos)
    elif opcao == "4":
        excluir_moto(motos)
    elif opcao == "0":
        break
    else:
        print("Opção inválida! Tente novamente!")

