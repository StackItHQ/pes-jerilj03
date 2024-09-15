import mysql.connector

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        # host='Jeril_J',
        user='root',
        password='1915',
        database='my_db'
    )
    return connection

# Read data from MySQL
def read_db_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test_table")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Update data in MySQL
def update_db_data(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM test_table")  # Reset the table
    insert_query = "INSERT INTO test_table (col1, col2, col3, col4) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_query, data)
    connection.commit()
    cursor.close()
    connection.close()



# def update_db_data(data):
#     connection = get_db_connection()
#     cursor = connection.cursor()
    
#     # Example: Assuming 'id' is a unique identifier in your data
#     upsert_query = """
#     INSERT INTO test_table (id, col1, col2, col3, col4) 
#     VALUES (%s, %s, %s, %s, %s)
#     ON DUPLICATE KEY UPDATE
#     col1 = VALUES(col1),
#     col2 = VALUES(col2),
#     col3 = VALUES(col3),
#     col4 = VALUES(col4)
#     """
    
#     cursor.executemany(upsert_query, data)
#     connection.commit()
#     cursor.close()
#     connection.close()

