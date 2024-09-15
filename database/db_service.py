import mysql.connector

# Establish the database connection
def get_db_connection():
    return mysql.connector.connect(
        user='root',
        password='1915',
        database='my_db'
    )

# Create new rows in the database
def create_db_rows(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO test_table (col1, col2, col3, col4)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    col2=VALUES(col2), col3=VALUES(col3), col4=VALUES(col4), last_modified=NOW()
    """
    
    try:
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Inserted or updated {cursor.rowcount} rows in the database.")
    except mysql.connector.Error as err:
        print(f"Error during insert/update: {err}")
    finally:
        cursor.close()
        connection.close()

# Read rows from the database
def read_db_rows(last_sync_time):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT col1, col2, col3, col4 FROM test_table WHERE last_modified > %s", (last_sync_time,))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

# Update rows in the database (handled in create_db_rows function)
# You can skip this if you use ON DUPLICATE KEY UPDATE in create_db_rows

# Delete rows from the database
def delete_db_rows(rows_to_delete):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    delete_query = "DELETE FROM test_table WHERE col1 = %s"
    
    try:
        cursor.executemany(delete_query, [(row[0],) for row in rows_to_delete])
        connection.commit()
        print(f"Deleted {cursor.rowcount} rows from the database.")
    except mysql.connector.Error as err:
        print(f"Error during deletion: {err}")
    finally:
        cursor.close()
        connection.close()
