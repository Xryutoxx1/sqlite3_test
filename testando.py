import sqlite3


def mostrar_tudo():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)


    conn.commit()
    conn.close()


def adicionar1(primeiro,ultimo,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES(?,?,?)", (primeiro, ultimo, email))
    conn.commit()
    conn.close()


def adicionar_varios(lista):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES(?,?,?)", (lista))
    conn.commit()
    conn.close()



def deletar(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", (id) )
    print(" usuário deletado com sucesso! ")
    conn.commit()
    conn.close()