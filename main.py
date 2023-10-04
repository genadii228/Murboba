x = int(input('Vvedite pervoe cislo = '))
y = int(input('Vvedite vtoroe cislo = '))

deistv = input('Vvedite deistvie - ')

if deistv == '+':
    print(x + y)
elif deistv == '-':
    print(x - y)
elif deistv == '/':
    print(x / y)
elif deistv == '*':
    print(x * y)
else:
    print('ya tebya ne ponyal')
