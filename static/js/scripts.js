document.addEventListener("DOMContentLoaded", function() {
    fetch("/get_peliculas")
    .then(response => response.json())
    .then(data => {
        const ul = document.querySelector("ul");
        ul.innerHTML = "";
        data.peliculas.forEach(pelicula => {
            const li = document.createElement("li");
            const img = document.createElement("img");
            img.src = pelicula.img_url;
            img.alt = `Poster de ${pelicula.titulo}`;
            li.appendChild(img);
            li.appendChild(document.createTextNode(`${pelicula.titulo} (${pelicula.ano}) - ${pelicula.director}`));
            ul.appendChild(li);
        });
    })
    .catch(error => console.error("Error fetching data:", error));
});
