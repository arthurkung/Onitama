from cards import Card
class Piece:

    def __init__(self, owner = None, orientation = None):
        if orientation is not None:
            self.orientation = orientation
        elif owner is not None:
            self.orientation = owner.orientation
        else:
            self.orientation = 0

    def __str__(self):
        sign = {1:'+', -1:'-'}
        return '{}({})'.format(self.shortname,sign[self.orientation])

class Master(Piece):
    shortname = 'M'
class Pawn(Piece):
    shortname = 'P'


class Player:

    def __init__(self, name, orientation, card_list = None):
        self.name = name
        self.orientation = orientation
        if card_list is None:
            self.card_list = []
        else:
            self.card_list = card_list.copy()

    def get_card(self, card):
        self.card_list.append(card)

    def remove_card(self, card):
        self.card_list.remove(card)

    def show_cards(self):
        for c in self.card_list:
            print(c)

    def copy(self):
        player_copy = Player(self.name, self.orientation, self.card_list)
        return player_copy


class Board:
    def __init__(self, size,l_player,r_player):
        self.size = size
        self.piece_dict = {}
        self.board_range = [(x,y) for x in range(size) for y in range(size)]
        middle_loc = round(size/2)
        l_x = 0
        r_x = size - 1
        self.win_loc = {1:(r_x,middle_loc), -1:(l_x,middle_loc)}
        for y in range(size):
            if y == middle_loc:
                self.piece_dict[(r_x,y)]=Master(r_player)
                self.piece_dict[(l_x,y)]=Master(l_player)
            else:
                self.piece_dict[(l_x,y)]=Pawn(l_player)
                self.piece_dict[(r_x,y)]=Pawn(r_player)

    def set_board(self,piece_dict):
        self.piece_dict = piece_dict.copy()

    def get_piece(self,loc):
        return self.piece_dict.get(loc,None)

    def display(self):
        output = 'Board:'
        for loc in self.board_range:
            *_ ,loc_y = loc
            if loc_y == 0:
                output = output + '\n'
            unit = self.get_piece(loc)
            if unit is None:
                output = output + (' ~~ ')
            else:
                output = output + unit.__str__()

        print(output)

    def check_out_of_range(self,loc):
        if loc in self.board_range:
            return False
        else:
            return True

class Game:

    def __init__(self,size = 5):
        self.size = size
        # set up players
        self.l_player = Player('L',1)
        self.r_player = Player('R',-1)
        # set up board
        self.board = Board(size,self.l_player,self.r_player)
        #set up card
        self.distribute_cards({})

    def distribute_cards(self,card_list_mapping):
        for player, card_list in card_list_mapping.items():
            for card in card_list:
                card.set_orientation(player.orientation)
                player.get_card(card)


    def play_card(self, player, player_opp, orig_loc, card_name, action):
        '''Example:
        c = Crab()
        game1.play_card(game1.l_player,game1.r_player,[0,2],c,2)
        '''

        dummy_card = Card(name = card_name)
        card_index = player.card_list.index(dummy_card)
        card = player.card_list[card_index]
        delta = card.move[action]
        orig_loc_x,orig_loc_y = orig_loc
        d_x,d_y = delta
        target_loc = (orig_loc_x + d_x,orig_loc_y + d_y)
        check = self.check_move_logic(player, orig_loc, card, target_loc)
        if check != 1:
            print(check)
            return 0
        self.move_piece(orig_loc, delta)
        if self.check_winning_condition(player,player_opp):
            print('Player {} has won the game'.format(player.name))
        player.remove_card(card)
        card.set_orientation(player_opp.orientation)
        player_opp.get_card(card)

    def check_move_logic(self,player,orig_loc,card,target_loc):
        if card not in player.card_list:
            return 'card not in card list'

        unit = self.board.get_piece(orig_loc)
        if unit is None:
            return 'no unit at location'
        if unit.orientation != player.orientation:
            return 'unit does not belong to player'
        if self.board.check_out_of_range(target_loc):
            return 'target location is out of range'
        target = self.board.get_piece(target_loc)
        if target is not None:
            if target.owner == player:
                return 'target location occupied by friendly unit'
        return 1



    def move_piece(self, orig_loc, delta):
        '''
        example: self.move_piece([0,2],[1,1])

        '''

        orig_loc_x,orig_loc_y = orig_loc
        d_x,d_y = delta
        target_loc = (orig_loc_x + d_x,orig_loc_y + d_y)
        unit = self.board.get_piece(orig_loc)
        self.board.piece_dict.pop(orig_loc)
        self.board.piece_dict[target_loc] = unit

    def check_winning_condition(self, player, player_opp):
        win = self.master_reached_win_loc(player) or not self.master_is_alive(player_opp)
        return win

    def master_reached_win_loc(self,player):
        winning_loc_unit = self.board.get_piece(self.board.win_loc[player.orientation])
        if isinstance(winning_loc_unit,Master):
            if winning_loc_unit.orientation == player.orientation:
                return True
        return False

    def master_is_alive(self,player):
        for piece in self.board.piece_dict.values():
            if piece.orientation==player.orientation and isinstance(piece,Master):
                return True
        return False

    def copy(self):
        new_game_instance = Game(self.size)
        # copy player and card list
        new_game_instance.l_player = self.l_player.copy()
        new_game_instance.r_player = self.r_player.copy()
        # copy board and pieces
        new_game_instance.board.set_board(self.board.piece_dict)
        return new_game_instance
