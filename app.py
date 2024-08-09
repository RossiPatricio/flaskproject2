from flask import Flask, render_template, jsonify
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
    return render_template('index.html')

@app.route('/get_peliculas')
def get_peliculas():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM peliculas;')
    peliculas = cur.fetchall()
    cur.close()
    conn.close()

    # Formatear los datos en una lista de diccionarios
    peliculas_dict = []
    for pelicula in peliculas:
        peliculas_dict.append({
            'titulo': pelicula['titulo'],
            'pais': pelicula['pais'],
            'director': pelicula['director'],
            'img_url': pelicula['img_url']
        })

    return jsonify({"peliculas": peliculas_dict})

if __name__ == '__main__':
    app.run(debug=True)

