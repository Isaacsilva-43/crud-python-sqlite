import sqlite3

conexao = sqlite3.connect("projeto1.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS jogos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco FLOAT NOT NULL)''')


def cadastrar():
    nome = input("Nome do jogo: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))

    cursor.execute('INSERT INTO jogos (nome, categoria, preco) VALUES(?, ?, ?)',
    (nome, categoria, preco))
    conexao.commit()
    print('jogo cadastrado com sucesso')


def listar():
    cursor.execute('SELECT * FROM jogos')
    jogos = cursor.fetchall()
    for jogo in jogos:
        id_jogo,nome,categoria,preco = jogo
        print(f'id = {id_jogo}\n'
                f'nome = {nome}\n'
                f'categoria = {categoria}\n'
                f'preço = {preco}')
        print()


def atualizar():
    alt = int(input('digite o id do jogo que deseja atualizar: '))
    nome = input("Nome do jogo: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))

    cursor.execute('''UPDATE jogos
    SET nome = ?, categoria = ?, preco = ?
    WHERE id = ?''',
    (nome,categoria, preco, alt ))
    conexao.commit()
    print("Jogo atualizado com sucesso!")

def excluir():
    jg = int(input('Digite o id do jogo que deseja excluir: '))
    cursor.execute('DELETE FROM jogos WHERE id = ?',
    (jg,))
    conexao.commit()
    print('jogo excluido com sucesso')

def menu():


    while True:
        print()
        cla = int(input('1 - cadastrar jogo\n'
                  '2 - Listar jogos\n'
                  '3 - atualizar jogo\n'
                  '4 - excluir jogo\n'
                  '5 - sair\n'
                        'R:'))
        print()
        if cla == 1:
            cadastrar()
        
        elif cla == 2:
            listar()

        elif cla == 3:
            atualizar()

        elif cla == 4:
            excluir()

        elif cla == 5:
            break

        else:
            print('Opção invalida')


menu()
conexao.close()