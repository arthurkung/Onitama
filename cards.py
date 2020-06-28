class Card:
    set_orientation = 1
    action_list = []
    name = 'empty card'

    def __init__(self,orientation=1, name = None, action_list = None):
        self.set_orientation(orientation)
        if not name is None:
            self.name = name
        if not action_list is None:
            self.action_list = action_list


    def __eq__(self,other):
        return self.name == other.name

    def __str__(self):
        return self.display()

    def display(self):
        output = self.name+':\n'
        move_dict = {x:str(i) for i,x in enumerate(self.move_list,1)}
        move_dict[(0,0)] = 'o'
        for i in range(-2,3):
            for j in range(-2,3):
                output = output + move_dict.get((i,j),'~')+'|'

            output = output[:-1] + '\n'

        return output

    def set_orientation(self, orientation):
        if orientation == 1:
            self.orientation = 1
            self.move_list = self.action_list.copy()

        if orientation == -1:
            self.orientation = -1
            self.move_list=[(-x,-y) for(x,y) in self.action_list]

        self.move = {i:x for i,x in enumerate(self.move_list,1)}
        return self.orientation


class Crab(Card):

    name = 'Crab'
    action_list = [(0,-2), (1,0), (0,2)]



class Lamb(Card):

    name = 'Lamb'
    action_list = [(-1,0), (1,1)]


class Card_all_dir(Card):

    name = 'Card_all_dir'
    action_list = [(-1,0), (1,0),(0,-1),(0,1)]


class Card_lr(Card):

    name = 'Card_lr'
    action_list = [(0,-1),(0,1)]


class Card_flr(Card):

    name = 'Card_flr'
    action_list = [(1,0),(0,-1),(0,1)]


class Tiger(Card):

    name = 'Tiger'
    action_list = [(2,0),(-1,0)]


class Dragon(Card):

    name = 'Dragon'
    action_list = [(1,2),(1,-2),(-1,-1),(-1,1)]


