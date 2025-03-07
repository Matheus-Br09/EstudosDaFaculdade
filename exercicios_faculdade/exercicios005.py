nota_do_aluno = float(input('Digite sua nota: '))
if nota_do_aluno < 0 or nota_do_aluno > 10:
    print('VALOR INVÁLIDO')
else:
    if nota_do_aluno == 10:
        print('APROVADO COM DISTINÇÃO')
    elif nota_do_aluno < 7:
        print('Situação: REPROVADO')
    elif nota_do_aluno >= 7:
        print('Situação: APROVADO')