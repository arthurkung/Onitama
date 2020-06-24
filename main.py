class Card:

    def __init__(self):
        self.move = []


    def __str__(self):
        return self.display()

    def display(self):
        output = ''
        for i in range(-2,3):
            for j in range(-2,3):
                if (i,j) in self.move:
                    output = output + 'x|'
                elif (i,j) == (0,0):
                    output = output + 'o|'
                else:
                    output = output + '~|'

            output = output[:-1] + '\n'

        return output

class Crab(Card):

    def __init__(self):
        self.move = [(-2,-2), (1,2)]


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

    def display(self):
        for j in self.board:
            output = ''
            for i in j:
                if i is None:
                    output = output + (' ~~ ')
                else:
                    output = output + i.__str__()
            print(output)

    def play_move(self, orig_loc, delta):
        '''
        example: self.play_move([0,2],[1,1])

        '''

        orig_loc_x = orig_loc[0]
        orig_loc_y = orig_loc[1]
        d_x = delta[0]
        d_y = delta[1]
        unit = self.board[orig_loc_x][orig_loc_y]
        self.board[orig_loc_x][orig_loc_y] = None
        self.board[orig_loc_x + d_x][orig_loc_y + d_y] = unit


# a = Game()

# a.play_move([0,2],[1,1])
# a.display()

a = Crab()
print(a)
