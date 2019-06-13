import sqlite3
#--------------------------------------------------------------------------------------------
                                        #FUNÇÕES INPUT
def pedir_nome():                           
    return(input('Digite o nome(apenas letras):'))
    
def pedir_CPF():                            
    return(input('Digite o CPF(apenas dígitos):'))

def pedir_departamento():                   
    return(input('Digite o departamento:'))

def pedir_codigo():
    return(input('Digite o código da disciplina:'))

def pedir_codturma():
    return(input('Digite o código da turma:'))

def pedir_periodo():
    return(input('Digite o período(dígito):'))

def pedir_CPF_professor():
    return(input('Digite o CPF do Professor(apenas dígitos):'))

def pedir_CPF_aluno():
    return (input('Digite o CPF do Aluno(apenas dígitos):'))
#-----------------------------------------------------------------------------------------
                                    #CLASSE ALUNO
class Aluno:
    def __init__(self):
        self.nome = ''
        self.CPF = ''
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def add_aluno(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        self.nome = pedir_nome()
        self.cpf = pedir_CPF()
        try:
            cursor.execute('''
                INSERT INTO alunos(nome, cpf)
                    VALUES (?, ?)
                    ''',(self.nome, self.cpf))
        except Exception as erro:
            print('---- CPF já utilizado ----')
            cursor.close()
            conexao.close()
            return erro
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def att_aluno(self, novo_nome, novo_cpf):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        try:
            cursor.execute('''
                    UPDATE alunos set cpf = '{}', nome = '{}' where cpf = '{}'
            '''.format(novo_cpf, novo_nome, self.cpf))
        except Exception as erro:
            print('---- CPF já utilizado ----')
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()
    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        self.cpf = pedir_CPF()
        try:
            cursor.execute("""
                    DELETE FROM alunos WHERE cpf = ?
            """, (self.cpf,))
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()

    def consultar(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM alunos')
        print('================================')
        print('     ALUNOS REGISTRADOS')
        print('--------------------------------')
        for linha in cursor.fetchall():
            print('ID: {} NOME:{}  CPF:{}'.format(linha[0], linha[1], linha[2]))
        print('================================')
        cursor.close()
        conexao.commit()
        conexao.close()
#-------------------------------------------------------------------------------
                                #CLASSE PROFESSOR
class Professor:
    def __init__(self):
        self.nome = ''
        self.CPF = ''
        self.departamento = ''
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_departamento(self):
        return self.departamento
    def set_departamento(self, novo_departamento):
        self.departamento = novo_departamento

    def add_professor(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        self.nome = pedir_nome()
        self.cpf = pedir_CPF()
        self.departamento = pedir_departamento()
        try:
            cursor.execute('''
                INSERT INTO professores(nome, cpf, departamento)
                    VALUES (?, ?, ?)
                    ''',(self.nome, self.cpf, self.departamento))
        except Exception as erro:
            print('---- CPF já utilizado ----')
            cursor.close()
            conexao.close()
            return erro
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def att_professor(self, novo_nome, novo_cpf, novo_departamento):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        try:
            cursor.execute('''
                    UPDATE professores set cpf = '{}', nome = '{}', departamento = '{}' where cpf = '{}'
            '''.format(novo_cpf, novo_nome, novo_departamento, self.cpf))
        except Exception as erro:
            print('---- CPF já utilizado ----')
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()
    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        self.cpf = pedir_CPF()
        try:
            cursor.execute("""
                    DELETE FROM professores WHERE cpf = ?
            """, (self.cpf,))
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()

    def consultar(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM professores')
        print('==================================================')
        print('            PROFESSORES REGISTRADOS')
        print('--------------------------------------------------')
        for linha in cursor.fetchall():
            print('ID: {} NOME:{}  CPF:{} DEPARTAMENTO: {}'.format(linha[0], linha[1], linha[2], linha[3]))
        print('==================================================')
        cursor.close()
        conexao.commit()
        conexao.close()

#-------------------------------------------------------------------------------
                                #CLASSE DISCIPLINA
class Disciplina:
    def __init__(self):
        self.nome = ''
        self.codigo = ''
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_codigo(self):
        return self.codigo
    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo

    def add_disciplina(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        self.codigo = pedir_codigo()
        self.nome = pedir_nome()
        try:
            cursor.execute('''
                INSERT INTO disciplinas(nome, codigo)
                    VALUES (?, ?)
                    ''',(self.nome, self.codigo))
        except Exception as erro:
            print('---- Código de Disciplina já utilizado ----')
            cursor.close()
            conexao.close()
            return erro
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def att_disciplina(self, novo_nome, novo_codigo):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        try:
            cursor.execute('''
                    UPDATE disciplinas set nome = '{}', codigo = '{}' where codigo = '{}'
            '''.format(novo_nome, novo_codigo, self.codigo))
        except Exception as erro:
            print('---- Código de Disciplina já utilizado ----')
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()
    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        self.codigo = pedir_codigo()
        try:
            cursor.execute("""
                    DELETE FROM disciplinas WHERE codigo = ?
            """, (self.codigo,))
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()

    def consultar(self):
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM disciplinas')
        print('======================================')
        print('       DISCIPLINAS REGISTRADAS')
        print('--------------------------------------')
        for linha in cursor.fetchall():
            print('ID: {} NOME:{}  CÓDIGO:{} '.format(linha[0], linha[1], linha[2]))
        print('======================================')
        cursor.close()
        conexao.commit()
        conexao.close()
