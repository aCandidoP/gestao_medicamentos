def escolha_plano():
    planos = ['Unimed', 'Policia Militar', 'Bradesco', 'NotreDame', 'SulAmérica']
    for i, plano in enumerate(planos, start=1):
        print(i, plano)
    escolha_index = input('Escolha um plano da lista (1-5) : ')
    return transforma_plano(escolha_index)

def transforma_plano(escolha):
    if escolha == '1':
        plano = 'Unimed'
    elif escolha == '2':
        plano = 'Polícia Militar'
    elif escolha == '3':
        plano = 'Bradesco'
    elif escolha == '4':
        plano = 'Notre Dame'
    elif escolha == '5':
        plano = 'SulAmérica'
    return plano
    



