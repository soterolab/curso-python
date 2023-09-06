# Exercício: https://python.nilo.pro.br/exercicios3/capitulo%2004/exercicio-04-10.html

## Solução 1
while(True):
    consumo_kWh = float(input('Informe a quantidade de kWh consumida:\n' ))
    tipo_instalacao = input('Escolha a opção conforme o tipo de \
    Instalação:\nR - Residências\nI - Indústria\nC - Comércio:\n' )

    if tipo_instalacao == 'R':
      if consumo_kWh <= 180:
        custo = 0.50
      else:
          custo = 0.65
    elif tipo_instalacao == 'I':
      if consumo_kWh <= 1800:
        custo = 0.20
      else:
          custo = 0.35
    elif tipo_instalacao == 'C':
      if consumo_kWh <= 480:
        custo = 0.35
      else:
          custo = 0.50
    else:
      custo = 0
      print('Erro! Instalação Desconhecida! \nInforme uma Instalação válida!')

    if tipo_instalacao =='R' or tipo_instalacao =='I' or tipo_instalacao =='C':
      break

preco = custo*consumo_kWh
print('O valor da sua conta de energia esse mês será: R${:.2f}'.format(preco))

## Solução 2
while(True):
    consumo_kWh = float(input('Informe a quantidade de kWh consumida:\n' ))
    tipo_instalacao = input('Escolha a opção conforme o tipo de \
    Instalação:\nR - Residências\nI - Indústria\nC - Comércio:\n' )

    if tipo_instalacao == 'R':
      if consumo_kWh <= 180:
        custo = 0.50
      else:
          custo = 0.65
    elif tipo_instalacao == 'I':
      if consumo_kWh <= 1800:
        custo = 0.20
      else:
          custo = 0.35
    elif tipo_instalacao == 'C':
      if consumo_kWh <= 480:
        custo = 0.35
      else:
          custo = 0.50
    else:
      custo = 0
      print('Erro! Instalação Desconhecida! \nInforme uma Instalação válida!')
      continue

    preco = custo*consumo_kWh
    print('O valor da sua conta de energia esse mês será: R${:.2f}'.format(preco))
    break
