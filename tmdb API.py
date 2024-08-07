import requests
import json

def obtener_poster_url(movie_id):
    api_key = "14dd84c8569641313e0340c876d913f0"  # Replace with your TMDb API Key
    base_url = "https://api.themoviedb.org/3/movie/"
    url = f"{base_url}{movie_id}?api_key={api_key}&language=en-US"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = json.loads(response.text)

        if 'poster_path' in data:
            image_base_url = "https://image.tmdb.org/t/p/w500"
            poster_url = f"{image_base_url}{data['poster_path']}"
            return poster_url
        else:
            return "No poster found for this movie."

    except requests.exceptions.RequestException as e:
        # Handle network errors, timeouts, etc.
        return f"Error retrieving movie data: {e}"

# Example usage
# movie_id = 550  # Try a different ID in case 540 is incorrect
# poster_url = obtener_poster_url(movie_id)
# print(poster_url)
