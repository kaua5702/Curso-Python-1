import random
import time

alunos = {
    'Kauã': 1 ,
    'Pedro': 2,
    'Andrei': 3,
    'José': 4
}

while True:
    print (f'Os alunos são: {alunos}')
    time.sleep(3)
    sorteio = random.choice(list(alunos.keys()) )
    print(f'O aluno escolhido para apagar o quadro foi: {sorteio}')
    time.sleep(3)
    break