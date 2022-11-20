class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def all_players(self):
        return self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self.all_players():
            if player.nationality == nationality:
                players.append(player)

        players.sort(key = lambda x: x.get_points(), reverse=True)
        return players