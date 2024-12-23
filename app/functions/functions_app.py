from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime
from config.database import Session
from cryptography.fernet import Fernet
import pwinput as pin
from os import system
from time import sleep

branco = "\033[97m"
cor = "\033[31m"
limpar = system("cls||clear")
reset = "\033[0m"

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    return chave

chave = carregar_chave()
cipher = Fernet(chave)

def senha():
    senha = pin.pwinput(f"{branco}Senha: {reset}")
    senha_seg = criptografia(senha)
    return senha_seg

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

def criptografia(texto):
    texto_criptografado = cipher.encrypt(texto.encode("utf-8"))
    return texto_criptografado

def descriptografia(texto):
    if texto is None:
        raise ValueError("Senha não pode ser None!")
    if isinstance(texto, str):
        texto = texto.encode("utf-8")
    try:
        return cipher.decrypt(texto).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Erro na descriptografia: {e}")

def descricao():
    descricao = input(f"{branco}Descrição: {reset}")  # Entrada para a descrição
    data = datetime.now()  # Obtém a data/hora atual
    dados = ("Data/Hora: ", data, "Descrição: ", descricao)

    dados_formatados = " ".join(map(str, dados))  # Junta os dados em uma string
    return dados_formatados  # Retorna a string formatada

def cadastro_itens():
    while True:
        nome = input(f"{branco}Nome: {reset}")
        if verificar_item(nome):  # Verifica se o item já existe
            print(f"{cor}Erro, o item já existe.{reset}")
        else:
            break
    descricao_item = descricao()  # Chama a função para obter a descrição formatada
    matricula = input(f"{branco}Matrícula do Funcionário: {reset}")  # Captura matrícula do funcionário
    while True:
        quantidade = input(f"{branco}Quantidade: {reset}")
        if quantidade.isnumeric():  # Verificação correta para garantir que quantidade seja numérica
            quantidade = int(quantidade)
            break
        else:
            print(f"{cor}Apenas números{reset}")
    localizacao_garagem = input(f"{branco}Localização da Garagem: {reset}")  # Adicionada a captura da localização da garagem
    # Chama o serviço para criar o item, passando os parâmetros corretos
    service.criando_item(nome, descricao_item, matricula, localizacao_garagem, quantidade)

def cadastro_garagens():
    nome = str(input(f"{branco}Nome: {reset}"))
    while True:
        localizacao = str(input(f"{branco}Endereço: {reset}"))
        if verificar_garagem(localizacao):
            print(f"{cor}Erro! Garagem já cadastrada{reset}")
        else:
            break
    adicionais = input("Dados Adicionais")

    service.criando_garagem(nome,localizacao,adicionais)

def senha1():
    while True:
        senha = input(f"{branco}Senha: {reset}")
        senha1 = input(f"{cor}Digite a senha novamente: {reset}")
        if senha == senha1:
            senha = criptografia(senha)
            break
        else:
            print(f"{cor}As senhas não são iguais, informe senhas iguais para prosseguir.{reset}")
    return senha

def cadastrando_funcionario():
    nome = str(input(f"{branco}Nome: {reset}"))
    while True:
        matricula = str(input(f"{branco}Matricula: {reset}")).strip()
        if matricula.isnumeric:
            matricula = str(matricula)
            if verificar_funcionario(matricula):
                print(f"{cor}Funcionario já cadastrado!{reset}")
            else:
                break
        else:
            print(f"{cor}Matricula inválida, digite apenas números!{reset}")
    senha = senha1()
    service.criando_funcionario(nome, matricula, senha)

def verificar_funcionario(a):
    funcionario = repository.pesquisar_funcionario(a)
    return funcionario is not None

def verificar_garagem(a):
    funcionario = repository.pesquisar_garagem(a)
    return funcionario is not None

def verificar_item(a):
    funcionario = repository.pesquisar_item(a)
    return funcionario is not None

def menu():
    print(f"""
{branco}1 - Cadastros 
2 - Solicitações
3 - Histórico de Movimentações
4 - Sair{reset}
""")
    
def menu_cadastro():
    print(f"""
{branco}1 - Funcionario
2 - Garagem
3 - Item{reset}
""")

def solicitacao_item():
    print("""
1 - SOLICITAR
2 - SAIR
""")
    
def criando_arquivo_final(a, b):
    with open(a, "w") as arquivo_dados:
        for dado in b:
            arquivo_dados.write(f"{dado}")  # Sem vírgula ou quebra de linha extra
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")



def lendo_arquivo_final(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo_dados:
            dados = arquivo_dados.readlines()  # Lê as linhas do arquivo
            print("\n=== Dados Lidos ===\n")
            for linha in dados:
                linha = linha.strip()  # Remove quebras de linha e espaços extras
                campos = linha.split(",")  # Exemplo: Se os dados estiverem separados por vírgulas
                print(campos)  # Imprime a lista com os dados divididos
            return dados  # Retorna os dados lidos
    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")



def solicitacao():
    while True:
        matricula = str(input("Matrícula: "))
        if matricula.isnumeric():  # Chamada correta do is_numeric()
            funcionario = repository.pesquisar_funcionario(matricula)
            dig_senha = str(input("Senha: "))
            if descriptografia(funcionario.senha) == dig_senha:
                print(f"=== SEJA BEM VINDO {funcionario.nome} ===")
                while True:
                    solicitacao_item()  # Supondo que esta função exibe um menu ou algo do tipo
                    opcao = input(": ")
                    match opcao:
                        case "1":
                            while True:
                                codigo = str(input("Código: "))
                                cod_cod = repository.pesquisar_item(codigo)
                                print(f"Nome: {cod_cod.nome} | Quantidade: {cod_cod.quantidade} | Descrição: {cod_cod.descricao}")
                                solicitacao = input("Deseja solicitar o item? \n1-Sim \n2-Não: ")
                                if solicitacao == "1":
                                    garagem = str(input("Informe para qual garagem: "))
                                    gar = repository.pesquisar_garagem(garagem)
                                    # Comparação correta de garagem
                                    if garagem.strip().lower() == gar.localizacao.strip().lower():
                                        while True:
                                            quantidade = str(input("Quantidade desejada: "))
                                            if quantidade.isnumeric():
                                                quantidade = float(quantidade)  # Convertendo para float
                                                dados = ['Funcionario:', funcionario.nome, 'Garagem:', gar.nome, 'Item:', cod_cod.nome, 'Qtd. Solicitada:', quantidade]
                                                
                                                # Certifique-se de que 'dados' seja uma string antes de criptografar
                                                dados_formatados = str(dados)  # Converte a lista para uma string
                                                dados_criptografados = criptografia(dados_formatados)  # Chama a criptografia com string formatada
                                                
                                                arquivo = "Historico.txt"
                                                criando_arquivo_final(arquivo, dados_criptografados)
                                                print("O item será entregue em breve!")
                                                print(dados_formatados)
                                                sleep(10)
                                            else:
                                                print("Somente números são aceitos!")
                                    else:
                                        print("Garagem não encontrada!")
                                else:
                                    break
                        case "2":
                            break
                        case "_":
                            print("Opção inválida!")
                            sleep(2)

def historico():
    dados_cripitografados = lendo_arquivo_final("Historico.txt")  # Agora isso retorna os dados
    
    # Verifica se os dados são uma lista e os transforma em uma string
    if isinstance(dados_cripitografados, list):
        dados_cripitografados = "".join(dados_cripitografados)  # Converte para string
    
    if dados_cripitografados:  # Verifica se os dados não são None ou vazios
        try:
            dados_descriptografados = descriptografia(dados_cripitografados)  # Descriptografa os dados
            print(dados_descriptografados)  # Exibe os dados descriptografados
        except ValueError as e:
            print(f"Erro na descriptografia: {e}")
    else:
        print("Erro ao ler os dados do arquivo.")
    
    sleep(10)

