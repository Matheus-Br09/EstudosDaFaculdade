identificador_de_consoante = str(input('Digite uma letra: ')).lower()
if identificador_de_consoante[0] in 'aeiou':
    print('É VOGAL')
elif identificador_de_consoante[0].isnumeric():
    float(identificador_de_consoante)
    print('DIGITE UMA LETRA')
else:
    print('É CONSOANTE')
