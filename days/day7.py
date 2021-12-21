from .day import Day

def calc_distance(a,b,c):
    return (b-a)*c

class Day7(Day):

    def calculate(self, fn):
        arr = list(self.data)
        shift = int(0-min(arr))
        mx = max(arr) + shift
        register = [0 for n in range(mx+1)]
        costs = [0 for n in range(mx+1)]
        for v in arr:
            register[v+shift] = register[v+shift]+1
        
        for d in range(len(register)):
            for idx, pos in enumerate(register):
                cost = fn(d,idx,pos)
                costs[d] = costs[d] + cost        
        return min(costs) 


    def quiz1(self):
        return self.calculate(lambda d,i,p: abs(d-i) * p )
    def quiz2(self):
        # MATHED!
        return self.calculate(lambda d,i,p: int((abs(d-i)*(abs(d-i)+1)/2)*p) )

    def load(self):
        self.data = [int(x) for x in self.dfile.read().strip().split(",")]

        