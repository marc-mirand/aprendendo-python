nome = str(input('Digite seu nome completo:')).title().strip()
n = nome.split()
print('Muito prazer em conhecer você {} {}!'.format(n[0], n[len(n)-1]))
