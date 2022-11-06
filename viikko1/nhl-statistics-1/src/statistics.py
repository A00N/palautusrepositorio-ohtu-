def sort_by_points(player):
    return player.points


def sort_by_goals(player):
    return player.goals


def sort_by_assists(player):
    return player.assists


class Statistics:
    def __init__(self, reader):
        self.reader = reader
        self._players = reader.get_players()

    def players(self):
        return self._players

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, function = 0):
        sort_algorithm = sort_by_points

        if function == 1:
            sort_algorithm = sort_by_points
        if function == 2:
            sort_algorithm = sort_by_goals
        if function == 3:
            sort_algorithm = sort_by_assists

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_algorithm
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result