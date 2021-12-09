class Day:
    quizzes = []

    def __init__(self, dfile):
        self.dfile = dfile

    def execute(self,quiz):
        return self.quizzes[quiz-1]()