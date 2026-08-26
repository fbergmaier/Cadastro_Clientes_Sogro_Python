# Para transformar em um arquivo executável, usar o comando: 
# pyinstaller --onefile nome_do_arquivo.py

from dataclasses import dataclass
import sqlite3
import time
import os

def menu():
    print("\n\n--------------- MENU ---------------\n1. Adicionar um novo cliente\n2. Buscar um cliente\n3. Editar informacoes do cliente\n4. Excluir cliente\n5. Sair do programa\n------------------------------------")

def limpar():
    input("Pressione ENTER para voltar ao Menu Principal...")
    os.system('cls' if os.name == 'nt' else 'clear')

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
    email: str
    cpf: str
    senha: str

lista_clientes = []

conexao = sqlite3.connect("banco_clientes.db")
cursor = conexao.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                nome TEXT, 
                telefone TEXT, 
                email TEXT, 
                cpf TEXT, 
                senha TEXT, 
                cidade TEXT, 
                bairro TEXT, 
                rua TEXT, 
                numero INTEGER
                )
                """)

while True:
    menu()
    escolha = int(input("\n-> "))

    if escolha == 1:
        print("\nPara voltar ao Menu Principal, digite *\nInformacoes pessoais do cliente: ")
        Nome = input("Nome: ")
        if(Nome == "*"):
            limpar()
            continue
        comando = "SELECT * FROM clientes WHERE nome = ?"
        cursor.execute(comando, (Nome,))
        if cursor.fetchone() != None:
            print("Cliente ja cadastrado!")
            limpar()
            continue
        Telefone = input("Telefone: ")
        Email = input("Email: ")
        Cpf = input("CPF: ")
        Senha = input("Senha: ")
        print("\nInformacoes do endereco: ")
        Cidade = input("Cidade: ")
        Bairro = input("Bairro: ")
        Rua = input("Rua: ")
        while True:
            try:
                Numero = int(input("Numero: "))
                break
            except ValueError:
                print("Erro! Insira apenas numeros!")


        comando_sql = """
            INSERT INTO clientes (nome, telefone, email, cpf, senha, cidade, bairro, rua, numero)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

        valores = (Nome, Telefone, Email, Cpf, Senha, Cidade, Bairro, Rua, Numero)

        cursor.execute(comando_sql, valores)
        conexao.commit()
    
        print("\nCliente adicionado com sucesso!")
        limpar()

        
        
    if escolha == 2:
        name = input("\nPara voltar ao Menu Principal, digite *\nDigite o nome do cliente: \n-> ")
        if(name == "*"):
            limpar()
            continue
        comando = "SELECT * FROM clientes WHERE nome = ?;"
        cursor.execute(comando, (name,))
        resultado = cursor.fetchone()

        if resultado is not None:
            endereco = Endereco(cidade=resultado[5], bairro=resultado[6], rua=resultado[7], numero=resultado[8])
            cliente = Cliente(endereco_cliente=endereco, nome=resultado[0], telefone=resultado[1], email=resultado[2], cpf=resultado[3], senha=resultado[4])

            print("\nInformacoes do cliente: \nTelefone: ", cliente.telefone, "\nCPF: ", cliente.cpf, "\nSenha: ", cliente.senha, "\nCidade: ", cliente.endereco_cliente.cidade, "\nBairro: ", cliente.endereco_cliente.bairro, "\nRua: ", cliente.endereco_cliente.rua, "\nNumero: ", cliente.endereco_cliente.numero)
            limpar()
        else:
            print("\nCliente nao encontrado")
            limpar()


        
    if escolha == 3: 
        name = input("\nPara voltar ao Menu Principal, digite *\nInsira o nome do cliente: \n-> ")
        if(name == "*"):
            limpar()
            continue
        mudar = input("\nEscolha entre: nome, telefone, email, cpf, senha, endereco\nQual informacao deseja alterar?\n-> ")
        
        if mudar == "nome":
            info = input("\nQual o novo nome?\n-> ")
            comando = "UPDATE clientes SET nome = ? WHERE nome = ?"
            valores = (info, name)
            cursor.execute(comando, valores)
            conexao.commit()
            limpar()

        elif mudar == "telefone":
            info = input("\nQual o novo telefone?\n-> ")
            comando = "UPDATE clientes SET telefone = ? WHERE nome = ?"
            valores = (info, name)
            cursor.execute(comando, valores)
            conexao.commit()
            limpar()

        elif mudar == "email":
            info = input("\nQual o novo email?\n-> ")
            comando = "UPDATE clientes SET email = ? WHERE nome = ?"
            valores = (info, name)
            cursor.execute(comando, valores)
            conexao.commit()
            limpar()

        elif mudar == "cpf":
            info = input("\nQual o novo CPF?\n-> ")
            comando = "UPDATE clientes SET cpf = ? WHERE nome = ?"
            valores = (info, name)
            cursor.execute(comando, valores)
            conexao.commit()
            limpar()

        elif mudar == "senha": 
            info = input("\nQual a nova senha?\n-> ")
            comando = "UPDATE clientes SET senha = ? WHERE nome = ?"
            valores = (info, name)
            cursor.execute(comando, valores)
            conexao.commit()
            limpar()

        elif mudar == "endereco":
            cidade = input("\nQual a nova cidade?\n-> ")
            bairro = input("Qual o novo bairro?\n-> ")
            rua = input("Qual a nova rua?\n-> ")
            while True:
                try:
                    numero = int(input("Qual o novo numero?\n-> "))
                    break
                except ValueError:
                    print("Erro! Insira apenas numeros!")
                    
            comando = "UPDATE clientes SET cidade = ?, bairro = ?, rua = ?, numero = ? WHERE nome = ?"
            valores = (cidade, bairro, rua, numero, name)
            cursor.execute(comando, valores)
            conexao.commit()
            limpar()

        if cursor.rowcount == 0:
            print("\nCliente nao encontrado!")
            limpar()
            continue
        

    if escolha == 4:
        name = input("\nPara voltar ao Menu Principal, digite *\nInsira o nome do cliente: \n-> ")
        if(name == "*"):
            limpar()
            continue
        comando = "DELETE FROM clientes WHERE nome = ?"
        cursor.execute(comando, (name,))
        conexao.commit()
        if cursor.rowcount == 0:
            print("\nCliente nao encontrado!")
        else:
            print("\nCliente excluido com sucesso")

        limpar()

    if escolha == 5:
        cursor.close()
        conexao.close()
        print("\nAguarde.. Salvando informacoes no Banco de Dados")
        time.sleep(2)
        print("Arquivos salvos com sucesso!")
        break