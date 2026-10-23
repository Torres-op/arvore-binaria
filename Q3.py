# Q3 — Tabela de símbolos: BUSCA domina, ordem imprevisível
from arvore_avl import ArvoreAVL
from arn import ArvoreRubroNegra

chaves = [50,30,70,20,40,60,80,10,25,35,55,65]

avl = ArvoreAVL()
for k in chaves: avl.inserir(k)

rn = ArvoreRubroNegra()
for k in chaves: rn.inserir(k)

print(f"AVL — altura: {avl.altura()} | rotações: {avl.rotacoes}")
print(f"RN  — altura: {rn.altura()} | rotações: {rn.rotacoes}")
