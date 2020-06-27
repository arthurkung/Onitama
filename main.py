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

    def __init__(self, name):
        self.name = name
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
        self.l_player = Player('L')
        self.r_player = Player('R')
        # set up board
        left_row = [Pawn(self.l_player) if i !=2 else Master(self.l_player) for i in range(5)]
        right_row = [Pawn(self.r_player) if i !=2 else Master(self.r_player) for i in range(5)]
        self.board = [left_row, [], [], [], right_row]
        for i in range(1,4):
            self.board[i] = [None for j in range(5)]
        #set up card
        self.l_player.get_card(Lamb(1))
        self.l_player.get_card(Crab(1))
        self.r_player.get_card(Lamb(-1))

    def display(self):
        for j in self.board:
            output = ''
            for i in j:
                if i is None:
                    output = output + (' ~~ ')
                else:
                    output = output + i.__str__()
            print(output)

    def play_card(self, orig_loc, card, action):
        '''Example:
        c = Crab()
        a.play_card([0,2],c,2)
        '''
        delta = card.move[action]
        self.move_piece(orig_loc, delta)


    def move_piece(self, orig_loc, delta):
        '''
        example: self.move_piece([0,2],[1,1])

        '''

        orig_loc_x = orig_loc[0]
        orig_loc_y = orig_loc[1]
        d_x = delta[0]
        d_y = delta[1]
        unit = self.board[orig_loc_x][orig_loc_y]
        self.board[orig_loc_x][orig_loc_y] = None
        self.board[orig_loc_x + d_x][orig_loc_y + d_y] = unit


a = Game()
# c = Crab()
# a.play_card([0,2],c,2)
# a.play_move([0,2],[1,1])
# a.display()


a.l_player.show_cards()
