from asyncio.windows_events import NULL
from distutils.log import error
from msilib.schema import tables
from operator import index
from turtle import pd
from xmlrpc.client import Transport
import pandas as pd


def salvar_Xcel(dados):
    print(dados)
    dados.to_excel('Dados_Gastos.xls', index=False)
    print("Salvo com sucesso")




def cadastra_vaca():
    racao = str(input("Qual o tipo de alimentação alimentação: "))
    vacincao = str(input("A vaca tomou a vacina resentimente: S/N")).upper().split()[0]
    com_filhote = input("A vaca está com filhote: S/N: ").upper()
    quant_producao = int(input("Digita a quantidade de letros produzido pela vaca: \n"))
    salvar = mudar(input("Deseja salvar os dados: S/N ").upper().split()[0]) 
    
    if salvar == True:
        print()
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


#sair = False
#while ( sair == False):
   
   # Inicio de dados produçao: 
#    numero_vacas = int(input("Digite a quantidade de vacas que voce possui: "))
#    resp = mudar(str(input("Tem alguma que nao estão produzindo leite no momento? s/n \n")).split()[0].upper())
#    if resp == True:
#        vacas_restringidas = int(input("Digite a quantidade de vacas Restringidas: "))
#        numero_vacas = numero_vacas - vacas_restringidas
#    print(numero_vacas)
    #Calculo diário
        #Calculo Mensal

    #


def litros_pordia( numero_vacas_em_ordenha,alimetacao):
    if alimetacao == 'racao' :
        quanti_leite = numero_vacas_em_ordenha * 10
        print("A quantidade de leite que deverá ser produzida é de {}.".format(quanti_leite))
    elif alimetacao == 'pastagem':
        quanti_leite = numero_vacas_em_ordenha * 7
        print("A quantidade de leite que deverá ser produzida é de {}.".format(quanti_leite))
    

    
def cadastro_vacas():
    numero_vacas_total = int(input("Digite a quantidade de vacas que voce possui: "))
    resp = mudar(str(input("Tem alguma que nao estão produzindo leite no momento? s/n \n")).split()[0].upper())
    if resp == True:
        vacas_restringidas = int(input("Digite a quantidade de vacas Restringidas: "))
        numero_vacas = numero_vacas_total - vacas_restringidas
    


def gastos(sair = False):
    while (sair == False):
        nome_gasto = str(input("Digite o gasto: ops: \n *Alimentaçao\n *Trabalhadores\n *Transporte\n *Manutenção: "))
        quanto_gasta = float(input("Digite o valor do gasto no mês: "))
        qual_mes = str(input("Digite o mês do gasto: "))
        salvar = input("Deseja salvar os dados: S/N ").upper().split()[0]
        salvar = mudar(salvar)
        
        if  (salvar == True) :
            try:
                dados = pd.DataFrame(pd.read_excel("Dados_Gastos.xls"))
                print(dados)
                dados2 = pd.Series([nome_gasto,quanto_gasta,qual_mes], index=['Nome Gastos', 'Valor Gasto','Mês'])
                print(dados2)
                salvar_Xcel(dados.append(dados2,ignore_index= True))
            except :
                dados = pd.DataFrame([[nome_gasto, quanto_gasta,qual_mes]], index=['row 1'],columns=['Nome Gastos', 'Valor Gasto', 'Mês'])
                salvar_Xcel(dados)

        sair = mudar(str(input("Deseja encerrar o cadastro de Gastos? s/n \n")).split()[0].upper())

    


        
    return NULL



