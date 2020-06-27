class Card:
    action_list = []
    name = 'empty card'
    def __init__(self,orientation):
        self.set_orientation(orientation)


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
    action_list = [(-2,-2), (1,2)]



class Lamb(Card):

    name = 'Lamb'
    action_list = [(-1,0), (1,1)]

