# Q1 — Catálogo de produtos: carga de BUSCA, inserção ordenada
from arvore_avl import ArvoreAVL

chaves = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]

avl = ArvoreAVL()
for k in chaves:
    avl.inserir(k)

print(f"AVL — altura: {avl.altura()} | rotações: {avl.rotacoes} | n = {len(chaves)}")
print(f"Altura ótima (log2 n ≈): {len(chaves).bit_length()-1}")
print(f"Busca: {avl.buscar(100)} | {avl.buscar(999)}")
