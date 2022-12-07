import json
import os
os.system("cls")

my_path = os.path.abspath(os.path.dirname(__file__))

angol = []
file1 = open(my_path+'/words.txt', 'r', encoding='utf-8')
Lines = file1.readlines()
for line in Lines:
    angol.append(line.strip())
file1.close()

magyar = []
file2 = open(my_path+'/szavak.txt', 'r', encoding='utf-8')
Lines = file2.readlines()
for line in Lines:
    magyar.append(line.strip())
file2.close()

en_hu = {}


for i in range(len(angol)):
    for j in range(len(magyar)):
        if i == j:
            en_hu[angol[i]] = magyar[j]

print(en_hu)

with open("szoparositas.json","w",encoding="UTF8") as f:
    json.dump(en_hu ,f, ensure_ascii=False)