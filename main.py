from utils.common import(
    said_yes,
    menu_maker
)
from number_guesser.number_guesser import main as start_number_guesser

def main():
    while True:
        print("\033c")
        menu_maker("Jordela's Games Main Menu", "Welcome to the main menu, select a game based on the number below and have fun!")
        print(f"Game List:")

        games_list = get_games_list()

        for index, game in enumerate(games_list):
            print(f"{index}: {game}")
        exit_index = len(games_list)
        print(f"{exit_index}: exit")

        response_game_index = int(input("> Which game would you like to play?: "))

        if response_game_index is exit_index:
            print(f"Exiting, thanks for coming")
            break
        else:
            selected_game = games_list[response_game_index]
            play_game(selected_game)



def get_games_list():
    games_list = [
        "number guesser"
        ]
    return games_list

def play_game(selected_game: str):
    print(f"Loading {selected_game}")
    print("\033c") 
    if selected_game == "number guesser":
        start_number_guesser()


if __name__ == "__main__":
    main()

