import random
import json

class Player:
    def __init__(self, name:str) -> None:
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
    f = open('roles.json')
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

    for playerNum in range(int(playerCount)):
        print("Add meg a " + str(playerNum+1) + ". nevét: ")
        name = input()
        playerList.append(Player(name))

    return playerList

def randomRoles(playerList:list) -> list:
    """Szerepet oszt minden játékoshoz.
    
    Returns:
        list: A játékosok listája szerepekkel.
    """
    f = open('roles.json')
    data = json.load(f)
    f.close()

    withoutRole = playerList[:]

    dreamer = random.choice(playerList)
    for player in playerList:
        if player.name == dreamer.name:
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

    return playerList


########
# Terv #
########
def round():
    kartyak = []
    helyesTippek = []
    rosszTippek = []
    almodoTippek = []
    while True:
        kartya = None
        print("Álmodó tipp: ")
        tipp = input()
        almodoTippek.append(tipp)
        if tipp == "exit": break
        elif helyesTipp: 
            almodoTippek.append(tipp)
            helyesTippek.append(tipp)
        else: 
            almodoTippek.append(None)

def helyesTipp(kartyaSzo, tipp): False # Balázs írja

if __name__ == "__main__": 
    playerList = playersInit()
    playerList = randomRoles(playerList)
    
    # Terv
    #option = 0
    #while option == 0:
    #    print('[1] új játék')
    #    print('[2] START')
    #    if option == 1:
    #        playerList = playersInit()
    #    elif option == 2:
    #        while True: round()
