import requests
from bs4 import BeautifulSoup
import os
from game import get_5_szo
# kell pip installálni: bs4, requests, shutil, urlextract, lxml

my_path = os.path.abspath(os.path.dirname(__file__))

def give_url(words: list) -> list:
    images = []
    #for i in range(len(words)):
    r = requests.get('https://www.google.com/search?tbm=isch&q=' + "cat")
    print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    path = os.path.join(my_path, "asd.txt")
    with open(path, "w",encoding="utf8") as f:
        f.write(f"{soup}")
        #first_image_link = soup.find('a', class_='image-list-link')['href']
        #images.append(first_image_link)
        #print(first_image_link)
    return images

def main():

    szavak = get_5_szo()
    # print(szavak)
    #szavak = ["mobile", "hammer"]
    urls = give_url(szavak)

    print(urls)

main()
