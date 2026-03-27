v1 = v2 = o = 0
continuar = 1
while True:
    print('-=-' * 15)
    print ('[CALCULADORA]')
    print('-=' * 10)
    v1 = float(input('digite o primeiro valor: ').strip())
    print('-=' * 10)
    v2 = float(input('digite o segundo valor: ').strip())
    print('-=' * 10)
    print('[1]Soma\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n[5]Potenciação\n[6]SAIR')
    o = int(input('qual a operação a ser feita? ').strip())
    if o == 1:
        print('a soma entre {} e {} é igual a : {}'.format(v1, v2, v1 + v2))
    elif o == 2:
        print('a subtração entre {} e {} é igual a {}'.format(v1, v2, v1 - v2))
    elif o == 3:
        print('a multiplicação entre {} e {} é igual a {}'.format(v1, v2, v1 * v2))
    elif o == 4:
        if v2 != 0:
            print('a divisão entre {} e {} é igual a {}'.format(v1, v2, v1 / v2))
        else:
            print('a divisão por zero não existe')
    elif o == 5:
        print('{} elevado a {} potência é igual a : {}'.format(v1, v2, v1 ** v2))
    elif o == 6:
        print('espero ter ajudado   ')
    continuar = input('deseja continuar? [S/N] ').strip().lower()[0]
    if continuar == 'n':
        break
