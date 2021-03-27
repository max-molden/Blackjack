spade_blk = "\u2660"     # a unicode char to represent a black spade 
club_blk = "\u2663"      # a unicode char to represent a black club
heart_blk = "\u2665"     # a unicode char to represent a black heart
diamond_blk = "\u2666"   # a unicode char to represent a black diamond

spade_wht = "\u2664"     # a unicode char to represent a white spade
club_wht = "\u2667"      # a unicode char to represent a white club
heart_wht = "\u2661"     # a unicode char to represent a white heart
diamond_wht = "\u2662"   # a unicode char to represent a white diamond

num_cards = 52      # the number of cards in a deck
max_cards = 11      # the max number of cards in a hand

# Functions

########################################
#
# Function     : print_card
# Description  : print the card from the integer value
#
# Inputs       : card - the card to print
# Outputs      : none
# print_card(0), (1), (2): --> 2SPADE, 3SPADE, 4SPADE
def print_card(card):
    # card_faces = "234567891JQKA"
    card_faces = ["2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K", "A"]
    card_suits = [spade_blk, club_blk, heart_blk, diamond_blk]
    # card_suits = [spade_wht, club_wht, heart_wht, diamond_wht]
    suit = card // 13
    cardty = card % 13

    if (cardty == 8):
        print(f"10{card_suits[suit]}")
    else:
        print(f"{card_faces[cardty]}{card_suits[suit]}")




