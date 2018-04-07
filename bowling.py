class Bowling:
    def __init__(self):
        self.overall = 0

    def evaluate(self, game):
        self.overall = 0
        bonus_scores = [0] * len(game)
        # The bonus scores table keeps how many bonus scores have to be added to the overall score in each try
        # A strike ('X') allocates two bonus scores: one in the next try, and another one in the try after the next
        # A spare ('/') only allocates a bonus score in the next try
        # Thus, the maximum number of bonus scores to add in any try is 2

        for k_try, score in enumerate(game):
            if score == 'X':
                # This is a strike
                self.overall += 10 * (1 + bonus_scores[k_try])

                # A strike only allocates future bonus points if it occur before the 10th frame of a game
                # If a strike occurred in the last try of a game, it was an extra ball --> no bonus points allocation
                # If it occurred in the second-to-last try: it was an extra ball --> no bonus points allocation
                # If it occurred in the third-to-last try: it was the last (10th) frame: no bonus points allocation
                if k_try < len(game) - 3:
                    bonus_scores[k_try+1] += 1
                    bonus_scores[k_try+2] += 1

            if score == '/':
                # This is a spare: in two tries all pins were knocked down
                # The score for a second try of a spare depends on how many pins were knocked down in the first try
                current_try_score = 10 - int(game[k_try - 1])
                self.overall += current_try_score * (1 + bonus_scores[k_try])

                # A spare only give future bonus points if it occur before the 10th frame of a game
                # If a spare occurred in the last try of a game, it was an extra ball --> no bonus points allocation
                # If it occurred in the second-to-last try: it was the last (10th) frame: no bonus points allocation
                if k_try < len(game) - 2:
                    bonus_scores[k_try+1] += 1

            if score.isdigit():
                self.overall += int(score) * (1 + bonus_scores[k_try])

        return self.overall
