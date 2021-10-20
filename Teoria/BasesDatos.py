import sqlite3 as dbapi

'''
# dbapi es un identificador

print(dbapi.apilevel)  # Para ver la versión de la api

print(dbapi.threadsafety)  # Nos proporciona un enteiro do 0 ó 3 e nos indica a fiabilidad do uso dos fios

# Nos indica que o preprocesado e qmark ,é dicir, interrogantes -- select * from persona  where dni=? para que np 
# haya sql injectado 

print(dbapi.paramstyle)   

'''

# Para conectarnos :


try:

    bbdd = dbapi.connect("baseDatos.dat")
    cursor = bbdd.cursor()
    '''
    cursor.execute("""CREATE TABLE usuarios(dni text,
                                            nome text,
                                            direccion text)""")
    '''
    '''
    cursor.execute("""INSERT INTO  usuarios 
                        VALUES ('334455P','Patricia Maceiras', 'Candean') """)
 
    cursor.execute("""INSERT INTO  usuarios 
                            VALUES ('334455R','Raquel Maceiras', 'Candean') """)

    

    bbdd.commit()
    
   
    
    cursor.execute("""SELECT * FROM usuarios""")

    for rexistro in cursor.fetchall():
        print("Nombre : " + rexistro[1])
        print(" DNI : " + rexistro[0])
        print(" DIRECCIÓN : " + rexistro[2])
   
    SQL Injection
    dni = "334455P' or ''='"
    cursor.execute("""SELECT * FROM usuarios WHERE dni= '""" + dni+"'")
    for usuario in cursor.fetchall():
        print(usuario)
   '''
    dni = "334455P"
    cursor.execute("""SELECT * FROM usuarios WHERE dni=?""", (dni,))
    for usuario in cursor.fetchall():
        print(usuario)

except dbapi.DatabaseError as e:

    print("Erro ó conectarse a base de datos : " + str(e))
