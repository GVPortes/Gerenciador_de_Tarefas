tarefas =['Abaixo seguem as tarefas',]
print ("Bem vindo ao Gerenciador De Tarefas em Python")
def adicionar_tarefa(tarefas):
    while True:
        tarefa = input('Digite a tarefa: ')
        tarefas.append(tarefa)
        print(f'Tarefa {tarefa} adicionada com sucesso!')
    
        continuar = input('Deseja adicionar mais tarefas? (s/n) ')
        if continuar == 'n':
            break

def remover_tarefa(tarefas):
    while True:
    #vamos ver se o usuário quer ou nao remover uma tarefa, se quiser, a gente mandar ele dizer qual, se nao a gente dá break.
        if not tarefas:
            print('Não há tarefas para remover!')
            break
        print('Tarefas disponíveis:')
        for i, tarefa_atual in enumerate(tarefas, start=1):
            print(f'{i} - {tarefa_atual }')
        tarefa = int(input('Digite o número da tarefa que deseja remover: '))
        tarefa.pop(tarefas - 1)
        print(f'Tarefa {tarefa} removida com sucesso!')
        continuar = input('Deseja remover mais tarefas? (s/n) ')
        if continuar == 'n':
            break

adicionar_tarefa(tarefas)
remover_tarefa(tarefas)
