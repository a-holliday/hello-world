import random


class GamePlay:


    pointDeck ={'Ace of Hearts': 11, '1 of Hearts': 1, '2 of Hearts':2, '3 of Hearts':3, '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6, '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9, '10 of Hearts':10, 'Jack of Hearts':10, 'Queen of Hearts':10, 'King of Hearts':10,
        'Ace of Diamonds':11, "1 of Diamonds":1, "2 of Diamonds":3, "3 of Diamonds":3, "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6, "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9, "10 of Diamonds":10, "Jack of Diamonds":10, "Queen of Diamonds":10, "King of Diamonds":10,
        "Ace of Spades":11, "1 of Spades":1, "2 of Spades":2, "3 of Spades":3, "4 of Spades":4, "5 of Spades":5, "6 of Spades":6, "7 of Spades":7, "8 of Spades":8, "9 of Spades":9, "10 of Spades":10, "Jacks of Spades":10, "Queen of Spades":10, "King of Spades":10,
        "Ace of Clubs":11, " 1 of Clubs":1, "2 of Clubs":2, "3 of Clubs":3, "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6, "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10, "Jack of Clubs":10, "Queen of Clubs":10, "King of Clubs":10
            }

    deck = ["Ace of Hearts", "1 of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts",
            "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts",
            "King of Hearts"
            "Ace of Diamonds", "1 of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds",
            "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds",
            "Queen of Diamonds", "King of Diamonds",
            "Ace of Spades", "1 of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades",
            "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jacks of Spades", "Queen of Spades",
            "King of Spades",
            "Ace of Clubs", " 1 of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs",
            "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"
            ]
    #class fields: Deck (dictionary) standOrHit (char) startOrQuit (char)
    standOrHit = ''
    startOrQuit = ''

    # functions in GamePlay: startMenu, round, , gameOver

    totalCash = 0


    def startMenu(self,p1):

        print("Welcome to Black Jack!")
        p1.currentCash = int(input("Enter starting cash amount (enter 0 to quit)"))
        if (p1.currentCash == 0):
            return
        #totalCash = p1.currentCash
        print(p1.currentCash)
        p1.betCash = int (input("Enter bet amount"))
        if p1.betCash > p1.currentCash:
            print("Can't bet more cash than you have!")
            instance.startMenu(p1)



    def round(self, p1, dealer):
        dealer.deal(1,self)
        print("****Dealer's Hand****")
        dealer.displayHand()
        print("*********************")
        dealer.displayPoints(self)

        print("")

        p1.deal(2, self)
        print("***Player's Hand***")
        p1.displayHand()
        print("*********************")
        p1.displayPoints(self)
        while (self.standOrHit != "s" and p1.points < 21):
            self.standOrHit = input("Press \"s\" to stand or \"h\" to hit ")
            if (self.standOrHit == "h"):
                p1.deal(1,self)
                print("****Player's Hand*****")
                p1.displayHand()
                print("**********************")
                p1.displayPoints(instance)
            if (p1.points > 21):
                #p1.displayPoints(instance)
                print("Bust! You lose!")
                p1.currentCash -= p1.betCash
                instance.continueGame(p1)
            if p1.points == 21:
                #p1.displayPoints(instance)
                print("Perfect 21! You win!")
                p1.currentCash += p1.betCash
                instance.continueGame(p1)

        print("Dealer's turn...")
        #dealer.displayHand()
        while (dealer.points <= p1.points and dealer.points < 21):
            dealer.deal(1, instance)
            print("*****Dealer's Hand*****")

            dealer.displayHand()
            print("************************")
            dealer.displayPoints(instance)
        if (dealer.points > 21):
            print("Dealer busts! You win!")
            p1.currentCash += p1.betCash
            instance.continueGame(p1)

        else :
            print("Dealer wins!")
            p1.currentCash -= p1.betCash
            instance.continueGame(p1)

    def continueGame(self, p1):
        print("*******Cash *******")
        print("$ " + str(p1.currentCash))
        if p1.currentCash == 0:
            print("******Game Over!*****")
            exit()
        choice = input("Play again?")
        if choice == "y":
            anotherInstance = GamePlay()
            p1.betCash = int(input("Enter new bet amount"))
            while (p1.currentCash < p1.betCash ):
                p1.betCash = int (input("Enter an amount lower than current cash"))
            p1.clearHand()
            dealer.clearHand()
            anotherInstance.round(p1, dealer)
        elif choice == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input")
            instance.continueGame(p1)




class Player:

    #class fields: betCash(int) currentCash(int) hand(array) points(int)
    def __init__(self):
        self.betCash = 0
        self.currentCash = 0
        self.hand =[]
        self.points = 0





    def deal(self, num, instance):
        for i in range(num):
            random.shuffle(instance.deck)
            self.hand.append(instance.deck[i])
            instance.deck.pop(i)

    def displayHand(self):
        for i in range (len(self.hand )):
            print(self.hand[i])




    def displayPoints(self, instance):
        self.points = 0
        for card in self.hand:
            self.points += instance.pointDeck[card]
        if self.points > 21:
            for i in range(len(self.hand)):
                if self.hand[i].find("Ace") == 1 and self.points > 21:
                    print("Lowering value of Ace")
                    self.points -= 10
                    break

        print("Points: " + str(self.points))

    def clearHand(self):
        self.hand = []





instance = GamePlay()
p1 = Player()
dealer = Player()
instance.startMenu(p1)
instance.round(p1,dealer)
#instance.continueGame(p1)


