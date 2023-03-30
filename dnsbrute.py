import sys
import dns.resolver

argumentos = sys.argv	# lê os argumentos do comando
try:
    dominio = argumentos[1]
    lista = argumentos[2]
except:
    print("Faltam argumentos no comando")
    sys.exit(1)

# abre a wordlist
try:
    arquivo = open(lista)
    linhas = arquivo.read().splitlines()
except:
    print("Arquivo nao encontrado ou inválido")
    sys.exit(1)

# para cada linha da wordlist, testa o dns
for linha in linhas:
    subdominio = linha + '.' + dominio
    try:
        respostas = dns.resolver.query(subdominio, 'a')
        for resultado in respostas:
            print(subdominio, resultado)
    except:
        pass
