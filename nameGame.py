from pathlib import Path as path
import json
import random

# Create two lists of potential games: the file path and the user-facing title.
games = []

p = path(".")
for i in p.glob("*.json"):

    with open(i, "r") as f:
        games.append(json.loads(f.read()))

# show the user the available titles and have them select one
print("Here are the available games")

for id, game in enumerate(games):
    print("%s: %s" % (id, game.get("title")))

whichGame = int(input("which game number would you like to play?\n"))

# load the contents of the selected game file, or a random file if there's user error
if whichGame < len(games):
    print("Nice choice!\n")
    data_loaded = games[whichGame]
else:
    print("I'll just pick one for you...\n")
    data_loaded = random.choice(games)

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
