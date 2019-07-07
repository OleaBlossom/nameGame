import os
import json
import random

# create two lists of potential games: the file path and the user-facing title
game_paths = []
game_titles = []
base_path = "/Users/oleablossom/Documents/Python/hello/"
for i in os.listdir(base_path):
    if i.endswith(".json"):
        game_paths.append("%s" % i)
        with open(i, "r") as f:
            game_titles.append(json.loads(f.read()).get("title"))


# show the user the available titles and have them select one
print("Here are the available games")

for id, game in enumerate(game_titles):
    print("%s: %s" % (id, game))

whichGame = int(input("which game number would you like to play?\n"))

# load the contents of the selected game file, or a random file if there's user error
if whichGame in game_titles:
    print("Nice choice!\n")
    with open(str(game_paths[whichGame]), "r") as f:
        data_loaded = json.loads(f.read())
else:
    print("I'll just pick one for you...\n")
    with open(str(random.choice(game_paths)), "r") as f:
        data_loaded = json.loads(f.read())

description = data_loaded.get("desc", "something interesting")
questions = data_loaded.get("inputQuestions", {})
randomCapital = chr(random.randint(65, 90))
results = []

print("\nOkay! Let's find out %s\nbased on your answers to a few simple questions...\n" % (description))

for question in questions.keys():
    currentGameData = questions[question]
    answer = input(question + "\n")

    # for the "character" type, find the result from the first letter of the given answer
    # if there's user error, find the result from a random character
    if currentGameData.get("_type") == "character":
        results.append(currentGameData.get(answer.upper()[0],
                                           currentGameData.get(randomCapital)))

    # for all other types, try to find the result from the exact answer given
    # if the answer given doesn't exist, choose a random result
    else:
        results.append(currentGameData.get(answer, currentGameData.get(
            random.choice(list(currentGameData)[1:]))))

#print the result for the user
print(data_loaded.get("output") + " ".join(results))