from cards import *
from game import Game

class Game_Tree:
    tree = dict()
    def __init__(self, tree = None, game = None, turn = 0):
        if tree is not None:
            self.tree = tree.copy()
        else:
            if game is None:
                game = Game()
            self.tree = {(None,None,turn):game}  # (move, parent ,turn):game
        turn_num = [x[1] for x in self.tree.keys()]
        self.start_turn = min(turn_num)

    def give_direct_descendants(self,loc):
        return [(k0,k1,k2) for k0,k1,k2 in self.tree.keys() if k1==loc]

    def get_game(self,loc):
        return self.tree[loc]

    def give_birth(self,loc,child):
        self.tree[loc] = child

class Game_Controller:
    def __init__(self, card_dict = {1:[Lamb(),Crab()],-1:[Lamb()]}):
        self.game_tree = Game_Tree()
        self.game_tree_loc = (None,None,0)
        game = self.game_tree.get_game(self.game_tree_loc)
        card_dict = {game.players[orientation]:card_list for orientation,card_list in card_dict.items()}
        game.distribute_cards(card_dict)

    def display_board(self,tree_loc=None):
        if tree_loc is None:
            game = self.game_tree.get_game(self.game_tree_loc)
        else:
            game = self.game_tree.get_game(tree_loc)
        game.board.display()

    def display_player_card(self,tree_loc=None,curr_player=1):
        if tree_loc is None:
            game = self.game_tree.get_game(self.game_tree_loc)
            orientation = self.get_current_play_orientation(self.game_tree_loc)
        else:
            game = self.game_tree.get_game(tree_loc)
            orientation = self.get_current_play_orientation(tree_loc)
        p = game.players[orientation * curr_player]
        p.show_cards()

    def get_current_play_orientation(self,tree_loc):
        turn_num = tree_loc[2] + 1
        if turn_num%2 == 1:
            return 1
        else:
            return -1

    def play_move(self,tree_loc,move):
        orig_loc, card_name, action = move
        orientation = self.get_current_play_orientation(tree_loc)
        opp_orientation = orientation * -1
        current_game = self.game_tree.get_game(tree_loc)
        current_player = current_game.players[orientation]
        current_opp_player = current_game.players[opp_orientation]
        move_played = current_game.copy()
        move_player = move_played.players[orientation]
        move_opp_player = move_played.players[opp_orientation]
        move_played.play_card(move_player,move_opp_player,orig_loc,card_name,action)
        return move_played



    def extend_tree_from_node(self, tree_loc):
        current_game = self.game_tree.get_game(tree_loc)
        orientation = self.get_current_play_orientation(tree_loc)
        avail_moves = self.detect_avail_moves(orientation,current_game)
        turn_num = tree_loc[2] + 1
        for move in avail_moves:
            new = self.play_move(tree_loc,move)
            self.game_tree.give_birth((move,tree_loc,turn_num),new)
        return avail_moves

    def detect_avail_moves(self, orientation,current_game):
        # detects all possible moves from a game state and extend game tree
        current_player = current_game.players[orientation]
        card_list = current_player.card_list
        player_pieces = {loc:piece for loc,piece in current_game.board.piece_dict.items() if piece.orientation == orientation}
        avail_moves = []
        for orig_loc in player_pieces.keys():
            for card in card_list:
                for action,delta in enumerate(card.move_list,1):
                    orig_loc_x,orig_loc_y = orig_loc
                    d_x,d_y = delta
                    target_loc = (orig_loc_x + d_x,orig_loc_y + d_y)
                    check = current_game.check_move_logic(current_player, orig_loc, card, target_loc)
                    if check == 1:
                        move = (orig_loc,card.name,action)
                        avail_moves.append(move)
        return avail_moves

# test area
a=Game_Controller(card_dict = {1:[Lamb(),Crab()],-1:[Lamb()]})
move_list = a.extend_tree_from_node((None,None,0))
# print(move_list)
# a.display_player_card()
# a.display_board()
move = ((0,2),'Crab',2) # orig loc, card_name, action
# new = a.play_move((None,None,0),move)
# a.game_tree.give_birth((move,(None,None,0),1),new)


# desc=a.game_tree.give_direct_descendants((None,None,0))
# print(len(desc))

g = a.game_tree.get_game((((0, 1), 'Crab', 2), (None, None, 0), 1))
g.board.display()

