
from .day import Day
from collections import deque

class Day6(Day): 
    def pop_explosion(self, days):
        for day in range(days+1): 
            birth = self.fish_registry[0]
            self.fish_registry.rotate(-1)
            self.fish_registry[6] = self.fish_registry[6] + birth
        return sum(self.fish_registry)

    def quiz1(self):
        return self.pop_explosion(80)

    def quiz2(self):
        return self.pop_explosion(256)

    
    def load(self):
        self.data = [int(x) for x in self.dfile.read().strip().split(",")]
        self.total_fish = len(self.data)
        reg = [0,0,0,0,0,0,0,0,0]
        for v in self.data:
            reg[v+1] = reg[v+1] + 1
        self.fish_registry = deque(reg)
