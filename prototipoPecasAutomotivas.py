from calendar import c
from operator import pos

# Código em desenvolvimento.

# Trabalho de faculdade, Intrução ao Python
# Criar um código que preveja a quantidade de peças que serão vendidas em um determinado mês com base nas vendas atuais

c = 200

# Dados de peças vendidas nos últimos meses
jan = ' janeiro = ', 200
fev = ' fevereiro = ', 400
mar = ' março = ', 600
abril = ' abril = ', 800
maio = ' maio = ', 1000
jun = ' juho = ', 1200

vendas = [jan,fev,mar,abril,maio,jun]


ultimasVendas = input("Deseja ver os números das ultimas vendas de peças? ")

if ultimasVendas == 'Sim' or ultimasVendas == 'sim' or ultimasVendas == 's': # Assegura ao input que todas as opções de respostas positivas sejam aceitas.
    print(vendas) # Informa os dados de vendas anteriores.

    print('Para qual mês quer prever as vendas? ')
    proxMes = input('Digite o número referente ao mês: ')
    r = proxMes * c
    print(f'O mês {proxMes} vai ter uma estimativa de {r} peças.')
else:
    print('Para qual mês quer prever as vendas? ')
    proxMes = input('Digite o número referente ao mês: ')
    r2 = proxMes * c
    print(f'O mês {proxMes} vai ter uma estimativa de {r2} peças.')
