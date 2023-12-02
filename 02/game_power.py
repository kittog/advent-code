import re
import numpy as np

def game_power(game):
    # returns power for one  game
    split = game.split(":")
    game_id, sets = int(re.findall(r'\d+', split[0])[0]), split[1]
    cols = {"red" : [int(i) for i in re.findall(r'\d+(?= red)', sets)],
    "blue" : [int(i) for i in re.findall(r'\d+(?= blue)', sets)],
    "green" : [int(i) for i in re.findall(r'\d+(?= green)', sets)]}
    power = 1
    for col in cols.keys():
        power *= np.max(cols[col])
    return power

def main():
    with open("02/input.txt", "r") as f:
        txt = f.read().strip()
    games = txt.split("\n")
    sum_power = 0
    for game in games:
        sum_power += game_power(game)
    print(sum_power)

main()