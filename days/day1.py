from .day import Day

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
        
    def load(self):
        self.data = list(map(lambda x: int(x),self.dfile.readlines()))
        