def aumentar(preço=0, taxa=0, show=False):
    res = preço + (preço * taxa/100)
    return res if show is False else moeda(res)


def diminuir(preço=0, taxa=0, show=False):
    res = preço - (preço * taxa/100)
    return res if show is False else moeda(res)


def dobro(preço=0, show=False):
    return preço*2 if show is False else moeda(preço*2)


def metade(preço=0, show=False):
    return preço/2 if show is False else moeda(preço/2)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
