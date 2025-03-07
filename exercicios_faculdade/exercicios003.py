ident_sexo = str(input('Digite o sexo [F/M]: ')).lower()
if ident_sexo == 'f' or ident_sexo == 'feminino':
    print(f'Sexo: FEMININO')
if ident_sexo == 'm' or ident_sexo == 'masculino':
    print(f'Sexo: MASCULINO')
else:
    print('\033[31mSEXO INVÁLIDO\033[m')
