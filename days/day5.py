
from .day import Day

def is_ortho(A,B):
    return A[0] == B[0] or A[1] == B[1]


def get_modifier(a,b):
    if a==b:
        return (0,0)
    else:
        return (int((b-a)/abs(b-a)), int(abs(b-a)))

def calc_line(line, graph={}):
    (x1,y1,x2,y2) = line
    # Shortcut only works because everything is right triangles 

    dx,lx = get_modifier(x1,x2)
    dy,ly = get_modifier(y1,y2)

    d = max(ly,lx)+1
    for ix in range(d):
        x = x1 + (ix * dx)
        y = y1 + (ix * dy)
        P = (x,y)
        if P in graph:
            graph[P] = graph[P]+1
        else:
            graph[P] = 1
    return graph

def calc_points(lines):
    graph = {}
    for line in lines:
        graph = calc_line(line, graph)
    return graph

class Day5(Day):
    
    def quiz1(self):
        lns = [a['line'] for a in filter(lambda x: x['ortho'],self.lines)]
        ml = list(filter(lambda e: e[1]>1,calc_points(lns).items()))

        return len(ml)

    def quiz2(self):
        lns = [a['line'] for a in self.lines]
        ml = list(filter(lambda e: e[1]>1,calc_points(lns).items()))

        return len(ml)
    
    def init_plot(self):
        fig = plt.figure(clear=True)
        ax = fig.add_subplot(111)
        ax.set_aspect(1)
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)
        return ax
    
    def load(self):
        lines = []
        for ln in self.dfile.readlines():
            (SA,dummy,SB) = ln.strip().split()
            SA = SA.split(",")
            SB = SB.split(",")
            A = (int(SA[0]),int(SA[1]))
            B = (int(SB[0]),int(SB[1]))
            lins = (A[0],A[1],B[0],B[1])
            ortho = is_ortho(A,B)
            lines.append({'line':lins,'ortho':ortho})
        self.lines = lines

    def __init__(self, dfile):
        super().__init__(dfile)
        self.load()
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)
