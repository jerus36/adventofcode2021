from .day import Day
import re
from io import StringIO
winners = [
    # Across
    [ 0, 1, 2, 3, 4],
    [ 5, 6, 7, 8, 9],
    [10,11,12,13,14],
    [15,16,17,18,19],
    [20,21,22,23,24],
    # Down
    [0,5,10,15,20],
    [1,6,11,16,21],
    [2,7,12,17,22],
    [3,8,13,18,23],
    [4,9,14,19,24],
    # Diagonal
    # [0,6,12,17,23],
    # [4,8,11,15,19]
]

class Day4(Day):
    def build_cards(self):
        cards = []

        for nc in self.cards:
            card = []
            for w in winners:
                card.append(list(map(lambda i: nc[i], w)))
            cards.append((card,nc))
        return cards
    
    def play_ball(self, ball, card):
        ret = []
        winner = False
        orig = card[1]

        if ball in orig:
            orig.remove(ball)
        for row in card[0]:
            nr = list(row)
            if ball in nr:
                nr.remove(ball)
            
            if len(nr) ==0:
                winner=True
            ret.append(nr)
        return (winner,(ret,orig))
    
    def process_winner(self,card,ix):
        if ix >= len(self.balls):
            return (-1, -1,([],[]))

        ball = self.balls[ix]
        (winner,new_card) = self.play_ball(ball,card)
        if winner:
            return (ix,ball,new_card)
        else:
            return self.process_winner(new_card,ix+1)

    def process_winners(self):
        cards = self.build_cards()
        ret = []
        for card in cards:
            (ix, ball, new_card) = self.process_winner(card,0)
            if ix > -1:
                ret.append((ix,ball, sum(new_card[1])))
            else:
                print("Card is not a winner")
        ret.sort(key= lambda x: x[0])
        return ret 

    def quiz1(self):
        (ix,ball, total) = self.process_winners()[0]
        return ball*total

    def quiz2(self):
        (ix,ball, total) = self.process_winners()[-1]
        return ball*total
    def load(self):
        b, *cs = self.dfile.read().split("\n\n")
        self.balls = list(map(lambda x: int(x), b.strip().split(",")))
        self.cards = []
        for c in cs:
            self.cards.append(list(map(lambda x: int(x), c.strip().split())))
    