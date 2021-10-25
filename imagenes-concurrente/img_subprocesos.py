from imgurpython import ImgurClient

import os
import urllib.request
import timeit
from concurrent.futures import ThreadPoolExecutor

secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"

cliente = ImgurClient(id_cliente, secreto_cliente)


def descarga_url_img(link):
    print(link)
    # Con esto ya podemos obtener el corte de la url imagen
    nombre_img = link.split("/")[3]
    formato_img = nombre_img.split(".")[1]
    nombre_img = nombre_img.split(".")[0]
    print(nombre_img, formato_img)
    url_local = "./Imagenes/{}.{}"
    # Guardar nne local las imagenes
    urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))


def main():
    id_album = "bUaCfoz"
    imagenes = [img.link for img in cliente.get_album_images(id_album)]
    numero_hilos = len(imagenes)

    with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
        executor.map(descarga_url_img, imagenes)


if __name__ == "__main__":
    print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))