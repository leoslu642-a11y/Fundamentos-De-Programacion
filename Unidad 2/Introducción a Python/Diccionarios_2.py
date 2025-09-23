import json

#Colocar un ISBN de los libros
biblioteca = {
    "978-84-376-0494-7": { 
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    "978-607-8946-54-9": {
        "título": "Un faro bjo la lluvia",
        "autor": ["Díaz Amador", "Marco Antonio"],
        "géneros": ["Filosofía ética y moral"]
    },
    "978-968-9723-10-3": {
        "título": "100 días sin ti diario de un duelo",
        "autor": ["G. de la Cueva", "Liliana"],
        "géneros": ["Autoayuda"]
    },
    "9978-607-29-7501-9": {
        "título": "El crujido del tiempo",
        "autor": ["Ortega Amezcua", "César"],
        "géneros": ["Ensayo filosófico", "Reflexión humanista"]
    }

}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)