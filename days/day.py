class Day:
    quizzes = []

    def __init__(self, dfile):
        self.dfile = dfile

    def execute(self,quiz):
        if (quiz-1) < len(self.quizzes):
            return self.quizzes[quiz-1]()
        else:
            return "No solution found"