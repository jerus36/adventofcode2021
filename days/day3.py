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
    print(df)
    g = fn(compare_vals(df).iat[ix])
    process(df.query(f"{cols[ix]}=={g}"),ix+1,fn)


class Day3(Day):
    def quiz1(self):
        g = "".join(compare_vals(self.data).apply(lambda x: str(int(x>0))).to_list())
        e = "".join(compare_vals(self.data).apply(lambda x: str(int(x<0))).to_list())

        gamma = int(f"0b{g}",2)
        epsilon = int(f"0b{e}",2 )
     
        return gamma * epsilon
        
    def quiz2(self):
        df = process(self.data,0, lambda x: int(x>0))
     
        print(df)
        return 11


    def __init__(self, dfile):
        super().__init__(dfile)
        self.data = read_fwf(dfile,widths=[1,1,1,1,1])
        self.data.columns = cols
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)