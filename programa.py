sair = False
while ( sair == False):
    numero_vacas = int(input("Digite a quantidade de vacas que voce possui: "))
    resp = str(input("Tem alguma que estão em produçao no momento? s/n \n"))
    resp.upper
    if resp == "S":
        vacas_restringidas = int(input("Digite a quantidade de vacas Restringidas: "))
        numero_vacas = numero_vacas - vacas_restringidas
    print(numero_vacas)
    sair = str(input("Deseja encerrar o cadastro das vacas? s/n \n"))
    if sair == "S":
        sair = True
    #teste
    

