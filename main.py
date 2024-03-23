caminho_arquivo = r'C:\\Users\\Pichau\\Desktop\\cursoudemy\\cursoudemy\\'
caminho_arquivo += 'arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# obs: with open = abre e fecha o arq

# obs: ultilizar: end='', strip(), para questoes de espaçamento


with open(caminho_arquivo, 'w+') as arquivo: # leitura e escrita
    arquivo.write('linha 1\n') # escrevo no arquivo
    arquivo.write('linha 2\n')
    arquivo.writelines( # varias linhas
        ('linha 3\n',
         'linha 4\n',
         'linha 5\n'
         )
    )
    arquivo.seek(0,0) # 'mover o cursor'
    print(arquivo.read())
    print("Leitura de uma unica linha") # unica linha readline ( singular)
    print(arquivo.readline())

    print(' ')
    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

print("$" * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read()) # leitura( visualização do conteudo do arquivo)
