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
        d1 = DataFrame([list(map(int,list(r.strip()))) for r in self.dfile])
        rows, cols = d1.shape
        d1.insert(cols,cols+1,[9 for x in range(rows)])
        d1.insert(0,-1,[9 for x in range(rows)])

        print(d1)
        mtx = [[9 for x in range(cols+2)] for y in range(rows+2)]
        

