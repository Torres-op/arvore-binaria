# Q6 — Escalonador: ESCRITA extrema, caminho crítico, busca irrelevante
from arvore_avl import ArvoreAVL
from arn import ArvoreRubroNegra

chaves = [40,20,60,10,30,50,70,5,15,25,35,45]

avl = ArvoreAVL()
for k in chaves: avl.inserir(k)
rn = ArvoreRubroNegra()
for k in chaves: rn.inserir(k)

print(f"AVL — altura: {avl.altura()} | rotações: {avl.rotacoes}")
print(f"RN  — altura: {rn.altura()} | rotações: {rn.rotacoes}")