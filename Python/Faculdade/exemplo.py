

#clientes_produto_x = {'C1', 'C2', 'C3', 'C4', 'C5', 'C6'}
#clientes_produto_y = {'C4', 'C5', 'C7', 'C8'}

#intersecao = clientes_produto_x & clientes_produto_y
#apenas_x = clientes_produto_x - clientes_produto_y
#apenas_y = clientes_produto_y - clientes_produto_x
#todos_clientes = clientes_produto_x | clientes_produto_y

#print ("Clientes que utilizam os dois produtos:", intersecao)
#print ("Clientes que usam apenas o produto X:",apenas_x)
#print ("Clientes que usam apenas o produto Y:",apenas_y)
#print ("Todos os clientes:",todos_clientes)

personagens_com_cabelo_curto = {'Shane', 'Harvey', 'Lewis', 'Linus', 'Kent'}
personagens_com_cabelo_curto_nao_casaveis= {'Lewis', 'Linus', 'Kent'}

intersecao = personagens_com_cabelo_curto & personagens_com_cabelo_curto_nao_casaveis
apenas_casaveis= personagens_com_cabelo_curto - personagens_com_cabelo_curto_nao_casaveis
naocasa= personagens_com_cabelo_curto_nao_casaveis - personagens_com_cabelo_curto
todos_personagens= personagens_com_cabelo_curto | personagens_com_cabelo_curto_nao_casaveis

print ("Personagens  com cabelo curto que nao sao casaveis e tem cabelo curto:", intersecao)
print ("Apenas personagens casáveis:", apenas_casaveis)
print ("Não casáveis:", naocasa)
print ("Todos os personagens, seja casável ou não casável:", todos_personagens)

