while True:
  nome = input('Informe o nome ou 0 para sair: ')
  if nome == '0':
      break
      
  if nome in agenda:
    telefones = agenda.get(nome)

    while True:
      telefone = input('Informe novo telefone: ')
      print('O novo número cadastrado é {}. Digite "1" \
      para confirmar e "0" para corrigir\n'.format(telefone))
      confirmar_telefone = int(input())

      if confirmar_telefone == 1:
        telefones.append(telefone)
        agenda[nome] = telefones
        print(f'\nTelefone adicionado com sucesso! A lista atualizada de\
          telefones de {nome} é: \n{agenda[nome]}')
        break
      else:
        print('Vamos tentar novamente!')
  else:
    print('Digite um nome cadastrado na agenda!')
