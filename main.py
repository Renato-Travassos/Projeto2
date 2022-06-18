def pedidocomida():
    c=input("digite comida:")
    pedido2.append(c)

pagamento=pergunta=valor=dinheiro=cont=total=final=comida=número=extra1=pedido1=0
pedidos=[[0],[1]]
cliente=list()
pedido2=[]
from random import randint
while True:  
 nome=input('\033[0m(digite "TOTAL" para os ganhos ou "L" para ver pedidos)\nnome do cliente:').upper()
 if nome =='TOTAL':
    print(f'Total de pedidos feitos{cont}\ntotal de ganho{total}')
 if nome == 'L':
    for d,i in cliente:
        print(f'Cliente{d} pedido{i}')
 pedidocomida()
 pedido=int(input('\033[0mInsira n o valor do pedido'))
 valor+=pedido
 número=randint(0,100)
 número='número:'+str(número)
 while True:
  pergunta=str(input('Finalizar pedido?[S/N]'))
  if pergunta in 'sS':
     pedidos[1]=pedido2[:] 
     pedidos[0]=(nome,número,pedido)
     pedido2.clear()
     break
     print('pedido finalizado')
  elif pergunta in 'nN':
     pedidocomida()
     pedido1=int(input('Insira o valor deste pedido '))
     pedido+=pedido1
 print(f'o pedido do cliente {nome} {número} deu {pedido}')
 while True:
  pagamento=int(input('Dinheiro==0 ou cartão==1 cancela==2'))
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
     cliente.append(pedidos.copy())
     print(f'pagamento feito\no pedido da(o) cliente {nome} número {número} já está a caminho')
     total+=pedido
     cont+=1
     break
  if pagamento==2:
     print('cancelado')
     break
