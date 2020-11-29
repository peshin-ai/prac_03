import random


# TODO: check score
def check(Score):
    #TODO: check code and write the outcome of Score
    OutFile = open('results.txt', 'a')
    if Score < 50:
        print(str(Score) + " is Bad", file=OutFile)
    elif Score < 90:
        print(str(Score) + " is Passable", file=OutFile)
    else:
        print(str(Score) + " is Excellent", file=OutFile)
    OutFile.close()


def main():
    # TODO: ensure that the file is empty
    OutFile = open('results.txt', 'w')
    OutFile.close()
    # TODO: get score
    NumTest = random.randint(1, 20)
    for i in range(NumTest):
        Score = random.randint(0, 100)
        check(Score)


if __name__ == '__main__':
    main()
