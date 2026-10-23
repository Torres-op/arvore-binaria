# Análise Assintótica — Questionário de Árvores Balanceadas

## Fundamentos

Tanto AVL quanto Rubro-Negra garantem **altura O(log n)** e, portanto:

- **Carga de BUSCA** → queremos **menor altura** → **AVL** (mais rígida, árvore mais "achatada").
- **Carga de ESCRITA** → queremos **menos rotações por inserção** → **Rubro-Negra**.

---

## Questão 1 — Catálogo de produtos: **AVL**

- **Carga:** busca milhares de vezes/minuto, inserção 1×/dia, chaves chegam ordenadas.
- **Altura:** para n=15, AVL atinge altura 4, contra a árvore RN podendo chegar a 8.
- **Rotações:** AVL faz apenas **um balanceamento** pela manhã, com n rotações. RN faz menos rotações na carga, mas isso é irrelevante frente ao custo permanente de busca.
- **Custo amortizado:** a economia de rotações do RN na carga não compensa o custo extra de **cada** busca durante o dia.
- **Decisão:** **AVL** minimiza altura, logo, minimiza comparações por busca.

---

## Questão 2 — Log de eventos Mumbuca: **Rubro-Negra**

- **Carga:** inserção a cada poucos ms (milhares/dia), relatório 1×/dia, timestamps **crescentes**.
- **Rotações:** inserção sempre à direita. Uma árvore AVL iria fazer muitos rebalanceamentos gerando rotações em cascata, a árvore RN faz ≤2 rotações por inserção.
- **Custo amortizado:** com N inserções, AVL pode fazer O(N log N) rotações no total, RN faz O(N) rotações totais (amortizado O(1) por inserção).
- **Busca rara:** a altura maior do RN é irrelevante quase não se busca.
- **Decisão:** **Rubro-Negra** escrita mais barata faz ele ser mais eficiente.

---

## Questão 3 — Tabela de símbolos: **AVL**

- **Carga:** inserção só na montagem (ordem **imprevisível**), busca intensa depois.
- **Altura:** AVL é mais balanceada, sua altura fica menor em comparação com a RN. Em média, AVL tem ~1 nível a menos.
- **Rotações:** a montagem é única, o custo extra de rotações do AVL é pago uma vez. O ganho em busca é permanente.
- **Decisão:** **AVL** de busca domina o ciclo de vida.

---

## Questão 4 — Índice de sessões: **Rubro-Negra**

- **Carga:** inserções e remoções constantes, buscas raras, IDs aleatórios.
- **Rotações:** com ordem aleatória, AVL ainda rebalanceia mais que RN. RN garante ≤2 rotações por inserção, AVL pode fazer O(log n) no pior caso.
- **Custo amortizado:** RN tem custo de inserção menor em média quando há muitas escritas.
- **Decisão:** **Rubro-Negra** escrita domina.

---

## Questão 5 — Importação IPTU ordenada: **AVL**

- **Carga:** importação 1× (dados já ordenados), consulta permanente o dia todo.
- **Degeneração:** sem balanceamento, BST vira lista O(n). Ambas corrigem, mas AVL fica mais achatada em comparação com RN.
- **Rotações na carga:** ambas rotacionam bastante na importação ordenada, mas isso ocorre apenas uma vez. Após carregada, só há busca, logo, altura menor vence.
- **Decisão:** **AVL** o custo de carga é amortizado pelas consultas permanentes.

---

## Questão 6 — Fila do escalonador: **Rubro-Negra**

- **Carga:** dezenas de milhares de inserções/segundo, busca quase nunca.
- **Rotações:** cada rotação é tempo de CPU roubado. RN: ≤2 rotações/inserção, amortizado O(1). AVL: pode fazer O(log n) rotações/inserção.
- **Evidência real:** o kernel Linux usa **red-black trees** no escalonador CFS (`rbtree`), exatamente por esse motivo.
- **Decisão:** **Rubro-Negra**  escrita extrema é o gargalo.