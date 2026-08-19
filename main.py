# Para transformar em um arquivo executável, usar o comando: 
# pyinstaller --onefile nome_do_arquivo.py

from dataclasses import dataclass

def menu():
    print("\n\n--------------- MENU ---------------\n1. Adicionar um novo cliente\n2. Buscar um cliente\n3. Editar informacoes do cliente\n4. Excluir cliente\n5. Sair do programa\n------------------------------------")

@dataclass
class Endereco:
    cidade: str
    bairro: str
    rua: str
    numero: int
@dataclass
class Cliente:
    endereco_cliente: Endereco
    nome: str
    telefone: str
    cpf: str
    senha: str

def buscarCliente(vetor):
    name = input("\nDigite o nome do cliente: ")
    for clientes in vetor:
        if clientes.nome == name:
            print("\nCliente encontrado!")
            return clientes
        else:
            print("\nCliente nao encontrado")
            return None

lista_clientes = []

while True:
    menu()
    escolha = int(input("\n-> "))

    if escolha == 1:
        print("\nInformacoes pessoais do cliente: ")
        Nome = input("Nome: ")
        Telefone = input("Telefone: ")
        Cpf = input("CPF: ")
        Senha = input("Senha: ")
        print("\nInformacoes do endereco: ")
        Cidade = input("Cidade: ")
        Bairro = input("Bairro: ")
        Rua = input("Rua: ")
        Numero = int(input("Numero: "))
    
        endereco = Endereco(cidade=Cidade, bairro=Bairro, rua=Rua, numero=Numero)
        cliente = Cliente(nome=Nome, telefone=Telefone, cpf=Cpf, senha=Senha, endereco_cliente=endereco)

        lista_clientes.append(cliente)

        print("\nCliente adicionado com sucesso!")
        
    if escolha == 2:
        name = input("\nDigite o nome do cliente: ")
        for clientes in lista_clientes:
            if clientes.nome == name:
                print("\nInformacoes do cliente: \nTelefone: ", clientes.telefone, "\nCPF: ", clientes.cpf, "\nSenha: ", clientes.senha, "\nCidade: ", clientes.endereco_cliente.cidade, "\nBairro: ", clientes.endereco_cliente.bairro, "\nRua: ", clientes.endereco_cliente.rua, "\nNumero: ", clientes.endereco_cliente.numero)

    if escolha == 3: 
        name = input("\nDigite o nome do cliente: ")
        for clientes in lista_clientes:
            if clientes.nome == name:
                mudar = input("\nQual informacao deseja alterar (Tudo em minusculo)? ")
                if mudar == "nome":
                    info = input("\nQual o novo nome? ")
                    clientes.nome = info
                    break

                elif mudar == "telefone":
                    info = input("\nQual o novo telefone? ")
                    clientes.telefone = info
                    break

                elif mudar == "cpf":
                    info = input("\nQual o novo CPF? ")
                    clientes.cpf = info
                    break

                elif mudar == "senha": 
                    info = input("\nQual a nova senha? ")
                    clientes.senha = info
                    break

                elif mudar == "endereco":
                    clientes.endereco_cliente.cidade = input("\nQual a nova cidade? ")
                    clientes.endereco_cliente.bairro = input("Qual o novo bairro? ")
                    clientes.endereco_cliente.rua = input("Qual a nova rua? ")
                    clientes.endereco_cliente.numero = int(input("Qual o novo numero?"))
                break
            else:
                print("\nCliente nao encontrado!")

    if escolha == 4:
        name = input("\nDigite o nome do cliente: ")
        for clientes in lista_clientes:
            if clientes.nome == name:
                lista_clientes.remove(clientes)
                break
            else:
                print("\nCliente nao encontrado!")

    if escolha == 5:
        break
