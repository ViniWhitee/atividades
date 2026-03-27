print ("Exercício 1")
print()
caminho = str(input("Você está em uma floresta escolha um caminho para seguir (esquerda/direita) : "))

if caminho == 'esquerda':
    print ("Você chegou a um rio.")
    caminhoRio = str(input("Deseja atravessar ou voltar? (atravessar/voltar) : "))
    if caminhoRio == 'atravessar':
        print()
        print ("Você chegou a uma vila segura")
    elif caminhoRio == 'voltar':
        print()
        print ("Você permanece perdido na floresta!")
if caminho == 'direita':
    print ("Você encontrou uma montanha")
    print ()
    caminhoMountain = str(input("Deseja subir a montanha ou voltar? (subir/voltar) : "))
    if caminhoMountain == 'subir':
        print()
        print ("Você esncontrou um tesouro no topo da montanha. Parabéns!")
    elif caminhoMountain == 'voltar':
        print()
        print ("Você permanece perdido na floresta!")
        print ()
