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
# Notes

'''
Passing by reference:
    - weird in python
        * doesnt really work like other languages
    - for arrays
        * it will work if I have a global (e.g. test_cards that is a full deck from 0 to 51) and I try to use, for example, shuffle_cards
            -* however, I have to make sure that I do not rename the argument in the function, if I modify its indices or use a .method() -- see shuffle cards, it will work

Printing a whole deck:
    - works normal for original deck
    - but if i sort the deck using my sort_cards function it looks weird since the 10s mess it up
        * consider changing it later to add a space if not printing a 10

Classes:
    - consider making classes for things
        * person?
            -* dealer and player (rename class)
        * cards/deck/hand (rename)
            -* deck, hand etc.
'''

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

'''
 Function       : hand_value
 Description    : return the value of the hand

 Inputs         : cards - the array of cards in the hand
                  num_cards - the number of cards in the hand

 Outputs        : value of the cards in the given hand - counts aces at the end

 Notes          : it is important to count aces at the end since they can count as either 1 or 11, the way this is done is very clear in the code, its quite simple
 '''

def hand_value(cards, num_cards):
    hand_sum = 0    # cumualtive sum for value of the hand
    ace_count = 0   # counter for number of aces, to be added at the end

    for i in range(num_cards): # for each card in the deck cards[] do:
        if cards[i] % 13 == 8: # if the card is a card 2-10 (use % 13 due to suit offset of 13) it is worth face value
            hand_sum += (cards[i] % 13) + 2 # need to add to cumulaitve sum, but need to add 2 more than the value at the index as a 2 is worth 2 points but represented by a 0 --> 0 + 2 = 2 points
        elif (cards[i] % 13 == 9) or (cards[i] % 13 == 10) or (cards[i] % 13 == 11): # if the card is a Jack, Queen, or King (represented by 9,10,11) (% 13 for suit offset)
            hand_sum += 10 # these cards are each worth 10
        else:
            ace_count += 1 # if the card is anyting else (only Aces are left) increase the ace count and add the ace value later

    for j in range(ace_count): # for each ace in the hand/deck do:  
        if hand_sum + 11 > 21: # if making the ace worth 11 would cause a "bust", make the ace a 1 and add to total sum
            hand_sum += 1
        else:
            hand_sum += 11  # otherwise make the ace worth 11 and add to the total sum

    return hand_sum

'''
Function        : sort_cards

Description     : sort a collection of cards using the bubble sort algorithm

Inputs          : hand - the cards to sort
                  num_cards - the number of cards in the hand

Outputs         : none
'''
def sort_cards(hand, num_cards):
    # bubble sort algo: perform a series of swaps
        # start with first element of array, compare current to next, if current is larger than next, swap the elements
        # otherwise skip to the next set of elements (current + 1 and current + 2) and increse the pointer
        # this will take several passes as it takes the largest unsorted element up to the index before the smallest sorted element (towards the end)
        # this must be repeated two ways (two for loops)
    
    # the outer loop controls the passes to sort - once the first pass is complete and the larges element is moved to the end of the array (and elements that need to go the front move up one spot)
    # another pass will need to complete and bring the next largest unsorted element to the spot right before the larges sorted element at the end
    for _ in range(num_cards - 1):
        for pointer in range(num_cards - 1):    #  the inner loop does the comparison for each set of 2 elements (first and second, second and third, thrid and fourth, etc.)
            if hand[pointer] % 13 > hand[pointer + 1] % 13:  # does comparisons if the value % 13 (suit offset) creates a swap condition (see above)
                temp = hand[pointer]
                hand[pointer] = hand[pointer + 1]
                hand[pointer + 1] = temp
            elif hand[pointer] % 13 == hand[pointer + 1] % 13: # if the values%13 are equal (i.e. 2HEARTS and 2CLUBS) then they need to still be put in suit order
                if hand[pointer] > hand[pointer + 1]: # in this case use the actual value not the % 13 as those are already in suit order
                    temp = hand[pointer]
                    hand[pointer] = hand[pointer + 1]
                    hand[pointer + 1] = temp
                else: # increments pointer if comparision doesn't need to be made
                    pointer += 1 
            else: # increments pointer if comparison doesn't need to be made
                pointer += 1

'''
Function        : dealer_play
Description     : dealer decision to hit or stand (hit on anything less than 17)

Inputs          : hand - cards dealer has
                  num_cards, the number of cards in dealer hand

Outputs         : 0 = stand, 1 = hit

Notes           : not really sure if I am going to need this but most likely
'''
def dealer_play(hand, num_cards):
    dealer_value = hand_value(hand, num_cards)

    if dealer_value <= 16: # if the dealer's cards total to 16 or less they have to hit per the rules of the game
        return 1
    else:  # otherwise they have to stand per the rules of the game
        return 0

'''
Function        : player_play

Description     : player decision to hit or stand

Inputs          : hand - cards player has
                  num_cards - the number of cards in player hand
                  dealer_card - the dealers face up card

Outputs         : 0 = stand, 1 = hit

Notes           : most likely WILL NOT need this in the final product, but could be good for the beginning/testing
'''
def player_play(hand, num_cards, dealer_card):
    # use this function to create a blackjack strategy for the player to decide if they should hit or stand for each time they are asked
    # Strategy is as follows:
        # if the player's hand totals to 11 or less they will hit every time
        # if the player's hand totals to higher than 17 (assuming they haven't bust and can still play) they will stand every time
        # if the player's hand totals to higher than 11 and less than or equal to 17, they hit when the assumed dealer's value is higher than their own and stand otherwise
    # Assumed dealer's value (int assumed_dealer) is a helpful tool to use in this black jack strategy.  A good rule of thumb is to assume that the dealer's face down card is
    # a face card. This helps the player assess the situation and make a good choice. For this reason, the player will assume that the dealer's hand evaluates to whatever card
    # they have plus 10.

    player_value = hand_value(hand, num_cards)
    assumed_dealer = (dealer_card % 13) + 2 + 10 #  see above def.; use mod 13 to get value from 0 to 12 (how deck is represented), + 2 since 0 represents 2 card etc., + 10 assumed face card

    if player_value <= 11: # if player value is 11 or less, always hit
        return 1
    elif player_value <= 17: # if player value is in the range (11, 17] choice depends on assumed dealer value
        if assumed_dealer > player_value: # if dealer value is higher than player value, hit
            return 1
        else: # if dealer value is lower than or equal to player, stand
            return 0
    else: # if player value is greater than 17, stand
        return 0

###########################################################################
###########################################################################
'''
This is probably th end of the functions I want to copy from 311 assignment
I dont think I want play_hand
I do think it could be good to look at it though, along with main

I need to figureo out my gameplan from here forward
'''
###########################################################################
###########################################################################


###########################################################################
# Debugging and testing stuff, will be removed later

test_cards = []
for i in range(52):
    test_cards.append(i)

print(f"ARRAY - deck before shuffle:\n\t{test_cards}\n")
print(f"\tVISUAL - \n{print_cards(test_cards, len(test_cards))}")
shuffle_cards(test_cards, len(test_cards))
print(f"ARRAY - deck after shuffle:\n\t{test_cards}\n")
print(f"\tVISUAL - \n{print_cards(test_cards, len(test_cards))}")
sort_cards(test_cards, len(test_cards))
print(f"ARRAY - deck after re-sorting:\n\t{test_cards}")
print(f"\tVISUAL - \n{print_cards(test_cards, len(test_cards))}")
