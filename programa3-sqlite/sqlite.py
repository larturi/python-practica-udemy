import sqlite3

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")

conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES(1, 'IMPRESORA', 300)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES(2, 'CUADERNO', 20)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES(3, 'SILLA', 1000)")
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()