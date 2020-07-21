'''
Zachary Sisco, Unit 5 Assignment 2

The purpose of this program is to create an interactive card game of Acey
Deucey using my library containing a deck of cards, Cards. The program will follow
Acey Deucey rules as described on Wikipedia.
'''
#import deck library
import Cards

#create class for the game
class AceyDeucey():

    #create class variables, manipulate deck
    game = Cards.cardDeck()
    game.buildDeck()
    game.shuffle()

    #create constructor, take in playerName and playerCash
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    #create method for the intro to the game to modularize code a bit 
    def intro(self):

        print("\nWelcome to Acey Deucey, ", self.name, "!\n")
        
        print("You have ", self.cash, "dollars to play with.\n")
        
        print("Let's get started!\n")

    #create method for playing the game
    def playGame(self):

        ante = int(input("How much are you willing to ante?: \n"))
        self.cash -= ante
        
        print("\nHere are your two cards: ")
        card1 = AceyDeucey.game.deal()
        card2 = AceyDeucey.game.deal()

        print("\nTime to wager. You can only bet up to the ante.")
        wager = int(input("How much are you willing to bet?: \n"))
        
        
        if wager > ante:
            print("\nThat bet is not possible, try again please.")
            wager = int(input("How much are you willing to bet?: "))
            

        #Wiki rules High/Low situation 
        if card1 == card2:
            print("Your cards match. You must now guess if the next card is higher or lower.")
            guess = str(input("High or Low? :"))

            print("You guessed ", guess, ". Here is your card: ")
            card3 = AceyDeucey.game.deal()

            if (guess == 'High') and (card3 > card1):
                self.cash += (wager*2)
                print("You won! You win ", wager, "dollars and now have ", self.cash, "dollars.")
                return 
                
            elif (guess == 'High') and (card3 < card1):
                self.cash -= wager
                print("You lost. You lose ", wager, "dollars and now have ", self.cash, "dollars.")
                return
                
            elif (guess == 'Low') and (card3 < card1):
                self.cash += (wager*2)
                print("You won! You win ", wager, "dollars and now have ", self.cash, "dollars.")
                return
                
            else:
                self.cash -= wager
                print("You lost. You lose ", wager, "dollars and now have ", self.cash, "dollars.")
                return

        #if no High/Low, then proceed as usual
        print("\nYour bet has been placed. Here is your third card: ")
        card3 = AceyDeucey.game.deal()

        #compare cards, determine result
        if (card3 > card1 and card3 < card2) or (card3 > card2 and card3 < card1):
            print("\nYou won!")
            self.cash += (wager*2)
            print("You just won ", wager, "dollars and now have " , self.cash, "dollars!")
            
        elif (card3 == card1 or card3 == card2):
            print("\nYou have two identical values. You must now add to the pot double your wager.")
            wager = wager*2
            self.cash -= wager
            print("You now have ", self.cash, "dollars.")
            
        else:
            print("\nYou lost.")
            self.cash -= wager
            print("You just lost ", wager, "dollars and now have ", self.cash, "dollars.")

        
        #see if player wants to play again
        play = str(input("\nWould you like to play again? Y/N: "))
        print()
        
        if play == 'Y':
            AceyDeucey.playGame(self)
                    
        else:
            print("Have a great day!")
                

#create instance variables
playerName = str(input("What is your name?: "))
playerCash = int(input("How much money do you want to play with today?: "))

#create player object, run program
player = AceyDeucey(playerName, playerCash)
player.intro()
player.playGame()
