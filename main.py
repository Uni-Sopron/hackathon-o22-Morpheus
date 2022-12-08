from window import render
import pontozas
import random
import json
import os

my_path = os.path.abspath(os.path.dirname(__file__))

class Player:
    def __init__(self, name:str, player_id: int) -> None:
        self.player_id = player_id
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
    f = open(my_path + "/roles.json")
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

def randomRoles(playerList: list, dreamerList: list) -> list:
    """Szerepet oszt minden játékoshoz.
    
    Returns:
        list: A játékosok listája szerepekkel.
    """
    f = open(my_path + "/roles.json")
    data = json.load(f)
    f.close()

    withoutRole = playerList[:]

    dreamer = random.choice(playerList)
    while dreamerList.count(dreamer) != 0:
        dreamer = random.choice(playerList)
    for player in playerList:
        if player.player_id == dreamer.player_id:
            player.setRole("almodo")
            withoutRole.remove(dreamer)
            break

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
        input('')
        #os.system('clear') # linux
        os.system('cls') # windows

    return playerList

def getDreamer(playerList: list) -> int:
    for player in playerList:
        if player.role == "almodo":
            return player

def readszavak():
    szavak = []
    file1 = open(my_path+'/szavak.txt', 'r', encoding='utf-8')
    Lines = file1.readlines()
    for line in Lines:
        szavak.append(line.strip())
    return szavak

def get_n_szo(n):
    selected_choices=[]
    szavak = readszavak()
    for _ in range(n):
        choice = random.choice(szavak)
        szavak.remove(choice)
        selected_choices.append(choice)
    return selected_choices

def round() -> tuple:
    """Egy kört vezényel le"""
    szavak = get_n_szo(5)

    roundAdatok = render(szavak)
    
    print("eredeti szavak:")
    print(szavak)
    print("álmodó tippek:")
    print(roundAdatok["tippek"])
    print("jó szavak:")
    print(roundAdatok["joTippek"])
    print("rossz szavak:")
    print(roundAdatok["rosszTippek"])

    return [len(roundAdatok["rosszTippek"]), len(roundAdatok["joTippek"])]

def printPoints(players:list) -> None:
    for player in players: 
        print(f"{player.name}({player.role}): {player.points}")
    print('\n')

def main() -> None:
    newRound = True
    while (newRound):
        playerList = playersInit()
        os.system('cls')
        dreamerList = []
        for player in playerList:
            playerList = randomRoles(playerList, dreamerList)
            dreamerList.append(getDreamer(playerList))
            guesses = round()
            for player in playerList:
                pontozas.points_handler(player, guesses[0], guesses[1])
            printPoints(playerList)
            for player in playerList:
                player.role = None 
        newGameCheck = input('Szeretnétek mégegy kört játszani? (y/n)')
        if newGameCheck == 'n' or newGameCheck == 'no' or newGameCheck == 'nem':
            newRound = False

if __name__ == "__main__": 
    main()