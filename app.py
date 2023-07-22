from time import sleep


s = fecho = 0

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
        novoregistro = 'S'
        while novoregistro == 'S':
            nome = str(input('Nome do cliente: ')).strip()
            produto = str(input('Digite o produto: ')).strip()
            preco = float(input('Digite o preco: '))

            desc = str(input('Esse produto tem desconto? [S/N] : ')).strip().upper()
            if desc in 'S':
                desconto = float(input('Digite o desconto: '))
            else:
                desconto = 0
            print('Emitindo a factura...')
            sleep(3)
            print ('-=' * 20)
            print('SISTEMA DE FACTURACAO VERSAO 1.0')
            print ('-=' * 20)
            print('Nome: {} '.format(nome))
            print('Produto: {}' .format(produto))
            print('Desconto: {}' .format(desconto))
            n = (preco - desconto) + (preco * 0.14)
            fecho += n
            print('Total a pagar: {} Kz' .format(n))
            print('Acrescentando IVA de 14%')
            print('-=' * 20)
            print('OBRIGADO PELA PREFERENCIA')
            print('-=' * 20)
            novoregistro = str(input('Desejas registrar novamente uma compra? [S/N]: ')).upper().strip()

    if opcao == 2:
        nome = str(input('Nome do Cliente: ')).strip()
        while True:
            produto = str(input('Digite o produto: ')).strip()
            preco = float(input('Digite o preco: '))
            s += preco
            item = str(input('Adicionar mais um produto [S/N]: ')).upper().strip()
            if item == 'N':
                break

        print('Emtindo a factura...')
        sleep(2)
        print()
        print ('-=' * 20)
        print('SISTEMA DE FACTURACAO VERSAO 1.0')
        print ('-=' * 20)
        print('Nome: {}' .format(nome))
        print('Produtos: Variados')
        print('Total a pagar: {}' .format(s))
        print('Sem aplicacao do IVA')
        print('-'*20)
        print('OBRIGADO PELA PREFERENCIA')
        print('-'*20)
