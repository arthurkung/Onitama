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

class Game:

    def __init__(self):
        # set up players
        self.l_player = Player('L',1)
        self.r_player = Player('R',-1)
        # set up board
        self.board_range = ((x,y) for x in range(5) for y in range(5))
        left_row = [Pawn(self.l_player) if i !=2 else Master(self.l_player) for i in range(5)]
        right_row = [Pawn(self.r_player) if i !=2 else Master(self.r_player) for i in range(5)]
        self.board = [left_row, [], [], [], right_row]
        for i in range(1,4):
            self.board[i] = [None for j in range(5)]
        #set up card
        self.l_player.get_card(Lamb(1))
        self.l_player.get_card(Crab(1))
        self.r_player.get_card(Lamb(-1))

    def check_out_of_range(self,x,y):
        if (x,y) in self.board_range:
            return False
        else:
            return True

    def display_board(self):
        for j in self.board:
            output = ''
            for i in j:
                if i is None:
                    output = output + (' ~~ ')
                else:
                    output = output + i.__str__()
            print(output)

    def play_card(self, player, player_opp, orig_loc, card, action):
        '''Example:
        c = Crab()
        game1.play_card(game1.l_player,game1.r_player,[0,2],c,2)
        '''
        delta = card.move[action]
        check = self.check_move_logic(player, orig_loc, card, delta)
        if check != 1:
            print(check)
            return 0
        self.move_piece(orig_loc, delta)
        player.remove_card(card)
        card.set_orientation(player_opp.orientation)
        player_opp.get_card(card)

    def check_move_logic(self,player,orig_loc,card,delta):
        if card not in player.card_list:
            return 'card not in card list'

        orig_loc_x,orig_loc_y = orig_loc
        d_x,d_y = delta
        unit = self.board[orig_loc_x][orig_loc_y]
        if unit is None:
            return 'no unit at location'
        if unit.owner != player:
            return 'unit does not belong to player'
        if self.check_out_of_range(orig_loc_x + d_x,orig_loc_y + d_y):
            return 'target location is out of range'
        target = self.board[orig_loc_x + d_x][orig_loc_y + d_y]
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
        unit = self.board[orig_loc_x][orig_loc_y]
        self.board[orig_loc_x][orig_loc_y] = None
        self.board[orig_loc_x + d_x][orig_loc_y + d_y] = unit


# a = Game()
# a.play_card(a.l_player,a.r_player,(0,2),a.l_player.card_list[1],2)
# a.display_board()
# a.r_player.show_cards()

