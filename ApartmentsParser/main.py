
from flask import Flask, jsonify
import psycopg2
from crawler import crawl
from web.html_translate import port_run

app = Flask(__name__)

# Define a function to create a connection to the PostgreSQL database
def create_db_connection():
    return psycopg2.connect(
        dbname="sreality_apartments_db",
        user="affan",
        password="2023",
        host="db_task",
        port=5432
    )

@app.route('/')
def get_apartments():
    connection = create_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM apartments500")
    rows = cursor.fetchall()

    apartments = []
    for row in rows:
        apartment = {
            "id": row[0],
            "name": row[1],
            "photo": row[3]
        }
        apartments.append(apartment)

    cursor.close()
    connection.close()

    return jsonify(apartments)

def main():
    apartments = crawl()
    
    # Create the 'apartments500' table if it doesn't exist
    connection = create_db_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS apartments500 (id serial PRIMARY KEY, name VARCHAR NOT NULL, photo VARCHAR NOT NULL);")
    connection.commit()
    cursor.close()
    connection.close()
    
    # Insert apartment data into the 'apartments500' table
    connection = create_db_connection()
    cursor = connection.cursor()
    for idx in range(len(apartments)):
        row = "INSERT INTO apartments500 (id, name, photo) " \
               "VALUES ('{id}', '{name}', '{img_url}');".format(id=idx+1, **apartments[idx])
        cursor.execute(row)

    connection.commit()
    cursor.close()
    connection.close()

    # Run the Flask web server
    port_run(apartments=apartments)

if __name__ == "__main__":
    main()