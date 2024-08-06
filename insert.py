import psycopg2

# Datos de conexión a la base de datos
conn = psycopg2.connect(
     database="peliculas_db",
    user="postgres",
    password="010001101000",
    host="localhost",
    port="5432"
)

# Función para insertar una película en la base de datos con todos los datos
def insertar_pelicula(conn, titulo, director, ano, genero, duracion):
    with conn.cursor() as cur:
        cur.execute(
             "INSERT INTO peliculas (titulo, director, ano, genero, duracion) VALUES (%s, %s, %s, %s, %s)",
            (titulo, director, ano, genero, duracion)
         )
        conn.commit()

# Leer las películas desde el archivo .txt
with open('peliculas.txt', 'r') as archivo:
     for linea in archivo:
        datos = linea.strip().split(',')
        titulo = datos[0].strip()
        director = datos[1].strip()
        ano = int(datos[2].strip())
        genero = datos[3].strip()
        duracion = int(datos[4].strip())
        insertar_pelicula(conn, titulo, director, ano, genero, duracion)

# Cerrar la conexión a la base de datos
conn.close()