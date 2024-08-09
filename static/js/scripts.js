document.addEventListener("DOMContentLoaded", function() {
    fetch("/get_peliculas")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const ul = document.querySelector("ul");
        ul.innerHTML = "";

        data.peliculas.forEach(pelicula => {
            const li = document.createElement("li");

            if (pelicula.img_url) {
                const img = document.createElement("img");
                img.src = pelicula.img_url;
                img.alt = `Poster de ${pelicula.titulo}`;
                li.appendChild(img);
            }

            const texto = `${pelicula.titulo} (${pelicula.pais}) - ${pelicula.director}`;
            li.appendChild(document.createTextNode(texto));

            ul.appendChild(li);
        });
    })
    .catch(error => console.error("Error fetching data:", error));
});

