RED, BLACK = 0, 1

class No:
    def __init__(self, chave):
        self.chave = chave; self.cor = RED
        self.esq = self.dir = self.pai = None

class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(None); self.NIL.cor = BLACK
        self.raiz = self.NIL
        self.rotacoes = 0

    def _rot_esq(self, x):
        self.rotacoes += 1
        y = x.dir; x.dir = y.esq
        if y.esq != self.NIL: y.esq.pai = x
        y.pai = x.pai
        if x.pai is None: self.raiz = y
        elif x == x.pai.esq: x.pai.esq = y
        else: x.pai.dir = y
        y.esq = x; x.pai = y

    def _rot_dir(self, x):
        self.rotacoes += 1
        y = x.esq; x.esq = y.dir
        if y.dir != self.NIL: y.dir.pai = x
        y.pai = x.pai
        if x.pai is None: self.raiz = y
        elif x == x.pai.dir: x.pai.dir = y
        else: x.pai.esq = y
        y.dir = x; x.pai = y

    def inserir(self, chave):
        novo = No(chave); novo.esq = novo.dir = self.NIL
        pai, atual = None, self.raiz
        while atual != self.NIL:
            pai = atual
            atual = atual.esq if chave < atual.chave else atual.dir
        novo.pai = pai
        if pai is None: self.raiz = novo
        elif chave < pai.chave: pai.esq = novo
        else: pai.dir = novo
        self._corrigir(novo)

    def _corrigir(self, z):
        while z.pai and z.pai.cor == RED:
            avo = z.pai.pai
            if z.pai == avo.esq:
                tio = avo.dir
                if tio.cor == RED:
                    z.pai.cor = tio.cor = BLACK
                    avo.cor = RED; z = avo
                else:
                    if z == z.pai.dir:
                        z = z.pai; self._rot_esq(z)
                    z.pai.cor = BLACK; avo.cor = RED
                    self._rot_dir(avo)
            else:
                tio = avo.esq
                if tio.cor == RED:
                    z.pai.cor = tio.cor = BLACK
                    avo.cor = RED; z = avo
                else:
                    if z == z.pai.esq:
                        z = z.pai; self._rot_dir(z)
                    z.pai.cor = BLACK; avo.cor = RED
                    self._rot_esq(avo)
        self.raiz.cor = BLACK

    def altura(self, n=None, _init=True):
        if _init: n = self.raiz
        if n == self.NIL: return 0
        return 1 + max(self.altura(n.esq, False), self.altura(n.dir, False))

rn = ArvoreRubroNegra()