from tkinter import *
from classes import *

aluno = Aluno()
professor = Professor()
disciplina = Disciplina()

#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #CLIQUES NO BOTÃO
def bt_click():
    menu_alunos()
def bt_click_professores():
    menu_professores()
def bt_click_disciplinas():
    menu_disciplinas()
def bt_click_turmas():
    menu_turmas()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #JANELA PRINCIPAL
def main_window():

    janela_principal = Tk()
    janela_principal.geometry('500x500+100+100')
    janela_principal['bg']='white'
    janela_principal.title('UFRPE - BSI')
    
    lb1 = Label(janela_principal, bg='red', text='==============================================================')
    lb1.place(x=0, y=0)
    lb7 = Label(janela_principal, bg='red',text='############ UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE ###############')
    lb7.place(x=0, y=20)
    lb4 = Label(janela_principal, bg='red', text='==============================================================')
    lb4.place(x=0, y=80)
    lb2 = Label(janela_principal, bg='red', text='=============== /// SISTEMA DE CONTROLE ACADÊMICO /// ==================')
    lb2.place(x=0, y=60)
    lb3 = Label(janela_principal, bg='red', text='==============================================================')
    lb3.place(x=0, y=40)
    lb5 = Label(janela_principal, bg='red',text='==============================================================')
    lb5.place(x=0, y=480)
    logo = Label(janela_principal, bg='red',text='UFRPE - BSI 2019.1')
    logo.place(x=380, y=480)

    ufrpe_logo = PhotoImage(file = 'ufrpe_logo.gif')
    ufrpe_logot = Label(janela_principal, image = ufrpe_logo, fg='white')

    ufrpe_logot.image = ufrpe_logo
    ufrpe_logot.place(x=315, y=130)
      
    bt1 = Button(janela_principal, width=20, text='ALUNOS', command = bt_click)
    bt1.place(x=85, y=190)
    bt2 = Button(janela_principal, width=20, text='PROFESSORES', command= bt_click_professores)
    bt2.place(x=85, y=230)
    bt3 = Button(janela_principal, width=20, text='DISCIPLINAS', command= bt_click_disciplinas)
    bt3.place(x=85, y=270)
    bt4 = Button(janela_principal, width=20, text='TURMAS', command= bt_click_turmas)
    bt4.place(x=85, y=310)
    bt5 = Button(janela_principal, width=40, text='SAIR', command= exit)
    bt5.place(x=10, y=400)

    janela_principal.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #JANELA ALUNOS
def menu_alunos():
    janela_alunos = Tk()
    janela_alunos.geometry('500x500+100+100')

    lb1 = Label(janela_alunos, bg='red',text='==============================================================')
    lb1.place(x=0, y=0)
    lb7 = Label(janela_alunos,bg='red', text='############ UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE ###############')
    lb7.place(x=0, y=20)
    lb4 = Label(janela_alunos,bg='red', text='==============================================================')
    lb4.place(x=0, y=80)
    lb2 = Label(janela_alunos,bg='red', text='========================= /// ALUNOS /// ===========================')
    lb2.place(x=0, y=60)
    lb3 = Label(janela_alunos,bg='red', text='==============================================================')
    lb3.place(x=0, y=40)
    lb5 = Label(janela_alunos,bg='red', text='==============================================================')
    lb5.place(x=0, y=480)
    logo = Label(janela_alunos, bg='red',text='UFRPE - BSI 2019.1')
    logo.place(x=380, y=480)

    bt1 = Button(janela_alunos, width=20, text='ADICIONAR', command= janela_add_aluno)
    bt1.place(x= 170, y=150)
    bt2 = Button(janela_alunos, width=20, text='ATUALIZAR', command= janela_att_aluno)
    bt2.place(x= 170, y=190)
    bt3 = Button(janela_alunos, width=20, text='LISTAR', command= janela_listar_alunos)
    bt3.place(x=170, y=230)
    bt4 = Button(janela_alunos, width=20, text='APAGAR', command= janela_apagar_aluno)
    bt4.place(x=170, y=270)
    bt5 = Button(janela_alunos, width=40, text='FECHAR', command= janela_alunos.destroy)
    bt5.place(x=100, y=400)

    janela_alunos.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #JANELA PROFESSORES
def menu_professores():
    janela_professores = Tk()
    janela_professores.geometry('500x500+100+100')

    lb1 = Label(janela_professores,bg='red', text='==============================================================')
    lb1.place(x=0, y=0)
    lb7 = Label(janela_professores,bg='red', text='############ UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE ###############')
    lb7.place(x=0, y=20)
    lb4 = Label(janela_professores,bg='red', text='==============================================================')
    lb4.place(x=0, y=80)
    lb2 = Label(janela_professores,bg='red', text='========================= /// PROFESSORES /// ===========================')
    lb2.place(x=0, y=60)
    lb3 = Label(janela_professores,bg='red', text='==============================================================')
    lb3.place(x=0, y=40)
    lb5 = Label(janela_professores,bg='red', text='==============================================================')
    lb5.place(x=0, y=480)
    logo = Label(janela_professores,bg='red', text='UFRPE - BSI 2019.1')
    logo.place(x=380, y=480)

    bt1 = Button(janela_professores, width=20, text='ADICIONAR', command= janela_add_professor)
    bt1.place(x= 170, y=150)
    bt2 = Button(janela_professores, width=20, text='ATUALIZAR', command= janela_att_professor)
    bt2.place(x= 170, y=190)
    bt3 = Button(janela_professores, width=20, text='LISTAR')
    bt3.place(x=170, y=230)
    bt4 = Button(janela_professores, width=20, text='APAGAR', command=janela_apagar_professor)
    bt4.place(x=170, y=270)
    bt5 = Button(janela_professores, width=40, text='FECHAR', command= janela_professores.destroy)
    bt5.place(x=100, y=400)

    janela_professores.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #JANELA DISCIPLINAS
def menu_disciplinas():
    janela_disciplinas = Tk()
    janela_disciplinas.geometry('500x500+100+100')

    lb1 = Label(janela_disciplinas,bg='red', text='==============================================================')
    lb1.place(x=0, y=0)
    lb7 = Label(janela_disciplinas,bg='red', text='############ UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE ###############')
    lb7.place(x=0, y=20)
    lb4 = Label(janela_disciplinas,bg='red', text='==============================================================')
    lb4.place(x=0, y=80)
    lb2 = Label(janela_disciplinas,bg='red', text='========================= /// DISCIPLINAS /// ===========================')
    lb2.place(x=0, y=60)
    lb3 = Label(janela_disciplinas,bg='red', text='==============================================================')
    lb3.place(x=0, y=40)
    lb5 = Label(janela_disciplinas,bg='red', text='==============================================================')
    lb5.place(x=0, y=480)
    logo = Label(janela_disciplinas,bg='red', text='UFRPE - BSI 2019.1')
    logo.place(x=380, y=480)

    bt1 = Button(janela_disciplinas, width=20, text='ADICIONAR', command= janela_add_disciplina)
    bt1.place(x= 170, y=150)
    bt2 = Button(janela_disciplinas, width=20, text='ATUALIZAR', command= janela_att_disciplina)
    bt2.place(x= 170, y=190)
    bt3 = Button(janela_disciplinas, width=20, text='LISTAR')
    bt3.place(x=170, y=230)
    bt4 = Button(janela_disciplinas, width=20, text='APAGAR', command = janela_apagar_disciplina)
    bt4.place(x=170, y=270)
    bt5 = Button(janela_disciplinas, width=40, text='FECHAR', command= janela_disciplinas.destroy)
    bt5.place(x=100, y=400)

    janela_disciplinas.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #JANELA TURMAS
def menu_turmas():
    janela_turmas = Tk()
    janela_turmas.geometry('500x500+100+100')

    lb1 = Label(janela_turmas, bg='red',text='==============================================================')
    lb1.place(x=0, y=0)
    lb7 = Label(janela_turmas,bg='red', text='############ UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE ###############')
    lb7.place(x=0, y=20)
    lb4 = Label(janela_turmas,bg='red', text='==============================================================')
    lb4.place(x=0, y=80)
    lb2 = Label(janela_turmas,bg='red', text='========================= /// TURMAS /// ===========================')
    lb2.place(x=0, y=60)
    lb3 = Label(janela_turmas,bg='red', text='==============================================================')
    lb3.place(x=0, y=40)
    lb5 = Label(janela_turmas, bg='red',text='==============================================================')
    lb5.place(x=0, y=480)
    logo = Label(janela_turmas, bg='red',text='UFRPE - BSI 2019.1')
    logo.place(x=380, y=480)

    bt1 = Button(janela_turmas, width=20, text='ADICIONAR')
    bt1.place(x= 170, y=150)
    bt2 = Button(janela_turmas, width=20, text='ATUALIZAR')
    bt2.place(x= 170, y=190)
    bt3 = Button(janela_turmas, width=20, text='LISTAR')
    bt3.place(x=170, y=230)
    bt4 = Button(janela_turmas, width=20, text='APAGAR')
    bt4.place(x=170, y=270)
    bt5 = Button(janela_turmas, width=40, text='FECHAR', command= janela_turmas.destroy)
    bt5.place(x=100, y=400)

    janela_turmas.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #FUNÇÕES NA JANELA ALUNO(ADICIONAR)
def janela_add_aluno():

    def bt_click_addaluno():

        nome = entrada_aluno.get()
        cpf = entrada_cpf.get()

        aluno.set_nome(nome)
        aluno.set_cpf(cpf)
        
        if not aluno.add_aluno():
            lb = Label(janela, text='ALUNO ADICIONADO')
            lb.place(x=140, y=200)
        else:
            lb1 = Label(janela, text='CPF JÁ CADASTRADO')
            lb1.place(x=140, y=200)


    janela = Tk()
    janela.geometry('400x250+50+50')
    
    lb5 = Label(janela, text='=================================================')
    lb5.place(x=0, y=0)
    lb4 = Label(janela, text='=============== /// ADICIONAR ALUNO /// ==================')
    lb4.place(x=0, y=20)
    lb2 = Label(janela, text='DIGITE O NOME:')
    lb2.place(x=20, y=90)
    lb3 = Label(janela, text='DIGITE O CPF:')
    lb3.place(x=30, y=150)
    lb6 = Label(janela, text='==================================================')
    lb6.place(x=0, y=230)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    bt1 = Button(janela, width=10, text='CONFIRMAR', command= bt_click_addaluno)
    bt1.place(x=280, y= 110)

    
    entrada_aluno = Entry(janela)
    entrada_aluno.place(x=115, y=90)
    entrada_cpf = Entry(janela)
    entrada_cpf.place(x=115, y=150)
        
    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #ATUALIZAR(ALUNOS)
def janela_att_aluno():

    def bt_click_attaluno():

        cpf = entrada_cpf.get()
        novo_nome = entrada_novo_nome.get()
        novo_cpf = entrada_novo_cpf.get()
        
        aluno.set_cpf(cpf)

        if not aluno.att_aluno(novo_nome, novo_cpf):
            lb = Label(janela, text='ALUNO ATUALIZADO')
            lb.place(x=170, y=210)
        else:
            lb2 = Label(janela, text='CPF JÁ CADASTRADO')
            lb2.place(x=170, y=210)

    janela = Tk()
    janela.geometry('400x250+50+50')

    lb8 = Label(janela, text='=================================================')
    lb8.place(x=0, y=0)
    lb9 = Label(janela, text='=============== /// ATUALIZAR ALUNO /// ==================')
    lb9.place(x=0, y=20)
    lb12 = Label(janela, text='==================================================')
    lb12.place(x=0, y=230)
    lb5 = Label(janela, text='DIGITE O NOVO NOME:')
    lb5.place(x=20, y=140)
    lb6 = Label(janela, text='DIGITE O NOVO CPF:')
    lb6.place(x=20, y=190)
    lb4 = Label(janela, text='DIGITE O CPF:')
    lb4.place(x=20, y=90)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    entrada_cpf = Entry(janela)
    entrada_cpf.place(x=100, y=90)
    entrada_novo_nome = Entry(janela)
    entrada_novo_nome.place(x=150, y=140)
    entrada_novo_cpf = Entry(janela)
    entrada_novo_cpf.place(x=135, y=190)
    

    bt = Button(janela, width=10, text='CONFIRMAR', command= bt_click_attaluno)
    bt.place(x=300, y=130)

    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #APAGAR(ALUNOS)
def janela_apagar_aluno():

    def bt_click_delaluno():

        cpf = entrada_cpf.get()
        aluno.set_cpf(cpf)

        if not aluno.apagar():
            lb = Label(janela, text='ALUNO APAGADO')
            lb.place(x=140, y=200)
        else:
            lb1 = Label(janela, text='ALUNO NÃO ENCONTRADO')
            lb1.place(x=140, y=200)

    janela = Tk()
    janela.geometry('400x250+50+50')

    lb8 = Label(janela, text='=================================================')
    lb8.place(x=0, y=0)
    lb9 = Label(janela, text='=============== /// APAGAR ALUNO /// ==================')
    lb9.place(x=0, y=20)
    lb12 = Label(janela, text='==================================================')
    lb12.place(x=0, y=230)
    lb5 = Label(janela, text='DIGITE O CPF:')
    lb5.place(x=20, y=120)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    entrada_cpf = Entry(janela)
    entrada_cpf.place(x=100, y=120)

    bt = Button(janela, width=10, text='CONFIRMAR', command= bt_click_delaluno)
    bt.place(x=270, y=115)

    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #LISTAR(ALUNOS)
def janela_listar_alunos():

    janela = Tk()
    janela.geometry('800x500+100+100')   
    
    lb = Label(janela, text='=====================================================================================================')
    lb.place(x=0, y=0)
    lb1 = Label(janela, text='======================================== /// ALUNOS REGISTRADOS /// ========================================')
    lb1.place(x=0, y=20)
    lb2 = Label(janela, text='=====================================================================================================')
    lb2.place(x=0, y=480)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=680, y=480)

    registro = aluno.consultar()
    listbox = Listbox(janela, width=120, height=25)
    listbox.insert(0,registro)
    listbox.place(x=28, y=50)
    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                            #FUNÇÕES NA JANELA PROFESSOR(ADICIONAR)
def janela_add_professor():
    
    def bt_click_addprofessor():

        nome = entrada_professor.get()
        cpf = entrada_cpf.get()
        departamento = entrada_departamento.get()

        professor.set_nome(nome)
        professor.set_cpf(cpf)
        professor.set_departamento(departamento)
        
        if not professor.add_professor():
            lb = Label(janela, text='PROFESSOR ADICIONADO')
            lb.place(x=170, y=215)
        else:
            lb1 = Label(janela, text='CPF JÁ CADASTRADO')
            lb1.place(x=175, y=215)


    janela = Tk()
    janela.geometry('400x250+50+50')
    
    lb5 = Label(janela, text='=================================================')
    lb5.place(x=0, y=0)
    lb4 = Label(janela, text='=============== /// ADICIONAR PROFESSOR /// ==================')
    lb4.place(x=0, y=20)
    lb2 = Label(janela, text='DIGITE O NOME:')
    lb2.place(x=20, y=90)
    lb3 = Label(janela, text='DIGITE O CPF:')
    lb3.place(x=20, y=140)
    lb7 = Label(janela, text='DIGITE O DEPARTAMENTO:')
    lb7.place(x=20, y=190)
    lb6 = Label(janela, text='==================================================')
    lb6.place(x=0, y=230)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    bt1 = Button(janela, width=10, text='CONFIRMAR', command= bt_click_addprofessor)
    bt1.place(x=280, y= 110)

    
    entrada_professor = Entry(janela)
    entrada_professor.place(x=115, y=90)
    entrada_cpf = Entry(janela)
    entrada_cpf.place(x=100, y=140)
    entrada_departamento = Entry(janela)
    entrada_departamento.place(x=170, y=190)
    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #ATUALIZAR PROFESSOR

def janela_att_professor():
    
    def bt_click_attprofessor():

        cpf = entrada_cpf.get()
        novo_nome = entrada_novo_nome.get()
        novo_cpf = entrada_novo_cpf.get()
        novo_departamento = entrada_novo_departamento.get()
        
        professor.set_cpf(cpf)

        if not professor.att_professor(novo_nome, novo_cpf, novo_departamento):                          
            lb = Label(janela, text='PROFESSOR ATUALIZADO')
            lb.place(x=140, y=200)                         
        else:                          
            lb2 = Label(janela, text='CPF JÁ CADASTRADO')
            lb2.place(x=140, y=200)

    janela = Tk()
    janela.geometry('400x250+50+50')

    lb8 = Label(janela, text='=================================================')
    lb8.place(x=0, y=0)
    lb9 = Label(janela, text='=============== /// ATUALIZAR PROFESSOR /// ==================')
    lb9.place(x=0, y=20)
    lb12 = Label(janela, text='==================================================')
    lb12.place(x=0, y=230)
    
    lb6 = Label(janela, text='DIGITE O NOVO CPF:')
    lb6.place(x=20, y=140)
    lb5 = Label(janela, text='DIGITE O NOVO NOME:')
    lb5.place(x=20, y=105)
    lb4 = Label(janela, text='DIGITE O CPF:')
    lb4.place(x=20, y=70)
    lb = Label(janela, text='DIGITE O NOVO DEPARTAMENTO:')
    lb.place(x=20, y=170)
    
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    entrada_cpf = Entry(janela)
    entrada_cpf.place(x=100, y=70)
    entrada_novo_nome = Entry(janela)
    entrada_novo_nome.place(x=150, y=105)
    entrada_novo_cpf = Entry(janela)
    entrada_novo_cpf.place(x=135, y=140)
    entrada_novo_departamento = Entry(janela)
    entrada_novo_departamento.place(x=210, y= 170)
    

    bt = Button(janela, width=10, text='CONFIRMAR', command= bt_click_attprofessor)
    bt.place(x=300, y=110)

    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #APAGAR(PROFESSORES)
def janela_apagar_professor():

    def bt_click_delprofessor():

        cpf = entrada_cpf.get()
        professor.set_cpf(cpf)

        if not professor.apagar():
            lb = Label(janela, text='PROFESSOR APAGADO')
            lb.place(x=140, y=200)
        else:
            lb1 = Label(janela, text='PROFESSOR NÃO ENCONTRADO')
            lb1.place(x=140, y=200)

    janela = Tk()
    janela.geometry('400x250+50+50')

    lb8 = Label(janela, text='=================================================')
    lb8.place(x=0, y=0)
    lb9 = Label(janela, text='=============== /// APAGAR PROFESSOR /// ==================')
    lb9.place(x=0, y=20)
    lb12 = Label(janela, text='==================================================')
    lb12.place(x=0, y=230)
    lb5 = Label(janela, text='DIGITE O CPF:')
    lb5.place(x=20, y=120)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    entrada_cpf = Entry(janela)
    entrada_cpf.place(x=100, y=120)

    bt = Button(janela, width=10, text='CONFIRMAR', command= bt_click_delprofessor)
    bt.place(x=270, y=115)

    janela.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------
                                                        #FUNÇÕES NA JANELA DISCIPLINA(ADICIONAR)
def janela_add_disciplina():

    def bt_click_adddisciplina():

        nome = entrada_disciplina.get()
        codigo = entrada_codigo.get()

        disciplina.set_nome(nome)
        disciplina.set_codigo(codigo)
        
        if not disciplina.add_disciplina():
            lb = Label(janela, text='DISCIPLINA ADICIONADA')
            lb.place(x=140, y=200)
        else:
            lb1 = Label(janela, text='CÓDIGO DE DISCPLINA JÁ CADASTRADO')
            lb1.place(x=140, y=200)


    janela = Tk()
    janela.geometry('400x250+50+50')
    
    lb5 = Label(janela, text='=================================================')
    lb5.place(x=0, y=0)
    lb4 = Label(janela, text='=============== /// ADICIONAR DISCIPLINA /// ==================')
    lb4.place(x=0, y=20)
    lb2 = Label(janela, text='DIGITE O NOME:')
    lb2.place(x=20, y=90)
    lb3 = Label(janela, text='DIGITE O CÓDIGO:')
    lb3.place(x=20, y=150)
    lb6 = Label(janela, text='==================================================')
    lb6.place(x=0, y=230)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    bt1 = Button(janela, width=10, text='CONFIRMAR', command= bt_click_adddisciplina)
    bt1.place(x=280, y= 110)

    
    entrada_disciplina = Entry(janela)
    entrada_disciplina.place(x=115, y=90)
    entrada_codigo = Entry(janela)
    entrada_codigo.place(x=125, y=150)
        
    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #ATUALIZAR(DISCIPLINAS)
def janela_att_disciplina():

    def bt_click_attdisciplina():

        codigo = entrada_codigo.get()
        novo_nome = entrada_novo_nome.get()
        novo_codigo = entrada_novo_codigo.get()
        
        disciplina.set_codigo(codigo)

        if not disciplina.att_disciplina(novo_nome, novo_codigo):
            lb = Label(janela, text='DISCIPLINA ATUALIZADA')
            lb.place(x=210, y=215)
        else:
            lb2 = Label(janela, text='CÓDIGO DE DISCPLINA JÁ CADASTRADO')
            lb2.place(x=210, y=215)

    janela = Tk()
    janela.geometry('400x250+50+50')

    lb8 = Label(janela, text='=================================================')
    lb8.place(x=0, y=0)
    lb9 = Label(janela, text='=============== /// ATUALIZAR DISCIPLINA /// ==================')
    lb9.place(x=0, y=20)
    lb12 = Label(janela, text='==================================================')
    lb12.place(x=0, y=230)
    lb5 = Label(janela, text='DIGITE O NOVO NOME:')
    lb5.place(x=20, y=140)
    lb6 = Label(janela, text='DIGITE O NOVO CÓDIGO:')
    lb6.place(x=20, y=190)
    lb4 = Label(janela, text='DIGITE O CÓDIGO DA DISCIPLINA:')
    lb4.place(x=20, y=90)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    entrada_codigo = Entry(janela)
    entrada_codigo.place(x=210, y=90)
    entrada_novo_nome = Entry(janela)
    entrada_novo_nome.place(x=150, y=140)
    entrada_novo_codigo = Entry(janela)
    entrada_novo_codigo.place(x=160, y=190)
    

    bt = Button(janela, width=10, text='CONFIRMAR', command= bt_click_attdisciplina)
    bt.place(x=300, y=130)

    janela.mainloop()
#---------------------------------------------------------------------------------------------------------------
                                                    #APAGAR(DISCIPLINA)
def janela_apagar_disciplina():

    def bt_click_deldisciplina():

        codigo = entrada_codigo.get()
        disciplina.set_codigo(codigo)

        if not disciplina.apagar():
            lb = Label(janela, text='DISCIPLINA APAGADA')
            lb.place(x=140, y=200)
        else:
            lb1 = Label(janela, text='DISCIPLINA NÃO ENCONTRADA')
            lb1.place(x=140, y=200)

    janela = Tk()
    janela.geometry('400x250+50+50')

    lb8 = Label(janela, text='=================================================')
    lb8.place(x=0, y=0)
    lb9 = Label(janela, text='=============== /// APAGAR DISCIPLINA /// ==================')
    lb9.place(x=0, y=20)
    lb12 = Label(janela, text='==================================================')
    lb12.place(x=0, y=230)
    lb5 = Label(janela, text='DIGITE O CÓDIGO DA DISCIPLINA:')
    lb5.place(x=20, y=120)
    logo = Label(janela, text='UFRPE - BSI 2019.1')
    logo.place(x=280, y=230)

    entrada_codigo = Entry(janela)
    entrada_codigo.place(x=210, y=120)

    bt = Button(janela, width=10, text='CONFIRMAR', command= bt_click_deldisciplina)
    bt.place(x=270, y=170)

    janela.mainloop()
main_window()
