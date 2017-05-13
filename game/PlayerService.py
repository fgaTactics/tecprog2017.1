

class PlayerService:

    player_info = ["Player1 Class", "Player2 Class"]
    player1_piece_list = []
    player2_piece_list = []

    @classmethod
    def set_player(cls, player, player_number):
        cls.player_info[player_number] = player

    @classmethod
    def get_player(cls, player_number):
        return cls.player_info[player_number]

    @classmethod
    def set_player1_pieces_list(cls, piece):
        cls.player1_piece_list.append(piece)

    @classmethod
    def set_player2_pieces_list(cls, piece):
        cls.player2_piece_list.append(piece)

    @classmethod
    def get_player1_list(self):
        return self.player1_piece_list

    @classmethod
    def get_player2_list(self):
        return self.player2_piece_list

    @classmethod
    def get_player(cls, player_number):
        return cls.player2_piece_list
