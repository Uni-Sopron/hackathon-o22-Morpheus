import random
import json

ROLES = ["mumus", "tunder", "alommano"]


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.role = None
        self.points = 0

def gameInit():
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

    withoutRole = playerList[:]

    dreamer = random.choice(playerList)
    for player in playerList:
        if player.name == dreamer.name:
            player.role = "almodo"
            withoutRole.remove(dreamer)

    for role in data[str(playerCount)].keys():
        #print(role)
        for _ in range(int(data[str(playerCount)][role])):
            randomPlayer = random.choice(withoutRole)
            randomPlayer.role = role
            withoutRole.remove(randomPlayer)
        #print(data[str(playerCount)][role])

    for player in playerList:
        print(player.name)
        print(player.role)
        print()

if __name__ == "__main__": 
    gameInit()
