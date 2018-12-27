import pymysql.cursors

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'cwsok045',
    charset = 'utf8',
    db = 'my_suppliers',
    port = 3306,
)

try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO suppliers (Supplier_Name, Invoice_Number) VALUES (%s, %s)'
        cursor.execute(sql, ('dd', 'Andres'))
    conn.commit()
    print(cursor.lastrowid)
    # 1 (last insert id)
    # sql = 'SELECT * FROM suppliers WHERE Supplier_Name = %s'
    # cursor.execute(sql, ('Daniel',))
    # result = cursor.fetchone()
    # print(result)
except:
    print("Duplicate index")
finally:
    conn.close()

