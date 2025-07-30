import random
import string

def obter_configuracoes():
    """
    Coleta as preferências do usuário para gerar a senha.
    Retorna um dicionário com tamanho e tipos de caracteres.
    """
    tamanho = int(input("Informe o tamanho da senha: "))
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    return {
        "tamanho": tamanho,
        "maiusculas": usar_maiusculas,
        "minusculas": usar_minusculas,
        "numeros": usar_numeros,
        "simbolos": usar_simbolos
    }

def construir_pool_caracteres(config):
    """
    Cria a lista de caracteres possíveis com base nas escolhas do usuário.
    """
    pool = ""
    if config["maiusculas"]:
        pool += string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if config["minusculas"]:
        pool += string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    if config["numeros"]:
        pool += string.digits           # 0123456789
    if config["simbolos"]:
        pool += string.punctuation      # !@#$%&*()

    if not pool:
        raise ValueError("Você precisa escolher ao menos um tipo de caractere!")

    return pool

def gerar_senha(pool, tamanho):
    """
    Gera a senha aleatoriamente usando a pool de caracteres.
    """
    senha = ''.join(random.choice(pool) for _ in range(tamanho))
    return senha

def main():
    """
    Função principal que organiza o processo de geração de senha.
    """
    try:
        config = obter_configuracoes()
        pool = construir_pool_caracteres(config)
        senha = gerar_senha(pool, config["tamanho"])
        print("\n🔐 Sua senha segura é:", senha)
    except ValueError as erro:
        print("Erro:", erro)

# Executa o programa
main()
