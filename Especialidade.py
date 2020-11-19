print ("Cadastro de Especialidade")

def cadastro_especialidade():       
    dados = dict()
    dados ['nome'] = input('Nome')
    dados ['descrição'] = input('Descrição')
    dados ['ID'] = input('ID')
    dados ['categoria'] = input('Caregoria')
    dados ['consultor'] = input('Consultor')
    print(dados) 
cadastro_especialidade()    