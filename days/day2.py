from .day import Day
class Day2(Day):
    def quiz1(self):
        pos = 0
        depth = 0
        for (k,v) in self.data:
            if k == "forward":
                pos = pos + v
            elif k == "down":
                depth = depth + v
            elif k == "up":
                depth = depth - v
            else:
                raise IOError("Unknown command")

        return pos * depth

    def quiz2(self):
        pos = 0
        depth = 0
        aim = 0
        for (k,v) in self.data:
            if k == "forward":
                pos = pos + v
                depth = depth + (aim * v)
            elif k == "down":
                aim = aim + v
            elif k == "up":
                aim = aim - v
            else:
                raise IOError("Unknown command")
        return pos * depth

    def __init__(self, dfile):
        super().__init__(dfile)
        self.data = list(map(lambda x: (x.split()[0],int(x.split()[1])), dfile.readlines()))
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)