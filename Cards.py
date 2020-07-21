'''
Zachary Sisco, Unit 5 Assignment 1

The purpose of this program is to use OOP to simulate a deck of playing cards.
The deck of cards will be the object and have its own class, cardDeck.
This class will have multiple methods in it:
Deal - this will return the card on the top of the deck.
Shuffle - Once all 52 cards have been dealt, this method will shuffle the deck.
Fan - This will show the deck from top to bottom
isOrdered - This will check to see if the deck is in proper order.
Order - This will place the cards in proper order.
'''

#import random module to allow for random shuffle function
import random

#create class to create the cards to be used for the deck
class playingCards:

    #class variables
    #create lists of suits/values so index value can be used as ranking value
    Suits = ['C', 'D', 'H', 'S']
    Values = ['None', 'None', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    #create constructor 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #use str operation override to return name of card as string and not data
    def __str__(self):
        return playingCards.Values[self.value] + playingCards.Suits[self.suit]

    #use operation override methods so that cards can be compared, bypassing function call error
    def __gt__(self,other):
        card1 = self.suit, self.value
        card2 = other.suit, other.value
        return card1 > card2

    def __lt__(self,other):
        card1 = self.suit, self.value
        card2 = other.suit, other.value
        return card1 < card2

    def __eq__(self,other):
        card1 = self.suit, self.value
        card2 = other.suit, other.value
        return card1 == card2 

#create class to create the deck
class cardDeck:

    #create class variable to track number of cards dealt
    cardCount = 0 

    #create constructor, create lists for deck and deck of dealt cards
    def __init__(self):
        self.deck = []
        self.dealtCards = []

    #create the deck of cards, calling playingCards class to assign card values 
    def buildDeck(self):

        for s in range(0,4):
            for v in range(2,15):
                card = playingCards(s, v)
                self.deck.append(card)

        return self.deck

    #shuffle the deck
    def shuffle(self):

        random.shuffle(self.deck)
        return self.deck

    #shuffle the deck of dealt cards, return the cards to the playing deck, clear dealt cards deck
    def shuffleDealt(self):

        if cardDeck.cardCount == 52:
            for card in self.dealtCards:
                self.deck.append(card)

            random.shuffle(self.deck)
            self.dealtCards.clear()
            
        else:
            pass
            
        return self.deck, self.dealtCards
    
    #show the deck
    def fan(self):

        for card in self.deck:
            print(card)

    #deal a card off the top of the deck, add the dealt card to the dealt cards deck
    def deal(self):

        cardDeck.cardCount += 1
        
        dealtCard = self.deck.pop()
        self.dealtCards.append(dealtCard)
        print(dealtCard)
        
        return dealtCard.value

    #use list sort function to order the deck
    def Order(self):

        self.deck.sort()

        return self.deck

    #use list sorted function to check if the deck is sorted properly
    def isOrdered(self):
        
        if self.deck == sorted(self.deck):
            print("Deck is in order.")
            return True
        
        else:
            print("Deck is not in order.")
            return False


#create instance variable
#play = cardDeck()

#use instance variable to call methods 
#play.buildDeck()
#play.shuffle()
#play.fan()
#play.deal()
#play.shuffleDealt()
#play.Order()
#play.isOrdered()
