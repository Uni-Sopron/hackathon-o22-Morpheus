import requests
from bs4 import BeautifulSoup
import random
import shutil
from urlextract import URLExtract
import os
import json
# kell pip installálni: bs4, requests, shutil, urlextract, lxml

my_path = os.path.abspath(os.path.dirname(__file__))


def readszavak():
    szavak = []
    file1 = open(my_path+'/words.txt', 'r', encoding='utf-8')
    Lines = file1.readlines()
    for line in Lines:
        szavak.append(line.strip())
    return szavak


def get_5_szo():
    selected_choices = []
    szavak = readszavak()
    for _ in range(5):
        choice = random.choice(szavak)
        szavak.remove(choice)
        selected_choices.append(choice)
    print(selected_choices)
    return selected_choices


def give_url(words: list) -> list:
    images = []
    for i in range(len(words)):
        r = requests.get('https://www.google.com/search?tbm=isch&q='+words[i])
        soup = BeautifulSoup(r.text, 'lxml')

        first_image_link = soup.find('img', class_='yWs4tf')['src']
        images.append(first_image_link)
    return images


def en_to_hu(angol: str) -> str:
    with open("szoparositas.json","r",encoding="utf8") as f:
        szavak = json.load(f)
    return szavak[angol]

    
def download_image(urls: list, szavak: list):
    # Set up the image URL and filename
    for i in range(len(urls)):
        image_url = urls[i]
        filename = en_to_hu(szavak[i])+".jpg"

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
    if not os.path.isdir(my_path+"/kepek/"):
        os.mkdir(my_path+"/kepek/")

    for i in os.listdir():
        if i.split(".")[-1] == "jpg":
            os.replace(i, my_path+"/kepek/"+i)


def main():
    #szavak = get_5_szo()
    szavak = readszavak()
    urls = give_url(szavak)
    download_image(urls, szavak)
    move_jpgs_to_folder()


main()
