from calendar import c
from operator import pos

# Script simples para resolver problema de trabalho de faculdade.

# Trabalho de faculdade, Intrução ao Python
# Criar um código que preveja a quantidade de peças que serão vendidas em um determinado mês com base nas vendas apresentadas em gráfico.

# Dados de peças vendidas nos últimos meses salvos em variaveis.
janeiro = 200
fevereiro = 400
marco = 600
abril = 800
maio = 1000
junho = 1200

print('Para qual mês quer prever as vendas? ')

proxMes = input('Digite o número referente ao mês: ') # Entrada do dado do mês escolhido.

# if e else if para comparar o mês digitado com o dado referente ao mês salvo nas variáveis.
if proxMes == 'janeiro' or proxMes == 'Janeiro':
    print(f'No mês de janeiro foram vendidas {janeiro} peças')
    input('Digite alguma tecla para sair...')
elif proxMes == 'fevereiro' or proxMes == 'Fevereiro':
    print(f'No mês de fevereiro foram vendidas {fevereiro} peças.')
    input('Digite alguma tecla para sair...')
elif proxMes == 'março' or proxMes == 'Março':
    print(f'No mês de março foram vendidas {marco} peças')
    input('Digite alguma tecla para sair...')
elif proxMes == 'abril' or proxMes == 'Abril':
    print(f'No mês de março foram vendidas {abril} peças')
    input('Digite alguma tecla para sair...')
elif proxMes == 'maio' or proxMes == 'Maio':
    print(f'No mês de março foram vendidas {maio} peças')
    input('Digite alguma tecla para sair...')
elif proxMes == 'junho' or proxMes == 'Junho':
    print(f'No mês de março foram vendidas {junho} peças')
    input('Digite alguma tecla para sair...')
else: # Fim do programa.
    print('Nenhum mês foi selecionado.')
    input('Digite alguma tecla para sair...')