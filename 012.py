import time

produtos = {
    'Computador': 5000,
    'Mouse': 200,
    'Teclado': 340,
    'Monitor': 1200,
    'Cadeira': 800,
    'Mesa': 600 
    
}

outros_p = {
   'Teclado': 340,
   'Monitor': 1200,
   'Cadeira': 800,
   'Mesa': 600
}

desconto = 0.05

print('\n Bem vindo a nossa loja online!\n')
time.sleep(1)

while True:
    busca = input('Deseja ver a oferta do dia? (s/n): ')
    time.sleep(1)
    if busca == 's':
        oferta = list(produtos.items())[:2]
        print('\n Ofertas do Dia: ')
        time.sleep(1)
        for item, preço in oferta:
           preco_com_desconto = preço * (1 - desconto)
           print(f'-{item}: De R${preço:.2f} por apenas R${preco_com_desconto:.2f} )')
           time.sleep(1)
        oportunidade = input('Deseja comprar algum desses produtos? (s/n): ')
        time.sleep(1)
        if oportunidade == 's':
            escolha = input('Qual produto você deseja? ')
            time.sleep(1)
            if escolha in produtos:
               preco_final = produtos[escolha] * (1 - desconto)
               print(f'O preço com desconto do {escolha} é R${preco_final:.2f}')
               time.sleep(1)
               pagamento1 = input('Deseja finalizar a compra? (s/n): ')
               time.sleep(1)
               if pagamento1 == 's':
                   print('Envie o pagamento usando a chave pix: 12345678900')
                   time.sleep(1)
                   print('Aguarde a confirmação do pagamento...')
                   time.sleep(10)
                   confirmação = input('Você já realizou o pagamento? (s/n): ')
                   time.sleep(1)
                   if confirmação == 's':
                      print('O pagamento foi confirmado!')
                      time.sleep(10)
                      print('Obrigado por comprar conosco! Volte sempre!')
                      time.sleep(1)
                      break
                   elif confirmação == 'n':
                      print('Aguardando o pagamento...')
                      time.sleep(5)
                      print('Pagamento recebido.')
                      time.sleep(10)
                      print('Obrigado por comprar conosco! Volte sempre!')
                      time.sleep(1)
                      break
               else:
                   print('Compra cancelada.')
                   time.sleep(1)
                   outro_produto = input('Deseja ver outro produto? (s/n): ')
                   time.sleep(1)
                   if outro_produto == 's':
                      continue
                   else:
                      print('Tudo bem, volte sempre!')
            else:
               print('Não temos esse produto em oferta no momento.')
               time.sleep(1)
               outro_produto = input('Deseja ver outro produto? (s/n): ')
               time.sleep(1)
               if outro_produto == 's':
                  continue
               else:
                  print('Tudo bem volte sempre!')
                  break
    else:
        outros_p = print('Tudo bem, de uma olhada em nossos outros produtos: ')
        time.sleep(1)
        print(outros_p)
        time.sleep(1)
        oportunidade = input('Deseja comprar algum desses produtos? (s/n): ')
        time.sleep(1)
        if oportunidade == 's':
            escolha = input('Qual produto você deseja? ')
            time.sleep(1)
            if escolha in outros_p:
               preco = outros_p[escolha]
               print(f'O preço do {escolha} é R$ {preço:.2f}')
               time.sleep(1)
               pagamento1 = input('Deseja finalizar a compra? (s/n): ')
               time.sleep(1)
               if pagamento1 == 's':
                  pagamento2 = print('Envie o pagamento usando a chave pix: 12345678900')
                  time.sleep(1)
                  print('Aguarde a confirmação do pagamento...')
                  time.sleep(5)
                  confirmação = input('Você  já realizou o pagamento? (s/n): ')
                  time.sleep(2)
                  if confirmação == 's':
                     time.sleep(5)
                     print('Pagamento confirmado!')
                     time.sleep(5)
                     print('Obrigado por comprar conosco! Volte sempre!')
                     time.sleep(1)                 
                     break
                  elif confirmação == 'n':
                     print('Aguardando o pagamento... ')
                     time.sleep(3)
                     print('Pagamento recebido. ')
                     time.sleep(10)
                     print('Obrigado por comprar conosco! Volte sempre!')
                     time.sleep(1)
                     break
               else:
                  print('Compra cancelada.')
                  time.sleep(1)
                  outro_produto = input('Deseja ver outro produto? (s/n): ')
                  time.sleep(1)
                  if outro_produto == 's':
                     continue
                  else:
                     print('Tudo bem, volte sempre!')
                     break
            else:
               print('Não temos esse produto no momento.')
               time.sleep(1)
               outro_produto = input('Deseja ver outro pruduto? (s/n): ')
               time.sleep(1)
               if outro_produto == 's':
                  continue
               else:
                  print('Tudo bem, volte sempre!')
                  break
        else:
             print('Tudo bem, volte sempre!')
             break