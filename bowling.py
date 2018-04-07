class Bowling:
    def __init__(self):
        self.overall = 0
        self.bonus = 0

    def evaluate(self, game):
        for n_try, score in enumerate(game):
            if score == 'X':
                self.overall += 10
                if self.bonus > 0 and n_try < len(game)-2:
                    self.overall += 10
                    self.bonus -= 1
                if self.bonus > 0 and n_try < len(game)-2:
                    self.overall += 10
                    self.bonus -= 1
                if n_try < len(game)-2:
                    self.bonus += 2
            if score == '/':
                previous_points = int(game[n_try-1])
                self.overall += (10 - previous_points)
                print("n_try: {}, len(game):{}".format(n_try, len(game)))
                if self.bonus > 0 and n_try < len(game)-2:
                    self.overall += (10 - previous_points)
                    self.bonus -= 1
                if n_try < len(game)-2:
                    self.bonus += 1
            if score.isdigit():
                self.overall += int(score)
                if self.bonus > 0 and n_try < len(game)-2:
                    self.overall += int(score)
                    self.bonus -= 1

        return self.overall
