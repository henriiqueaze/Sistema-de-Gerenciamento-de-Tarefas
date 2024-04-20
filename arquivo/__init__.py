def Arquivo_Existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True


def Criar_Arquivo(nome):
    a = open(nome, 'wt+')
    a.close()




