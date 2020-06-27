from cards import Lamb, Crab
class Piece:

    def __init__(self, owner):
        self.owner = owner

class Master(Piece):

    def __str__(self):
        return 'M({})'.format(self.owner.name)

class Pawn(Piece):

     def __str__(self):
        return 'P({})'.format(self.owner.name)


class Player:

    def __init__(self, name, orientation):
        self.name = name
        self.orientation = orientation
        self.card_list = []

    def get_card(self, card):
        self.card_list.append(card)

    def remove_card(self, card):
        self.card_list.remove(card)

    def show_cards(self):
        for c in self.card_list:
            print(c)

class Board:
    def __init__(self, size,l_player,r_player):
        self.piece_dict = {}
        self.board_range = [(x,y) for x in range(size) for y in range(size)]
        middle_loc = round(size/2)
        l_x = 0
        r_x = size - 1
        l_player.win_loc = (r_x,middle_loc)
        r_player.win_loc = (l_x,middle_loc)
        for y in range(size):
            if y == middle_loc:
                self.piece_dict[(r_x,y)]=Master(r_player)
                self.piece_dict[(l_x,y)]=Master(l_player)
            else:
                self.piece_dict[(l_x,y)]=Pawn(l_player)
                self.piece_dict[(r_x,y)]=Pawn(r_player)

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

    def __init__(self):
        # set up players
        self.l_player = Player('L',1)
        self.r_player = Player('R',-1)
        # set up board
        self.board = Board(5,self.l_player,self.r_player)
        #set up card
        self.l_player.get_card(Lamb(1))
        self.l_player.get_card(Crab(1))
        self.r_player.get_card(Lamb(-1))


    def play_card(self, player, player_opp, orig_loc, card, action):
        '''Example:
        c = Crab()
        game1.play_card(game1.l_player,game1.r_player,[0,2],c,2)
        '''
        delta = card.move[action]
        orig_loc_x,orig_loc_y = orig_loc
        d_x,d_y = delta
        target_loc = (orig_loc_x + d_x,orig_loc_y + d_y)
        check = self.check_move_logic(player, orig_loc, card, target_loc)
        if check != 1:
            print(check)
            return 0
        self.move_piece(orig_loc, delta)
        player.remove_card(card)
        card.set_orientation(player_opp.orientation)
        player_opp.get_card(card)

    def check_move_logic(self,player,orig_loc,card,target_loc):
        if card not in player.card_list:
            return 'card not in card list'

        unit = self.board.get_piece(orig_loc)
        if unit is None:
            return 'no unit at location'
        if unit.owner != player:
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

    def check_winning_condition(self, player):
        win = self.master_reached_win_loc(player) or not self.master_is_alive(player)
        return win

    def master_reached_win_loc(self,player):
        winning_loc_unit = self.board.get_piece(player.win_loc)
        if isinstance(winning_loc_unit,Master):
            if winning_loc_unit.owner == self.l_player:
                return True
        return False

    def master_is_alive(self,player):
        for piece in self.board.piece_dict.values():
            if piece.owner==player and isinstance(piece,Master):
                return True
        return False



a = Game()

a.play_card(a.l_player,a.r_player,(0,2),a.l_player.card_list[1],2)
# print(a.board.piece_dict)
a.board.display()

print(a.check_winning_condition())
# a.r_player.show_cards()

