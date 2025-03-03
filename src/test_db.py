from repository.db_mysql import get_connection

conn = get_connection()
if conn:
    print("Conexión exitosa a MySQL")
    conn.close()
else:
    print("No se pudo conectar a MySQL")
