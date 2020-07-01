from cards import Lamb, Crab
from game import Game

a = Game()
l_player_card_list = [Lamb(),Crab()]
r_player_card_list = [Lamb()]
card_dict = {a.players[1]:l_player_card_list,a.players[-1]:r_player_card_list}
a.distribute_cards(card_dict)
a.board.display()
# a.players[1].show_cards()
a.play_card(a.players[1],a.players[-1],(0,2),'Crab',2)
# a.board.display()

# a.players[-1].show_cards()

# copy
# b = a.copy()
# b.board.display()
# b.play_card(b.players[-1],b.players[1],(4,2),'Crab',2)
# b.board.display()
# a.board.display()
# a.players[-1].show_cards()
# b.players[-1].show_cards()
