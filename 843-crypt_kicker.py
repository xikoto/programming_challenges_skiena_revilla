import sys
from collections import defaultdict

if __name__ == '__main__':
    num_words = int(sys.stdin.readline())
    words_dict = defaultdict(list)
    for n_word in range(num_words):
        word = sys.stdin.readline().strip()
        words_dict[len(word)].append(word)

    frases = []
    while True:
        frase = sys.stdin.readline()
        if not frase:
            break

        frases.append(frase)

    for frase in frases:

        frase 
        for palabra in frase:

