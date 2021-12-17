from argparse import ArgumentParser
from days import days


parser = ArgumentParser()
parser.add_argument("--day", type=int)
parser.add_argument("--quiz", type=int)
parser.add_argument("--file", type=str)

def main(day, quiz, filename):
    with open(filename) as f:
        day_class = days[day-1](f)
        res = day_class.execute(quiz)
        print(f"Day {day}, Quiz {quiz}, result = {res}")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.day, args.quiz, args.file)