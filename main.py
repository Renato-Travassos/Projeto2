from cardapio import pratos
pagamento=pergunta=valor=dinheiro=cont=total=pedido2=final=0
from random import randint
while True:
 cliente=list()
 nome=str(input('\033[0m(digite "TOTAL" para os ganhos)\nnome do cliente:'))
 if nome=='TOTAL':
    print(f'Total de pedidos feitos{cont}\ntotal de ganho{total}')
 pratos()
 pedido=int(input('\033[0mInsira  o valor do pedido'))
 valor+=pedido
 número=randint(0,100)
 cliente.append([nome,[pedido,número]])
 print(f'o pedido da(o) cliente {nome} já está a caminho')
 while True:
  pergunta=str(input('Finalizar pedido?[S/N]')).upper()[0]
  if pergunta=='S':
     break
     print('pedido finalizado')
  elif pergunta=='N':
     pedido2=int(input('Insira o que pediram'))
     pedido+=pedido2
 print(f'o pedido do cliente {nome}{número} deu {pedido}')
 while True:
  pagamento=int(input('Dinheiro==0 ou cartão==1 cancela==3'))
  if pagamento==0:
    dinheiro=int(input('insira o valor'))
    if dinheiro>=pedido:
     print(f'o valor foi de {pedido}')
     total+=pedido
     cont+=1
     dinheiro=pedido-dinheiro
     print(f'troco de {dinheiro}')
     break
    else:
     print('\033[0;31mErro,dinheiro insuficiente')
  if pagamento==1:
     print('pagamento feito')
     total+=pedido
     cont+=1
     break
  if pagamento==3:
     break
  print('indo ao próximo pedido...')