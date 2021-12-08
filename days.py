from day import Day
from pandas import read_fwf


class Day3(Day):
    def quiz1(self):
        half = self.data.size()/2
    
        
    def quiz2(self):
        pass

    def __init__(self, dfile):
        super().__init__(dfile)
        self.data = read_fwf(dfile,widths=[1,1,1,1,1])
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)

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
       
        
class Day1(Day):
    def quiz1(self):
        ret = 0
        last = self.data[0]
        for d in self.data[1:]:
            if last < d:
                ret = ret + 1
            last = d
        return ret

    def quiz2(self):
        ret = 0
        last = sum(self.data[0:3])
        for ix in range(3,len(self.data)-2):
            v = sum(self.data[ix:ix+3])
            if last < v:
                ret = ret +1
            last = v
        return ret
        
    def __init__(self, f):
        super().__init__(f)
        self.data = list(map(lambda x: int(x),f.readlines()))
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)

days = [Day1,Day2,Day3]