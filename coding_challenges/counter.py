from collections import Counter

def main(n, ws):
    # n = int(input())
    # words = Counter([input() for _ in range(n)])
    words = Counter(ws)
    print(len(words))
    for w in words:
        print(words.get(w), end=' ')


if __name__ == "__main__":
    n = 4
    ws = ["bcdef", "abcdefg", "bcde", "bcdef"]
    main(n, ws)