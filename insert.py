import requests
import psycopg2

diccionario = {
    'titulo': '',
    'pais': '',
    'director': '',
    'img_url': '',
}

def obtener_informacion_por_titulo(titulo):
    api_key = "14dd84c8569641313e0340c876d913f0"
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={titulo}"
    
    try:
        search_response = requests.get(search_url)
        search_response.raise_for_status()
        search_data = search_response.json()

        if search_data['results']:
            movie_id = search_data['results'][0]['id']

            base_url = "https://api.themoviedb.org/3/movie/"
            movie_url = f"{base_url}{movie_id}?api_key={api_key}&language=en-US"
            movie_response = requests.get(movie_url)
            movie_response.raise_for_status()
            movie_data = movie_response.json()

            title = movie_data.get('title', 'N/A')
            countries = [country['name'] for country in movie_data.get('production_countries', [])]
            overview = movie_data.get('overview', 'No overview available.')
            poster_path = movie_data.get('poster_path', None)

            if poster_path:
                image_base_url = "https://image.tmdb.org/t/p/w500"
                poster_url = f"{image_base_url}{poster_path}"
            else:
                poster_url = None

            # Llenar el diccionario con los datos obtenidos
            diccionario['titulo'] = title
            diccionario["pais"] = countries
            diccionario["director"] = overview
            diccionario["img_url"] = poster_url

            return diccionario
        else:
            return None
        
    except requests.exceptions.RequestException as e:
        return None


def insertar_pelicula(conn, titulo, pais, director, img_url):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO peliculas (titulo, pais, director, img_url) VALUES (%s, %s, %s, %s)",
            (titulo, pais, director, img_url)
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
        linea = linea.strip()
        resultado = obtener_informacion_por_titulo(linea)
        
        if resultado:
            titulo = resultado['titulo']
            pais = ', '.join(resultado['pais'])  
            director = resultado['director']
            img_url = resultado['img_url']
            insertar_pelicula(conn, titulo, pais, director, img_url)

conn.close()
