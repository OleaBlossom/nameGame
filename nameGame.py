from pathlib import Path as path
import json
import random

# Create a list of potential games.


def load_games(game_path="."):
    games = []

    p = path(".")
    for i in p.glob("*.json"):

        with open(i, "r") as f:
            games.append(json.loads(f.read()))
    return games


def play_game(games):

    # Show the user the available titles and have them select one.
    print("Here are the available games")

    for n, game in enumerate(games):
        print("%s: %s" % (n, game.get("title")))

    user_selection = int(input("which game number would you like to play?\n"))

    # Allow the user to select a game, or choose a random file.
    if user_selection < len(games):
        print("Nice choice!\n")
        selected_game = games[user_selection]
    else:
        print("I'll just pick one for you...\n")
        selected_game = random.choice(games)

    description = selected_game.get("desc", "something interesting")
    print("\nOkay! Let's find out %s\nbased on your answers to a few simple questions...\n" % (description))

    results = []
    questions = selected_game.get("inputQuestions")

    for entry in questions:
        q = entry.get("question")
        result = entry.get("result")

        # Collect the user's input.
        answer = input(q + "\n")

        # For a question that expects a "character" result type,
        # use only the first letter of the given answer to build the name.
        # If something goes wrong, find the result from a random character.
        if entry.get("type") == "character":
            single_char = answer.upper()[0]
            random_capital = chr(random.randint(65, 90))
            default = result.get(random_capital)
            results.append(result.get(single_char, default))

        # For all other types, try to find the result from the exact answer given.
        # If the answer given doesn't exist, choose a random result.
        else:
            result_list = list(result)
            random_result = result.get(random.choice(result_list))
            results.append(result.get(answer, random_result))

    # Print the result for the user.
    print(selected_game.get("output") + " ".join(results))


if __name__ == "__main__":

    games = load_games()
    play_game(games)
