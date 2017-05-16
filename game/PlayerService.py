

class PlayerService:

    player_info = ["Player1 Class", "Player2 Class"]

    @classmethod
    def set_player(cls, player, player_number):
        cls.player_info[player_number] = player

    @classmethod
    def get_player(cls, player_number):
        return cls.player_info[player_number]
