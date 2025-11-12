import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="pwd123",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Connection error:", e)
        return None

def create_users_table():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            create_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                name VARCHAR(50),
                email VARCHAR(100)
            );
            """
            cursor.execute(create_query)
            conn.commit()
            print("Users table created successfully.")
        except Exception as e:
            print("Error creating table:", e)
        finally:
            cursor.close()
            conn.close()

def create_user(user_id, name, email):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, name, email))
            conn.commit()
            print("User inserted successfully.")
        except Exception as e:
            print("Insert error:", e)
        finally:
            cursor.close()
            conn.close()

def get_users():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Read error:", e)
            return []
        finally:
            cursor.close()
            conn.close()    

if __name__ == "__main__":

    create_users_table()
    
    create_user(1, "Greeshma", "greeshmak@gmail.com")
    create_user(2, "Pranav", "pranavk@gmail.com")

    print("All users:", get_users())