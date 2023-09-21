import sqlite3

#USUÁRIO
def cria_usuario(Nome, Idade,Cpf,Endereco, Email):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM Usuarios WHERE Email = '{Email}';"
    cursor.execute(sql_query)
    consulta = cursor.fetchall()
    print(consulta)
    # conn.commit()
    if len(consulta) == 0:
        cursor.execute("""
        INSERT INTO Usuarios (Nome, Idade,CPF,Endereco, Email)
        VALUES (?, ?, ?, ?, ?);
        """, (Nome, Idade,Cpf,Endereco, Email))
        conn.commit()
        conn.close()
        return 200
    else:
        email_banco = consulta[0][2]
        if email_banco == Email:
            return 400

def lista_usuario_especifico(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM Usuarios WHERE ID = '{id}';"
    cursor.execute(sql_query)
    id = []
    for linha in cursor.fetchall():
        id.append(linha)
    conn.close()
    return id

def lista_usuarios():
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM Usuarios;
    """)
    usuarios = []
    for linha in cursor.fetchall():
        usuarios.append(linha)
    conn.close()
    return usuarios

def altera_usuario(id,Nome,Idade,Cpf,Endereco,Email):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Usuarios SET Nome = ?,Idade = ?,Cpf = ?,Endereco = ?,Email = ? WHERE ID = ?;",(Nome,Idade,Cpf,Endereco,Email,id))
    conn.commit()
    conn.close()
    return 200

def deleta_usuario(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"DELETE FROM Usuarios WHERE ID = {id};"
    cursor.execute(sql_query)
    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    if rows_affected == 0:
        return 404
    else:
        return 200

#PRODUTOS
def cria_produto(nome, descricao,categoria,preco,estoque):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM Produtos WHERE nome = '{nome}';"
    cursor.execute(sql_query)
    consulta = cursor.fetchall()
    print(consulta)
    # conn.commit()
    if len(consulta) == 0:
        cursor.execute("""
        INSERT INTO Produtos (nome, descricao,categoria,preco, estoque)
        VALUES (?, ?, ?, ?, ?);
        """, (nome, descricao,categoria,preco,estoque))
        conn.commit()
        conn.close()
        return 200
    else:
        email_banco = consulta[0][2]
        if email_banco == Email:
            return 400

def lista_produto_especifico(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM Produtos WHERE ID = '{id}';"
    cursor.execute(sql_query)
    id = []
    for linha in cursor.fetchall():
        id.append(linha)
    conn.close()
    return id

def lista_produtos():
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM Produtos;
    """)
    produtos = []
    for linha in cursor.fetchall():
        produtos.append(linha)
    conn.close()
    return produtos

def altera_produto(id,nome, descricao,categoria,preco,estoque):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Produtos SET nome = ?, descricao = ?,categoria = ?,preco = ?,estoque = ? WHERE ID = ?;",(nome, descricao,categoria,preco,estoque,id))
    conn.commit()
    conn.close()
    return 200

def deleta_produto(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"DELETE FROM Produtos WHERE ID = {id};"
    cursor.execute(sql_query)
    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    if rows_affected == 0:
        return 404
    else:
        return 200

#CLASSIFICAÇÕES
def cria_classificacao(id_usuario, id_produto,comentario):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Classificacoes (id_usuario, id_produto,comentario)
        VALUES (?, ?, ?);
        """, (id_usuario, id_produto,comentario))
    conn.commit()
    conn.close()
    return 200

def lista_classificacao_especifico(id_usuario,id_produto):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM Classificacoes WHERE id_usuario = '{id_usuario}' and id_produto = '{id_produto}';"
    cursor.execute(sql_query)
    id = []
    for linha in cursor.fetchall():
        id.append(linha)
    conn.close()
    return id

def lista_classificacoes():
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM Classificacoes;
    """)
    classificacoes = []
    for linha in cursor.fetchall():
        classificacoes.append(linha)
    conn.close()
    return classificacoes

def altera_classificacoes(id_usuario, id_produto,comentario):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Classificacoes SET id_usuario = ?, id_produto = ?,comentario = ? WHERE id_usuario = ?, id_produto = ?;",(id_usuario, id_produto,comentario))
    conn.commit()
    conn.close()
    return 200

def deleta_classificacao(id_usuario, id_produto):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()
    sql_query = f"DELETE FROM Classificacoes WHERE id_usuario = {id_usuario} and id_produto = {id_produto};"
    cursor.execute(sql_query)
    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    if rows_affected == 0:
        return 404
    else:
        return 200
