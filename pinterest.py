import requests
from bs4 import BeautifulSoup
import random
import shutil
from urlextract import URLExtract
import os
# kell pip installálni: bs4, requests, shutil, urlextract, lxml


def readszavak():
    szavak = []
    file1 = open('words.txt', 'r', encoding='utf-8')
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
        r = requests.get('https://gr.pinterest.com/search/pins/?q=' + words[i] + '&rs=typed')
        print(r)
        soup = BeautifulSoup(r.text, 'lxml')
        with open("asd.txt", "w",encoding="utf8") as f:
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
