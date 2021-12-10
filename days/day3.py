from .day import Day
from pandas import read_fwf
import math

cols = ["a","b","c","d","e"]
def compare_vals(df):
        ones = df.sum()
        zeros = df.count().sub(ones)
        mask = ones.combine(zeros, lambda o,z: o-z )
        return mask
def process(df, ix, fn):
    if len(df.index) == 1:
        return df
    g = fn(compare_vals(df).iat[ix])
    return process(df.query(f"{cols[ix]}=={g}"),ix+1,fn)


class Day3(Day):
    def quiz1(self):
        g = "".join(compare_vals(self.data).apply(lambda x: str(int(x>0))).to_list())
        e = "".join(compare_vals(self.data).apply(lambda x: str(int(x<0))).to_list())

        gamma = int(f"0b{g}",2)
        epsilon = int(f"0b{e}",2 )
     
        return gamma * epsilon
        
    def quiz2(self):
        o = "".join(process(self.data,0, lambda x: int(x>=0)).iloc[0].apply(lambda x: str(x)).to_list())
        o2 = int(f"0b{o}",2)
        c = "".join(process(self.data,0, lambda x: int((x*-1)>=0)).iloc[0].apply(lambda x: str(x)).to_list())
        co2 = int(f"0b{c}",2)
        return co2


    def __init__(self, dfile):
        super().__init__(dfile)
        self.data = read_fwf(dfile,widths=[1,1,1,1,1])
        self.data.columns = cols
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)