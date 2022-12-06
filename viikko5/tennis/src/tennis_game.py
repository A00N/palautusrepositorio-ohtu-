# Entities:
START_P = 0
ROUND_W = 1
FORTY_P = 40


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {player1_name: START_P, player2_name: START_P}

    def player_home(self):
        return list(self.players.keys())[0]

    def player_quest(self):
        return list(self.players.keys())[1]

    def player_home_points(self):
        return self.players[self.player_home()]

    def player_quest_points(self):
        return self.players[self.player_quest()]

    def won_point(self, player_name):
        self.players[player_name] += ROUND_W

    def score_difference(self):
        diff = abs(self.player_home_points() - self.player_quest_points())
        return diff

    def tie(self):
        return self.player_home_points() == self.player_quest_points()

    def scores_over_four(self):
        return (self.player_home_points() or self.player_quest_points()) >= FORTY_P

    def score_statuses(self, score: int):
        statuses = ["Love", "Fifteen", "Thirty", "Forty"]
        return statuses[score]

    def when_tie(self, score: int):
        if score >= FORTY_P:
            return "Deuce"
        return self.score_statuses(score) + "-All"

    def winning_statuses(self, diff: int):
        statuses = ["-", "Advantage player1", "Win for player1", "Win for player2", "Advantage player2"]
        return statuses[diff]

    def get_score(self):
        if self.tie():
            return self.when_tie(self.player_home_points())

        elif self.scores_over_four():
            return self.winning_statuses(self.score_difference())

        else:
            return self.score_statuses(self.player_home_points()) + "-" + self.score_statuses(
                self.player_quest_points())
