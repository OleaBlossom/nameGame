from pathlib import Path as path
import json
import random

# create two lists of potential games: the file path and the user-facing title
game_paths = []
game_titles = []
p = path(".")
for i in p.glob("*.json"):
    game_paths.append(str(i))

    with open(i, "r") as f:
        game_titles.append(json.loads(f.read()).get("title"))


# show the user the available titles and have them select one
print("Here are the available games")

for id, game in enumerate(game_titles):
    print("%s: %s" % (id, game))

whichGame = int(input("which game number would you like to play?\n"))

# load the contents of the selected game file, or a random file if there's user error
if whichGame < len(game_titles):
    print("Nice choice!\n")
    with open(str(game_paths[whichGame]), "r") as f:
        data_loaded = json.loads(f.read())
else:
    print("I'll just pick one for you...\n")
    with open(str(random.choice(game_paths)), "r") as f:
        data_loaded = json.loads(f.read())

description = data_loaded.get("desc", "something interesting")
print("\nOkay! Let's find out %s\nbased on your answers to a few simple questions...\n" % (description))

randomCapital = chr(random.randint(65, 90))
results = []
questions = data_loaded.get("inputQuestions")

for entry in questions:
    q = entry.get("question")
    result = entry.get("result")

    # Collect the user's input.
    answer = input(q + "\n")

    # For a question that expects a "character" result type,
    # use only the first letter of the given answer to build the name.
    # If there's user error, find the result from a random character
    if entry.get("type") == "character":
        c = answer.upper()[0]
        results.append(result.get(c,
                                  result.get(randomCapital)))

    # for all other types, try to find the result from the exact answer given
    # if the answer given doesn't exist, choose a random result
    else:
        results.append(result.get(answer, result.get(
            random.choice(list(result)))))

# print the result for the user
print(data_loaded.get("output") + " ".join(results))
