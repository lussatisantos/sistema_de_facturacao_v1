print ('-=' * 20)
print('SISTEMA DE FACTURACAO VERSAO 1.0')
print ('-=' * 20)

opcao = 0

while opcao != 5:
    print('''
[ 1 ] Registrar uma compra
[ 2 ] Registrar uma lista de compras
[ 3 ] Fecho do dia
[ 4 ] Sobre o app
[ 5 ] Terminar
''')
    opcao = int(input('Digite a opcao da operacao: '))

    print ('-=' * 20)
    print('SISTEMA DE FACTURACAO VERSAO 1.0')
    print ('-=' * 20)

    if opcao == 1:
        produto = str(input('Digite o produto: '))
        preco = float(input('Digite o preco: '))
        
        promocao = str(input(''))