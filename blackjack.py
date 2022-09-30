#This program simulates a blackjack game between two players. Program continues until all cards have been dealt.
#MIS285 - 9.9 - Blackjack Simulator
#Author: Michael Shiiki-Morris

def main():
    deck = create_deck()
    deal_cards(deck)
    
#Library for the deck of cards - used same formatting as provided by book. 
def create_deck():
    deck = {'Ace of Spades':1,'2 of Spades':2,'3 of Spades':3,
            '4 of Spades':4,'5 of Spades':5,'6 of Spades':6,
            '7 of Spades':7,'8 of Spades':8,'9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10,'King of Spades':10,
            
            'Ace of Hearts':1,'2 of Hearts':2,'3 of Hearts':3,
            '4 of Hearts':4,'5 of Hearts':5,'6 of Hearts':6,
            '7 of Hearts':7,'8 of Hearts':8,'9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10,'King of Hearts':10,

            'Ace of Clubs':1,'2 of Clubs':2,'3 of Clubs':3,
            '4 of Clubs':4,'5 of Clubs':5,'6 of Clubs':6,
            '7 of Clubs':7,'8 of Clubs':8,'9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10,'King of Clubs':10,
            
            'Ace of Diamonds':1,'2 of Diamonds':2,'3 of Diamonds':3,
            '4 of Diamonds':4,'5 of Diamonds':5,'6 of Diamonds':6,
            '7 of Diamonds':7,'8 of Diamonds':8,'9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10,'King of Diamonds':10}            
    return deck

def deal_cards(deck):
    hand_one = 0 #starting values for both players
    hand_two = 0
    import random #random to provide true random numbers. Update to Python 3.7 changed .popitem functionality
    while len(deck) > 1: #Make sure there are cards in the deck
        while hand_one < 21 and hand_two < 21: #Check score, if no one at 21 draw another card
            card, value = random.choice(list(deck.items())) #draws random card from deck
            print('Player 1 draws:',card)
            deck.pop(card, value) #removes the card that was drawn
            deck_size = len(deck) #set deck size to current size after drawing a card
            if len(deck) < 1: #catch for not enough cards
                print('The deck is out of cards')
                break
            if value == 1 and hand_one < 11: #logic for handling drawing an Ace
                hand_one += 11
            else:
                hand_one += value
            card, value = random.choice(list(deck.items())) #repeat above process for hand two
            print('Player 2 draws is:',card)
            deck.pop(card, value)
            if len(deck) < 1:
                print('The deck is out of cards')
                break
            if value == 1 and hand_two < 11:
                hand_two += 11
            else:
                hand_two += value
        #print scores for both players after round is completed
        print('Player one total:', hand_one) 
        print('Player two total:', hand_two,'\n')
        hand_one = 0 #reset hands to zero
        hand_two = 0
        
main()