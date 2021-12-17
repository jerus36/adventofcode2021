class Day:
    quizzes = []
    def quiz1(self):
        pass
    
    def quiz2(self):
        pass
    
    def load(self):
        pass
    
    def __init__(self, dfile):
        self.dfile = dfile
        self.load()
        self.quizzes.append(self.quiz1)
        self.quizzes.append(self.quiz2)


    def execute(self,quiz):
        if (quiz-1) < len(self.quizzes):
            return self.quizzes[quiz-1]()
        else:
            return "No solution found"