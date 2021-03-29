###########################################################################
# imports
import random as rand

# Global vars, constants and symbols
spade_blk = "\u2660"     # a unicode char to represent a black spade 
club_blk = "\u2663"      # a unicode char to represent a black club
heart_blk = "\u2665"     # a unicode char to represent a black heart
diamond_blk = "\u2666"   # a unicode char to represent a black diamond

spade_wht = "\u2664"     # a unicode char to represent a white spade
club_wht = "\u2667"      # a unicode char to represent a white club
heart_wht = "\u2661"     # a unicode char to represent a white heart
diamond_wht = "\u2662"   # a unicode char to represent a white diamond

NUM_CARDS = 52      # the number of cards in a deck
MAX_CARDS = 11      # the max number of cards in a hand

###########################################################################
# Functions

'''
Function        : print_card

Description     : print the card from the integer value
                : took from 311 code

Inputs          : card - the card to print

Outputs         : none

print_card(0), (1), (2): --> 2SPADE, 3SPADE, 4SPADE
'''
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

'''
Function        : print_cards
Description     : print a number of cards (no more than 13 on one line)

Inputs          : cards - the array of cards to print
                  num_cards - the number of cards to print

Outputs         : none
'''
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

'''
Function        : shuffle_cards

Description     : Fisher-Yates algo steps listed for respective lines of code; source for algo steps: wikipedia page for Fisher-Yates Shuffle
                    using the modern implementation as that significantly decreases the run time of the algo
                    the modern algorithm is "common knowledge" i.e. can be found very easily on wikipedia
                    the steps are adapted from pseudo code on the wiki

Inputs          : cards - the array of cards to print
                  num_cards - the number of cards to print

Outputs         : none
'''

def shuffle_cards(cards, num_cards):
    # 1) write out numbers 1 to N, in this case they are written as 0 to 51, contained in arg cards
    strike_idx = 0 # counter to keep track of the index at which to swap (instead of strikes as in "old" implementation)

    # 4) repeat step 2 until all numbers have been struck (for loop)
    while strike_idx <= num_cards - 1:
        # 2) let k be a random card in the deck between [0, num cards remaining in deck-1]
        k = rand.randint(0, strike_idx)

        # 3) count (from beginning) the kth element and "strike it out", add it to the shuffled deck
            # instead of removing and placing into a new array, the elements can be swapped with the largest still unchosen number (MODERN IMPLEMENTATION)
        # code for a basic swap, store val of array at k in temp

        temp = cards[k]
        cards[k] = cards[strike_idx]
        cards[strike_idx] = temp

        strike_idx += 1

    # 5) the sequence obtained by performing swaps is one of the permuations for this set of cards, e.g. a shuffled deck

###########################################################################
# Debugging and testing stuff, will be removed later

test_cards = []
for i in range(52):
    test_cards.append(i)

print(f"deck before shuffle:\n\t{test_cards}")
shuffle_cards(test_cards, len(test_cards))
print(f"deck after shuffle:\n\t{test_cards}")