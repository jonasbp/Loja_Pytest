import sqlite3
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