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

###########################################################################

#
# Function     : print_card
# Description  : print the card from the integer value
#              : took from 311 code
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
        print(f"10{card_suits[suit]}", end= "")  # the end="" arg will make sure we dont print on a new line
    else:
        print(f"{card_faces[cardty]}{card_suits[suit]}", end= "") # the end="" arg will make sure we dont print on a new line

###########################################################################
#
# Function     : print_cards
# Description  : print a number of cards (no more than 13 on one line)
#
# Inputs       : cards - the array of cards to print
#                num_cards - the number of cards to print
# Outputs      : none
def print_cards(cards, num_cards):
    line_counter = 0
    
    for card_counter in range(num_cards):
        if line_counter == 12:
            # print("\n", end= "")  # dont need in this since python will print on a new line???
            print_card(cards[card_counter])
            # print(" ", end= "")
            print(" ")
            line_counter = 0
        else:
            print_card(cards[card_counter])
            print(" ", end= "")  # the end="" arg will make sure we dont print on a new line
            line_counter += 1
