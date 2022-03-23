from asyncio.windows_events import NULL
from distutils.log import error
from xmlrpc.client import Transport




def cadastra_vaca():
    racao = str(input("Qual o tipo de alimentação alimentação: "))
    vacincao = str(input("A vaca tomou a vacina resentimente: S/N")).upper().split()[0]
    com_filhote = input("A vaca está com filhote: S/N: ").upper()
    quant_producao = int(input("Digita a quantidade de letros produzido pela vaca: \n"))
    salvar = input("Deseja salvar os dados: S/N ").upper().split()[0]
    if salvar == "S":
        print("")
    else:
        print("ola")

    #Fazer o arquivamento dos dados:

    return print("Savamento completo:")

def mudar(resp):
    if (resp == "S"):
        resp = True
        return resp
    elif (resp == "N"):
        resp = False
        return resp


#fazer um Switch Case




sair = False
while ( sair == False):
   
   # Inicio de dados produçao: 
    numero_vacas = int(input("Digite a quantidade de vacas que voce possui: "))
    resp = mudar(str(input("Tem alguma que nao estão produzindo leite no momento? s/n \n")).split()[0].upper())
    if resp == True:
        vacas_restringidas = int(input("Digite a quantidade de vacas Restringidas: "))
        numero_vacas = numero_vacas - vacas_restringidas
    print(numero_vacas)
    #Calculo diário
        #Calculo Mensal

    #


    sair = mudar(str(input("Deseja encerrar o cadastro das vacas? s/n \n")).split()[0].upper())
    
    case

def gastos():
    val_tranporte = input

    return NULL



