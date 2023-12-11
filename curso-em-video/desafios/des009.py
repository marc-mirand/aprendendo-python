n = int(input('Digite um número inteiro:'))
i = 1
for i in range(0, 11):
    t = (n * i)
    print('{} x {} = {}' .format(n, i, t))
    i = i+1
