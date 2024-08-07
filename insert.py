import psycopg2
import requests
import json

def obtener_poster_url(titulo):
    api_key = "14dd84c8569641313e0340c876d913f0"
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={titulo}"

    try:
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            poster_path = data['results'][0]['poster_path']
            image_base_url = "https://image.tmdb.org/t/p/w500"
            poster_url = f"{image_base_url}{poster_path}"
            return poster_url
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def insertar_pelicula(conn, titulo, director, ano, genero, duracion, img_url):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO peliculas (titulo, director, ano, genero, duracion, img_url) VALUES (%s, %s, %s, %s, %s, %s)",
            (titulo, director, ano, genero, duracion, img_url)
        )
        conn.commit()

conn = psycopg2.connect(
    database="peliculas_db",
    user="postgres",
    password="010001101000",
    host="localhost",
    port="5432"
)

with open('peliculas.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        titulo = datos[0].strip()
        director = datos[1].strip()
        ano = int(datos[2].strip())
        genero = datos[3].strip()
        duracion = int(datos[4].strip())
        img_url = obtener_poster_url(titulo)
        insertar_pelicula(conn, titulo, director, ano, genero, duracion, img_url)

conn.close()
