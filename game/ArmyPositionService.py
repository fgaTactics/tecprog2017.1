


class ArmyPositionService:

    player_piece_list = []

    @classmethod
    def set_player_list(cls, list_piece_playe):
        cls.player1_piece_list = list_piece_playe

    @classmethod
    def get_player_list(cls):
        return cls.player_piece_list
