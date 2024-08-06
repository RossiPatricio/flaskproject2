from flask import Flask, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="peliculas_db",
        user="postgres",
        password="010001101000",
        options='-c client_encoding=UTF8'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM peliculas;')
    peliculas = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', peliculas=peliculas)

if __name__ == '__main__':
    app.run(debug=True)