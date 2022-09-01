print('\nPROVA DE MATEMATICA REGRAS\n')
pertundas = {
    'Pergunta 1':{
    'Pergunta': '5*5?',
    'Resposta': {'a': '10', 'b': '25', 'c': '100', 'd':'90'},
    'Resposta_certa': 'b'},
    'Pergunta 2':{
    'Pergunta': '9*2?',
    'Resposta': {'a': '10', 'b': '15', 'c': '18', 'd':'90'},
    'Resposta_certa': 'c'},
    'Pergunta 3':{
    'Pergunta': '7*4?',
    'Resposta': {'a': '28', 'b': '15', 'c': '100', 'd':'90'},
    'Resposta_certa': 'a'},
    'Pergunta 4':{
    'Pergunta': '4*8?',
    'Resposta': {'a': '10', 'b': '15', 'c': '100', 'd':'32'},
    'Resposta_certa': 'd'},
    'Pergunta 5':{
    'Pergunta': '10*5?',
    'Resposta': {'a': '20', 'b': '15', 'c': '50', 'd':'90'},
    'Resposta_certa': 'c'},
}
acertos = []
num_certas = 0
num_erradas = 0

for pe, pr in pertundas.items():
    print(f'{pe}: {pr["Pergunta"]}')

    print('Resposta')
    for pk, pj in pr["Resposta"].items():
        print(f'[{pk}] {pj}')

    resposta_usuario = input('Escolha uma opção: ')

    if resposta_usuario == pr["Resposta_certa"]:
        print('Ebaaaa! Você acertou')
        acertos+=resposta_usuario
        num_certas=+1

    else:
        print('Ixiiiii! Você errou')
        num_erradas+=1

print('gabarito')
print('b, c, a, d, c')
print(f'Questão acertadas:')
for i in acertos:
    print(i)
print()
print(f'Questões acertadas: {num_certas}')
print(f'Questões erradas: {num_erradas}')