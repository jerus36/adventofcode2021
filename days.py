from day import Day
from pandas import read_fwf
import math

def agg_mask(v):
    return str(round(v.mean()))
def agg2_mask(o,z):
    if o>=z:
        return 1
    else:
        return 0
def compare_vals(df):
        ones = df.sum()
        zeros = df.count().sub(ones)
        mask = ones.combine(zeros, agg2_mask )
        return mask

class Day3(Day):
    def quiz1(self):
        return self.gamma * self.epsilon
        
    def quiz2(self):
        ser = self.gamma_series
        df = self.data
        cols = self.data.columns
        res = "0b"
        for i in range(5):
            g = ser.iat[i]
            c = cols[i]
            df = df.query(f"{c}=={g}")
            ser = compare_vals(df)
            res = res + str(g)

        return int(res, 2)


    def __init__(self, dfile):
        super().__init__(dfile)
        self.data = read_fwf(dfile,widths=[1,1,1,1,1])
        self.data.columns = ['a','b','c','d','e']
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)
        self.gamma_series = compare_vals(self.data)
        self.epsilon_series = self.gamma_series.apply(lambda x: str((int(x)+1)%2))
        self.gamma = int(f'0b{"".join(self.gamma_series.to_list())}', 2)
        self.epsilon = int(f'0b{"".join(self.epsilon_series.to_list())}', 2)

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