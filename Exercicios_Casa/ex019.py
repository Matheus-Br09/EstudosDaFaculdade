import random


print('Vamos sortear um aluno para apagar o quadro...')
nome_aluno = str(input('Aluno 1: '))
nome_aluno2 = str(input('Aluno 2: '))
nome_aluno3 = str(input('Aluno 3: '))
nome_aluno4 = str(input('Aluno 4: '))
lista = [nome_aluno, nome_aluno2, nome_aluno3, nome_aluno4]

sorteio = random.choice(lista)
print(f'O aluno sorteado foi: {sorteio}')