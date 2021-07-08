from nltk.tokenize import WhitespaceTokenizer
import random


def main():
    filename = input().strip()
    with open(filename, 'r', encoding='utf-8') as f:
        corpus = f.read()

    wst = WhitespaceTokenizer()
    tokens = wst.tokenize(corpus)
    len_t = len(tokens)
    bigrams = []
    for i in range(0, len_t):
        if i < len_t - 1:
            bigrams.append([tokens[i], tokens[i+1]])

    # print("Number of bigrams:", len_t - 1)
    # print("Unique tokens:", len(set(tokens)))

    markov_chain = {}

    for bigram in bigrams:
        markov_chain.setdefault(bigram[0], {}).setdefault(bigram[1], 0)
        # markov_chain[bigram[0]].setdefault(bigram[1], 0)
        markov_chain[bigram[0]][bigram[1]] += 1

    def generate(head):
        tails = []
        weights = []
        for tail in markov_chain[head]:
            tails.append(tail)
            weights.append(markov_chain[head][tail])
        return random.choices(tails, weights)[0]

    punctuation_marks = ['.', '?', '!']

    for _ in range(10):
        word = random.choice(tokens)
        while not word.istitle() or any(pm in word for pm in punctuation_marks):
            word = random.choice(tokens)
        sentence = [word]
        counter = 1
        while True:
            word = generate(word)
            sentence.append(word)
            counter += 1
            if any(pm in word for pm in punctuation_marks) and counter >= 5:
                break
        print(' '.join(sentence))

    # q = input().strip()
    # while q != "exit":
    #     try:
    #         head = q
    #         print("Head:", head)
    #         for tail in markov_chain[head]:
    #             print("Tail:", tail, "\tCount:", markov_chain[head][tail])
    #     except KeyError:
    #         print("Key Error. The requested word is not in the model. Please input another word.")
    #     # except IndexError:
    #     #     print("Index Error. Please input an integer that is in the range of the corpus.")
    #     # except (TypeError, ValueError):
    #     #     print("Type Error. Please input an integer.")
    #     print()
    #     q = input().strip()


if __name__ == "__main__":
    main()
