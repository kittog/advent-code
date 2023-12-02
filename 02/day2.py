import numpy as np
import re

def set_check(set, colours):
    # checks one set of a game
    set_clean = set.replace(",", "").split()
    check = []
    for i in np.arange(0, len(set_clean), 2):
        n = int(set_clean[i])
        col = set_clean[i+1]
        check.append(colours[col] >= n)
    # print(set, check)
    return check # list of booleans

def game_sets(game, colours):
    # checks sets of one game
    split = game.split(":")
    game_id, sets = int(re.findall(r'\d+', split[0])[0]), split[1].split(";")
    n_sets = len(sets) # number of sets
    c = 0 # counter for sets that work out
    for set in sets:
        check = set_check(set, colours)
        c += np.sum(check) == len(check)
        # set is plausible in this configuration
    # print(c, n_sets)
    if c == n_sets: 
        return game_id
    else:
        return 0

def main():
    with open("02/input.txt", "r") as f:
        txt = f.read().strip()
    games = txt.split("\n")
    colours = {"red":12, "green":13, "blue":14}
    sum_games = 0
    for game in games:
        sum_games += game_sets(game, colours)
    print(sum_games)

main()