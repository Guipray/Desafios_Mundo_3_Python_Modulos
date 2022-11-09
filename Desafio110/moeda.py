def resumo(preço=0,aument=10,redu=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aument}% de aumento: \t{aumentar(preço, aument, True)}')
    print(f'{redu}% de redução: \t{diminuir(preço, redu, True)}')
    print('-' * 30)


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
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
