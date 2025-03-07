turno_escolar = str(input('Turno: [M/V/N] ')).lower()
if turno_escolar == 'm' or turno_escolar == 'matutino' or turno_escolar == 'manha':
    print(f'Bom Dia !!!')
elif turno_escolar == 'v' or turno_escolar == 'vespertino' or turno_escolar == 'tarde':
    print(f'Boa Tarde !!!')
elif turno_escolar == 'n' or turno_escolar == 'noturno' or turno_escolar == 'noite':
    print('Boa Noite !!!')
else:
    print('Valor inválido!')