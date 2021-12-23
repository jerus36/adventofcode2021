from .day import Day
from pandas import DataFrame, Series
def is_local_min(mtx, offset):
    mn = 10
    mx = 0
    my = 0

    for col, m in mtx.iteritems():
        imin = m.idxmin()
        nmn = m.min()
        if nmn < mn:
            mn = nmn
            mx = col
            my = imin
    return offset == (my,mx)

def sweep_for_mines(df, score):
    rows,cols = df.shape
    ret = []
    for row in range(1,rows-1):
        for col in range(1,cols-1):
            mtx = df.iloc[row-1:row+2,col-1:col+2]
            if is_local_min(mtx, (row,col)):
                ret.append(score(df.iat[row,col]))
    return ret

def slice_column(ser):
    ret = []
    tot = 0
    ser.replace(9)

    for k,v in ser.iteritems():
        if v == 9:
            if tot > 0:
                ret.append(tot)
                tot = 0
        else:
            tot = tot + v
    return ret

def slice_the_pie(df,score=lambda x:x):
    partitions = []
    for label, s in df.iteritems():
        cols = slice_column(s)
        print(cols)
    return DataFrame(partitions)

class Day9(Day):
    def quiz1(self):
        fn = lambda x: x+1
        low_points = sweep_for_mines(self.data, fn)
        return sum(low_points)        
    def quiz2(self):
        parts = slice_the_pie(self.data)
        return parts
    def load(self):
        d = []
        for idx, row in enumerate(self.dfile):
            nrow = [9]
            nrow.extend(map(int,list(row.strip())))
            nrow.append(9)

            if idx == 0:
                border = [9 for x in range(len(nrow))]
                d.append(border)

            d.append(nrow)
        d.append(border)

        self.data = DataFrame(d)

