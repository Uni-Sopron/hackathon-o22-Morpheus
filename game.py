from guess_checker import is_correct_guess
import random
import json
import os

my_path = os.path.abspath(os.path.dirname(__file__))

class Player:
    def __init__(self, name:str, playar_id: int) -> None:
        self.player_id = playar_id
        self.name = name
        self.role = None
        self.points = 0
    
    def setRole(self, role:str) -> None:
        """Beállít a játékosnak egy szerepet."""
        self.role = role

    def addPoint(self, point:int) -> None:
        """Hozzáaddja a pontokat a játékos pontjaihoz."""
        self.points += point

def playersInit() -> list:
    """Felveszi a játékosokat névvel.
    
    Returns:
        list: A játékosok listája.
    """
    playerList = []
    path = os.path.join(my_path, "roles.json")
    f = open(path)
    data = json.load(f)
    f.close()

    playerCount = 0
    maxPlayerCount = max([int(i) for i in data.keys()])
    minPlayerCount = min([int(i) for i in data.keys()])
    while int(playerCount) > maxPlayerCount or int(playerCount) < minPlayerCount: 
        print('Add meg a játékosok számát:')
        playerCount = input()
        if int(playerCount) > maxPlayerCount or int(playerCount) < minPlayerCount: 
            print("Nem jó játékos szám!")

    id = 0
    for playerNum in range(int(playerCount)):
        print("Add meg a " + str(playerNum+1) + ". nevét: ")
        name = input()
        playerList.append(Player(name,id))
        id += 1

    return playerList

def randomRoles(playerList:list) -> list:
    """Szerepet oszt minden játékoshoz.
    
    Returns:
        list: A játékosok listája szerepekkel.
    """
    path = os.path.join(my_path, "roles.json")
    f = open(path)
    data = json.load(f)
    f.close()

    withoutRole = playerList[:]

    dreamer = random.choice(playerList)
    for player in playerList:
        if player.player_id == dreamer.player_id:
            player.setRole("almodo")
            withoutRole.remove(dreamer)

    roles = []
    for role in data[str(len(playerList))].keys():
        for _ in range(int(data[str(len(playerList))][role])):
            roles.append(role)

    for player in withoutRole:
        role = random.choice(roles)
        player.setRole(role)
        roles.remove(role)

    for player in playerList:
        print("Név: " + player.name)
        print("Szerep: " + player.role)
        print()
        #os.system('clear') # linux
        os.system('cls') # windows

    return playerList

def readszavak():
    szavak = []
    path = os.path.join(my_path, 'szavak.txt')
    file1 = open(path, 'r',encoding='utf-8')
    Lines = file1.readlines()
    for line in Lines:
        szavak.append(line.strip())
    return szavak

def get_5_szo():
    selected_choices=[]
    szavak = readszavak()
    for _ in range(5):
        choice = random.choice(szavak)
        szavak.remove(choice)
        selected_choices.append(choice)
    return selected_choices

def round() -> None:
    """Egy kört vezényel le"""
    szavak = get_5_szo()
    almodoTippek = []
    joTippek = []
    rosszTippek = []

    for szo in szavak:
        print("szó: " + szo)
        tipp = input("tipp: ")
        almodoTippek.append(tipp)
        #os.system('clear') # linux
        os.system('cls') # windows

    for i in range(len(almodoTippek)):
        if is_correct_guess(almodoTippek[i], szavak[i]): joTippek.append(almodoTippek[i])
        else: rosszTippek.append(almodoTippek[i])
        
    print("eredeti szavak:")
    print(szavak)
    print("álmodó tippek:")
    print(almodoTippek)
    print("jó szavak:")
    print(joTippek)
    print("rossz szavak:")
    print(rosszTippek)

if __name__ == "__main__": 
    # print(is_correct_guess("csíRke", "csirke"))
    # print(is_correct_guess("kosar", "kosár")) FALSE???
    # print(is_correct_guess("muzsika", "zene")) FALSE???
    # print(is_correct_guess("regeny", "regény")) FALSE???
    playerList = playersInit()
    playerList = randomRoles(playerList)
    round()
