from .day import Day
from pandas import read_fwf
import math

cols = []
def compare_vals(df):
        ones = df.sum()
        zeros = df.count().sub(ones)
        mask = ones.combine(zeros, lambda o,z: o-z )
        return mask
def process(df, ix, fn):
    if len(df.index) == 1:
        return df
    cmp = compare_vals(df)
    g = fn(cmp.iat[ix])
    return process(df.query(f"{cols[ix]}=={g}"),ix+1,fn)

def q2_co2(x):
    if x>=0:
        return 0
    else:
        return 1

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
        cdf = process(self.data,0, q2_co2)
        c = "".join(cdf.iloc[0].apply(lambda x: str(x)).to_list())
        co2 = int(f"0b{c}",2)

        return co2 * o2

    def load(self):
        with open(self.dfile.name) as d:
            ln = d.readline()
        col_cnt = len(ln.strip())
        widths = []
        for i in range(col_cnt):
            widths.append(1)
            cols.append(F"c{i}")
        self.data = read_fwf(self.dfile,widths=widths,names=cols)
    