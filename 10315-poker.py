import sys
from collections import Counter

def method_2(values, types):
    max_hand = values[0]
    # escalera de color
    if types[0] == types[1] == types[2] == types[3] == types[4] \
            and values[0] == values[1] + 1 == values[2]+2 == values[3] + 3 == values[4] + 4:
        return [900 + max_hand]
    # poker
    elif max(list(Counter(values).values())) == 4:
        aux = Counter(values).most_common()[0][0]
        auxiliar = Counter(values).most_common()[1][0]
        return [800 + aux, auxiliar]
    # full
    elif max(list(Counter(values).values())) == 3 and min(list(Counter(values).values())) == 2:
        aux1 = Counter(values).most_common()[0][0]
        aux2 = Counter(values).most_common()[1][0]
        return [700+aux1, aux2]
    # color
    elif types[0] == types[1] == types[2] == types[3] == types[4]:
        return [600]+values
    # escalera
    elif values[0] == values[1] + 1 == values[2]+2 == values[3] + 3 == values[4] + 4:
        return [500 + max_hand]
    # trio
    elif max(list(Counter(values).values())) == 3:
        trio_value = Counter(values).most_common()[0][0]
        aux = []
        for x in values:
            if x is not trio_value:
                aux.append(x)
        return [400+trio_value]+aux
    # doble pareja
    elif list(Counter(values).values()).count(2) == 2:
        if values[1] == values[2] and values[3] == values[4]:
            lone_card = values[0]
        elif values[0] == values[1] and values[3] == values[4]:
            lone_card = values[2]
        elif values[0] == values[1] and values[2] == values[3]:
            lone_card = values[4]
        if values[1] > values[3]:
            aux = values[1]
            aux2 = values[3]
        else:
            aux = values[3]
            aux2 = values[1]
        return [300 + aux, aux2, lone_card]
    # pareja
    elif list(Counter(values).values()).count(2) == 1:
        pair_value = Counter(values).most_common()
        resto = sorted(pair_value[1:5], reverse= True)
        return [200 + pair_value[0][0], resto[0][0], resto[1][0], resto[2][0]]
    # carta mas alta
    else:
        return [100 + max_hand, ]+values[1:5:1]


if __name__ == '__main__':
    hash_map = {"A" : 14, "K":13, "Q":12, "J":11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4,
                      "3": 3, "2": 2}
    while True:
        hands = sys.stdin.readline().strip().split()
        if not hands:
            break
        points_black = []
        points_white = []

        black = hands[0:5]
        white = hands[5:10]

        values = []
        types = []
        for x in black:
            values.append(hash_map[x[0]])
            types.append(x[1])
        values = sorted(values, reverse=True)
        points_black = method_2(values, types)

        values = []
        types = []
        for x in white:
            values.append(hash_map[x[0]])
            types.append(x[1])
        values = sorted(values, reverse=True)
        points_white = method_2(values, types)
        aux = 0
        for b, w in zip(points_black, points_white):
            if b > w:
                aux = 1
                break
            elif b < w:
                aux = 2
                break

        if aux == 1:
            print('Black wins.')
        elif aux == 2:
            print('White wins.')
        else:
            print('Tie.')
