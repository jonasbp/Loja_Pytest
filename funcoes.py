from db.db_utils import cria_usuario,lista_usuario_especifico,lista_usuarios,altera_usuario,deleta_usuario
#VALIDAÇÕES
def valida_idade(idade):
    if (0 <= idade <= 120):
        return True
    else:
        return False
def valida_cpf(cpf):
    if (len(cpf) == 11):
        return True
    else:
        return False
def valida_email(email):
    if "@" in email:
        divide_email = email.split("@")
        nome = divide_email[0]
        dominio = divide_email[1]
        if (len(nome)>= 1 and len(dominio)>= 1):
            return True
        else:
            return False
    else:
        return False
def valida_preco(preco):
    if preco < 0:
        return False
    else:
        return True
def valida_estoque(estoque):
    if estoque < 0:
        return False
    else:
        return True
def valida_categoria(categoria):
    if categoria not in ["Limpeza",'Comida',"Hortifruti"]:
        return False
    else:
        return True

# USUÁRIO
# CADASTRO
def cadastra_usuario(Nome, Idade,Cpf,Endereco, Email):
    if (valida_idade(Idade) and valida_cpf(Cpf) and valida_email(Email)):
        usuario_banco = cria_usuario(Nome,Idade,Cpf,Endereco,Email)
        if usuario_banco == 200:
            return True
        else:
            return False
    else:
        return False
    
# print(cadastra_usuario("Jonas Pelegrina",22,"44444444444","Rua A","jonas@jonas.com.br"))
def usuario_especifico(id):
    return lista_usuario_especifico(id)
# print(usuario_especifico(6))
def todos_usuarios():
    return lista_usuarios()
# print(todos_usuarios())
def altera_dados_usuario(id,Nome,Idade,Cpf,Endereco,Email):
    if (valida_idade(Idade) and valida_cpf(Cpf) and valida_email(Email)):
        altera_banco = altera_usuario(id,Nome,Idade,Cpf,Endereco,Email)
        if altera_banco == 200:
            return "Alterado com sucesso!"
        else:
            return "Erro"
    else:
        return False
# print(altera_dados_usuario(6,"Jonas P",22,"44444444444","Rua AA","jonas@jonas.com"))
def deleta_usuario_sistema(id):
    deleta_banco = deleta_usuario(id)
    if deleta_banco == 200:\
        return "Deletado com sucesso"
    else:
        return "Não encontrado"
# print(deleta_usuario_sistema(6))