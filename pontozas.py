from game import Player

def points_handler(player: Player, incorrect_guesses: int, correct_guesses: int) -> dict:
    role = player.role
    if role == "mumus":
        player.points += incorrect_guesses
    elif role == "tunder":
        player.points += correct_guesses
    elif role == "alommano":
        if correct_guesses == incorrect_guesses:
            player.points = correct_guesses + 2    
        elif correct_guesses - incorrect_guesses == 1 or correct_guesses - incorrect_guesses == -1:
            if correct_guesses > incorrect_guesses:
                player.points = correct_guesses       
            else:
                player.points = incorrect_guesses 

        elif correct_guesses - incorrect_guesses >= 2:
            if correct_guesses > incorrect_guesses:
                player.points = incorrect_guesses
            else:
                player.points = correct_guesses

        elif correct_guesses - incorrect_guesses <= -2:
            if correct_guesses > incorrect_guesses:
                player.points = incorrect_guesses
            else:
                player.points = correct_guesses
    elif role == "almodo":
        query = int(input("Az álmodó fel tudta idézni az álmokat? Ha igen, akkor írj be egy 1-est, ha nem, akkor 2-est: ",))
        if query == 1:
            player.points = correct_guesses + 2
        else:
            player.points = correct_guesses