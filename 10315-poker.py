import sys

def calculate_hand(hand):
    valor = 0
    max_hand = max(hash_map[x[0]] for x in hand)
    #escalera de color
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1] \
        and hash_map[hand[0][0]] == hash_map[hand[1][0]]-1 == hash_map[hand[2][0]]-2 == \
            hash_map[hand[3][0]]-3 == hash_map[hand[4][0]]-4:
        return 900+max_hand
    #poker
    elif max(dict, key=lambda key: dict[key]) == 4:
        return 800+max_hand
    #full
    elif max(dict, key=lambda key: dict[key]) == 3 \
        and min(dict, key=lambda key: dict[key]) == 2:
        return 700+max_hand
    #color
    elif hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return 600+max_hand
    #escalera
    elif hash_map[hand[0][0]] == hash_map[hand[1][0]]-1 == hash_map[hand[2][0]]-2 == \
            hash_map[hand[3][0]]-3 == hash_map[hand[4][0]]-4:
        return 500+max_hand
    #trio
    elif max(dict, key=lambda key: dict[key]) == 3:
        return 400+max_hand
    #doble pareja
    elif list(dict.values()).count('2') == 2:
        return 300+max_hand
    #pareja
    elif list(dict.values()).count('2') == 1:
        return 200+max_hand
    #carta mas alta
    else:
        return 100+max_hand
    return ""

if __name__ == '__main__':
    hash_map = {"A" : 14, "K":13, "Q":12, "J":11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4,
                      "3": 3, "2": 2}
    while True:
        hands = sys.stdin.readline().strip().split()
        if not hands:
            break
        points_black = 0
        points_white = 0
        dict = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0,
                      "3": 0, "2": 0}
        black = hands[0:5]
        white = hands[5:10]
        for x in black:
            dict[x[0]] += 1
        points_black = calculate_hand(black)
        dict = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0,
                "3": 0, "2": 0}
        for x in white:
            dict[x[0]] += 1
        points_white = calculate_hand(white)

        if points_black > points_white:
            print('Black Wins.')
        elif points_white > points_black:
            print('White wins.')
        else:
            print('Tie.')

