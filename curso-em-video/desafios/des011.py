h = float(input('Digite a altura da parede em metros:'))
w = float(input('Digite a largura da parede em metros:'))
a = h * w
q = a / 2
print('A área da parede equivale a {:.2f}m² e você precisará de {:.2f}l de tinta para pintá-la.' .format(a, q))
