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
        self.l_player = Player('L')
        self.r_player = Player('R')
        left_row = [Pawn(self.l_player) if i !=2 else Master(self.l_player) for i in range(5)]
        right_row = [Pawn(self.r_player) if i !=2 else Master(self.r_player) for i in range(5)]
        none_row = [None for i in range(5)]
        self.board = [left_row, none_row, none_row, none_row, right_row]

    def display(self):
        for j in self.board:
            output = ''
            for i in j:
                if i is None:
                    output = output + (' ~~ ')
                else:
                    output = output + i.__str__()
            print(output)


a = Game()
a.display()

