from cards import *
from cards import *

a = Game()
l_player_card_list = [Lamb(),Crab()]
r_player_card_list = [Lamb()]
card_dict = {a.l_player:l_player_card_list,a.r_player:r_player_card_list}
a.distribute_cards(card_dict)


a.play_card(a.l_player,a.r_player,(0,2),'Crab',2)
# a.board.display()

# a.r_player.show_cards()

# copy
b = a.copy()
# b.board.display()
b.play_card(b.r_player,b.l_player,(4,2),'Crab',2)
# b.board.display()
# a.board.display()
# a.r_player.show_cards()
b.r_player.show_cards()
