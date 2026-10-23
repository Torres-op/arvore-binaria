# Q4 — Índice de sessões: ESCRITA domina, ordem aleatória
from arvore_avl import ArvoreAVL
from arn import ArvoreRubroNegra

chaves = [42,17,63,9,28,55,74,3,21,38,50,70]

avl = ArvoreAVL()
for k in chaves: avl.inserir(k)
rn = ArvoreRubroNegra()
for k in chaves: rn.inserir(k)

print(f"AVL — altura: {avl.altura()} | rotações: {avl.rotacoes}")
print(f"RN  — altura: {rn.altura()} | rotações: {rn.rotacoes}")