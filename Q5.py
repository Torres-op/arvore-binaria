# Q5 — Importação ordenada + consulta permanente → BUSCA domina
from arvore_avl import ArvoreAVL
from arn import ArvoreRubroNegra

chaves = [1,2,3,4,5,6,7]

avl = ArvoreAVL()
for k in chaves: avl.inserir(k)
rn = ArvoreRubroNegra()
for k in chaves: rn.inserir(k)

print(f"AVL — altura: {avl.altura()} | rotações: {avl.rotacoes}")
print(f"RN  — altura: {rn.altura()} | rotações: {rn.rotacoes}")