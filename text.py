import cx_Oracle
conn_str='inv/inventiva$ngo@192.168.15.2:1521/bdngo'
db_conn = cx_Oracle.connect(conn_str)
cursor = db_conn.cursor()
cursor.execute('SELECT * FROM st_rubros')
registros = cursor.fetchall()
for r in registros:
  print (r)