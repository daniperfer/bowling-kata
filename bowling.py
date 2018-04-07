class Bowling:
    def __init__(self):
        self.overall = 0
        self.bonus = 0
        # there might be bonus points from a frame before (strike or spare) and from two frames before (strike)
        self.bonus_from_previous = 0
        self.bonus_before_previous = 0

    def evaluate(self, game):
        for n_try, score in enumerate(game):
            if score == 'X':
                self.overall += 10
                if self.bonus > 0:
                    self.overall += 10
                    self.bonus -= 1
                if self.bonus > 1:
                    self.overall += 10
                    self.bonus -= 1
                # strikes only give future bonus points if they occur before 10th frame
                if n_try < len(game)-3:
                    self.bonus += 2
            if score == '/':
                # score for second ball in a spare depends on pins knocked down by the previous ball
                previous_points = int(game[n_try-1])
                self.overall += (10 - previous_points)
                if self.bonus > 0:
                    self.overall += (10 - previous_points)
                    self.bonus -= 1
                if self.bonus > 1:
                    self.overall += (10 - previous_points)
                    self.bonus -= 1
                # spares only give future bonus points if they occur before 10th frame
                if n_try < len(game)-2:
                    self.bonus += 1
            if score.isdigit():
                self.overall += int(score)
                if self.bonus > 0:
                    self.overall += int(score)
                    self.bonus -= 1
                if self.bonus > 1:
                    self.overall += int(score)
                    self.bonus -= 1

        return self.overall
