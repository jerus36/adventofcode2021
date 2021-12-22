from .day import Day
from pandas import DataFrame, Series

def sweep_for_mines(df):
    rows,cols = df.shape
    print(df)
    for row in range(rows):
        for col in range(cols):
            p = df.iat[row,col]
            a = df.iat[row-1,col-1]
            print(a)
            print (f"x={col}, y={row}, val={p}")
            # if col > 0 and col > cols:

    return []

def calculate_score(arr, score):
    ret = 0
    top = len(arr)-1
    for i, p in enumerate(arr[1:]):
        idx = i+1
        if (idx >= top and p < arr[idx-1]) or (p < arr[idx-1] and p < arr[idx+1]):
            print(f"low_point={p}")
            ret = ret + score(p)
    print()
    return ret

class Day9(Day):
    def quiz1(self):
        score = 0
        low_points = sweep_for_mines(self.data)

        fn = lambda x: x+1
        for r in self.data:
            score = score + calculate_score(r,fn)
        return score
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
        print(self.data)

