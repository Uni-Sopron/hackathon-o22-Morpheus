import requests
from bs4 import BeautifulSoup
import random
import shutil
from urlextract import URLExtract
import os
from game import get_5_szo, readszavak
# kell pip installálni: bs4, requests, shutil, urlextract, lxml

my_path = os.path.abspath(os.path.dirname(__file__))

def give_url(words: list) -> list:
    images = []
    for i in range(len(words)):
        r = requests.get('https://www.google.com/search?tbm=isch&q='+words[i])
        soup = BeautifulSoup(r.text, 'lxml')

        first_image_link = soup.find('img', class_='yWs4tf')['src']
        images.append(first_image_link)
    return images

def download_image(urls: list, szavak: list):
    # Set up the image URL and filename
    for i in range(len(urls)):
        image_url = urls[i]
        filename = szavak[i]+".jpg"

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream=True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')

def move_jpgs_to_folder():
    if not os.path.isdir(my_path+"/images/"):
        os.mkdir(my_path+"/images/")

    for i in os.listdir():
        if i.split(".")[-1] == "jpg":
            os.replace(i, my_path+"/images/"+i)

def main():
    #szavak = get_5_szo()
    szavak = readszavak()
    urls = give_url(szavak)
    download_image(urls, szavak)
    move_jpgs_to_folder()

main()
