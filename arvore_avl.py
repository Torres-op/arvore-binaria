# arvore_avl.py — AVL com contagem de rotações
class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esq = self.dir = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.rotacoes = 0

    def _alt(self, n):
        return n.altura if n else 0

    def _fator(self, n):
        return self._alt(n.esq) - self._alt(n.dir) if n else 0

    def _atualizar(self, n):
        n.altura = 1 + max(self._alt(n.esq), self._alt(n.dir))

    def _rot_dir(self, y):
        self.rotacoes += 1
        x = y.esq
        y.esq = x.dir
        x.dir = y
        self._atualizar(y); self._atualizar(x)
        return x

    def _rot_esq(self, x):
        self.rotacoes += 1
        y = x.dir
        x.dir = y.esq
        y.esq = x
        self._atualizar(x); self._atualizar(y)
        return y

    def _balancear(self, n):
        self._atualizar(n)
        f = self._fator(n)
        if f > 1:
            if self._fator(n.esq) < 0:
                n.esq = self._rot_esq(n.esq)
            return self._rot_dir(n)
        if f < -1:
            if self._fator(n.dir) > 0:
                n.dir = self._rot_dir(n.dir)
            return self._rot_esq(n)
        return n

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, n, chave):
        if not n:
            return NoAVL(chave)
        if chave < n.chave:
            n.esq = self._inserir(n.esq, chave)
        elif chave > n.chave:
            n.dir = self._inserir(n.dir, chave)
        else:
            return n
        return self._balancear(n)

    def altura(self):
        return self._alt(self.raiz)

    def buscar(self, chave):
        n = self.raiz
        while n:
            if chave == n.chave:
                return True
            n = n.esq if chave < n.chave else n.dir
        return False