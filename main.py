import requests
from bs4 import BeautifulSoup

# Hacer una solicitud a la página web
url = "https://www.example.com"
page = requests.get(url)

# Verificar si la solicitud fue exitosa
if page.status_code == 200:
    # Crear un objeto BeautifulSoup a partir del contenido de la página
    soup = BeautifulSoup(page.content, "html.parser")
    # Buscar y extraer información de la página
    title = soup.find("title").text
    # Imprimir la información extraída
    print("Title:", title)
else:
    print("No se pudo acceder a la página")
