import sqlite3
from classes import Aluno
from classes import Professor
from classes import Disciplina
#------------------------------------------------------------------------
                                      #FUNÇÕES MENU
def menu_principal():
    return print('''
----- MENU PRINCIPAL -----

1 - Dados de Professores
2 - Dados de Alunos
3 - Dados de Disciplinas
4 - Dados de Turmas
0 - Sair
''')

def menu_professor():           
    return print('''
----- MENU -----

* PROFESSORES *

1 - Adiciona
2 - Atualiza
3 - Consulta
4 - Deleta
0 - Menu Principal
''')
#------------------------
def menu_aluno():                           
    return print('''
----- MENU -----

* ALUNOS *

1 - Adiciona
2 - Atualiza
3 - Consulta
4 - Deleta
0 - Menu Principal
''')
#------------------------
def menu_disciplina():                           
    return print('''
----- MENU -----

* DISCIPLINAS *

1 - Adiciona
2 - Atualiza
3 - Consulta
4 - Deleta
0 - Menu Principal
''')
#-----------------------
def menu_turma():                           
    return print('''
----- MENU -----

* TURMAS *

1 - Adiciona
2 - Atualiza
3 - Consulta
4 - Deleta
0 - Menu Principal
''')
#----------------------------------------------------------------------------------
                            #OPERADOR PROFESSORES
while True:
    x = 0
    professor = Professor()
    menu_principal()
    operacao = int(input('Digite a operação que deseja fazer:'))
    if operacao == 1:
        menu_professor()
        while True:
            professor = Professor()
            op2 = input('Digite a operação para PROFESSORES:')
            if op2 == '1':
                print('---- Insira os dados a serem cadastrados ----')
                self.nome = pedir_nome()
                self.cpf = pedir_CPF()
                self.departamento = pedir_departamento()
                professor.add_professor()
            elif op2 == '2':
                print('---- Insira o CPF do professor a ser atualizado ----')
                set_cpf(input('Digite o CPF:'))
                set_nome = input('Digite o novo nome:')
                set_cpf = int(input('Digite o novo CPF:'))
                set_departamento = input('Digite o novo departamento:')
                professor.att_professor(novo_nome, novo_cpf, novo_departamento)

            elif op2 == '3':
                professor.consultar()
            elif op2 == '4':
                print('---- Digite o CPF do professor a ser deletado ----')
                professor.set_cpf(input('Digite o CPF:'))
                professor.apagar()
                print('---- Professor Deletado ----')
    
            elif op2 == '0':
                break
            else:
                print('---- Operação Inválida ----')
#----------------------------------------------------------------------------------
                            #OPERADOR ALUNOS               
    elif operacao == 2:
        menu_aluno()
        while True:
            aluno = Aluno()
            op3 = input('Digite a operação para ALUNOS:')
            if op3 == '1':
                print('---- Insira os dados a serem cadastrados ----')
                aluno.set_nome(input('Digite o nome:'))
                aluno.set_cpf(input('Digite o CPF:'))
                aluno.add_aluno()                
            elif op3 == '2':
                print('---- Insira o CPF do aluno a ser atualizado ----')
                aluno.set_cpf(input('Digite o CPF:'))
                novo_nome = input('Digite o novo nome:')
                novo_cpf = input('Digite o novo CPF:')
                aluno.att_aluno(novo_nome, novo_cpf)
               
            elif op3 == '3':
                aluno.consultar()
                
            elif op3 == '4':
                print('---- Insira o CPF do aluno a ser deletado ----')
                aluno.set_cpf(input('Digite o CPF:'))
                aluno.apagar()
                print('---- Aluno deletado ----')
                
            elif op3 == '0':
                break
            
            else:
                print('---- Operação Inválida ----')
#----------------------------------------------------------------------------------
                            #OPERADOR DISCIPLINAS              
    elif operacao == 3:
        menu_disciplina()
        while True:
            disciplina = Disciplina()
            op4 = input('Digite a operação para DISCIPLINA:')
            if op4 == '1':
                print('---- Insira os dados a serem cadastrados ----')
                disciplina.set_nome(input('Digite o nome:'))
                disciplina.set_codigo(input('Digite o código:'))
                disciplina.add_disciplina()
            elif op4 == '2':
                print('---- Insira o Código da disciplina a ser atualizada ----')
                disciplina.set_codigo(input('Digite o Código da Disciplina:'))
                novo_nome = input('Digite o novo nome:')
                novo_codigo = input('Digite o novo Código:')
                disciplina.att_disciplina(novo_nome, novo_codigo)
            elif op4 == '3':
                disciplina.consultar()
            elif op4 == '4':
                print('---- Insira o código da disciplina a ser deletada ----')
                disciplina.set_codigo(input('Digite o código da Disciplina:'))
                disciplina.apagar()
            elif op4 == '0':
                break
            else:
                print('---- Operação Inválida ----')
#----------------------------------------------------------------------------------
                            #OPERADOR TURMAS
    elif operacao == 4:
        menu_turma()
        while True:
            op5 = input('Digite a operação para TURMA:')
            if op5 == '1':
                print('---- Insira os dados a serem cadastrados ----')
            elif op5 == '2':
                print('---- Insira o Código da turma a ser atualizada ----')
            elif op5 == '3':
                print(' MANUTENCAO')
            elif op5 == '4':
                print('---- Insira o código da turma a ser deletada ----')
            elif op5 == '0':
                break
            else:
                print('---- Operação Inválida ----')
    elif operacao == 0:
        break
    
            
            
