
# https://www.hackerrank.com/challenges/the-minion-game/problem
# 11.10.2020

def minion_game(string):
    p1 = 0
    p2 = 0
    for i in range(len(string)):
        if vowel(string[i]):
            p1 += (len(string) - i)
        else:
            p2 += (len(string) - i)

    if p1 > p2:
        print("Kevin " + str(p1))
    elif p1 < p2:
        print("Stuart " + str(p2))
    else:
        print("Draw")


def vowel(char):
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        return True
    return False


if __name__ == '__main__':
    s = input()
    minion_game(s)
