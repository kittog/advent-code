# part 1
import numpy as np

def point(card):
    card_id, numbers = card.split(":")
    winning = [int(i) for i in numbers.split("|")[0].split()]
    my_numbers = [int(i) for i in numbers.split("|")[1].split()]
    c = 0
    for i in range(len(my_numbers)):
        if my_numbers[i] in winning:
            if c == 0: c += 1
            else: c *= 2
            # p *= 2 if c!=1 else 1
    # print(c)
    return c

def main():
    with open("04/input.txt", "r") as f:
        txt = f.read().strip()
    cards = txt.split("\n")
    points = []
    for card in cards:
        points.append(point(card))
    # print(points)
    print(np.sum(points))
