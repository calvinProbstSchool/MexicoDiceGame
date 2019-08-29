# mexicoMethods.py
# This is a file to hold all of the different methods that can be used to run the game

from mexicoDie import Die

from colorama import init

init()


class Game:
    # Number of players - will be replaced in game setup w/ user input
    # After a player loses, this will decrease by 1. When it == 1, the remaining player wins

    def __init__(self):
        self.numPlayers = 1
        self.playerList = [0]
        self.livesList = [0]
        self.rollList = [0]
        self.rankList = [0]
        self.dice1 = Die(6)
        self.firstOpen = True

    def newGame(self):
        self.numPlayers = 1
        self.playerList = [0]
        self.livesList = [0]
        self.rollList = [0]
        self.rankList = [0]
        self.dice1 = Die(6)
        self.firstOpen = True
        self.getPlayers()

    @staticmethod
    def continuePrompt():
        input("Press any key to continue\n")
        print("\r")

    def getPlayers(self):
        userInputNumb = ""
        if self.firstOpen:
            userInputNumb = input("Welcome to Mexico! Enjoy your game! \nHow many players?\n")
        else:
            userInputNumb = input()
        self.numPlayers = int(userInputNumb)
        self.firstOpen = False
        if self.numPlayers < 2:
            print("Please try again, that number is invalid \nHow many players? ")
            self.getPlayers()
        else:
            self.setupGame()

    @staticmethod
    def printMexicoFlag():
        print(
            "\033["
            "1;30;40m"
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "             ,/,,//*((                  \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "          ., ,(*(//(((,,*               \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "    /,  #(**/*(.(#//(*(((#*.            \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "   /.,.(((((/,//(/*/#//*#*#(/           \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "   //////  //((/(#//#/(((/(((/          \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "       */ ,,//*//((#/#,#*#*#(#*         \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m         "
            ",*.   *.*  /*/(/#((#(#/#/#(#/#,#(        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "  , //    /*/*/((((//(#((#*(/((/        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "  * **     /(/(////#(  / (/*.(*#        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m         "
            ",  //, . ./, (///((/((*     .(/,(    #(  \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m     (.  "
            "**.  * //,**/(/(((#/((/(/,   /, (   # /  \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m    /#    "
            "*##, */,  .(((((/((#(((/(//,   (  * .   \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m    ,(,   "
            ",###/  (*/        /(( ##////* .    /    \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m     ..   "
            "  *##(####.#/#/(*,/(/(,   . ((  ./#(.   \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m     *,"
            "(.       (##(####(######,# ##,#    /#/.    \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m       ,"
            "(**  *,*.  #    . ####(  /###     ,       "
            "\033[1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m       "
            "**,//   *.*****,,**##,/*,**,*   /#*        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "/(#(      **,,,,*,,,***  .*/#/#/        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            " **(/.  ,   .**///*   ((. /             \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "   .*.#/##(#(/***.,/###//               \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "         ,.   ,.(#,                     "
            "\033[1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")
        print(
            "\033[1;30;40m@\033[1;32;42m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;47m          "
            "                                        \033["
            "1;31;41m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\033[1;30;40m")

    def printTrophy(self) :
        print("  .__.")
        print(" (|  |)")
        print("  (  )")
        print("  _)(_")
        print("\nTrophy or Frog: You Decide!")

    def printScoreboard(self):
        print("Here's a list of everyone's life count")
        line1 = "| Player: | "
        line2 = "|         | "
        line3 = "-----------"
        line4 = "| Lives:  | "
        line5 = "|         | "
        for i in range(0, self.numPlayers):
            line1 = line1 + str((i + 1)) + " | "
            line2 = line2 + "  | "
            line3 = line3 + "----"
            line4 = line4 + str(self.livesList[i]) + " | "
            line5 = line5 + "  | "
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)

    def setupGame(self):
        self.playerList = [0] * self.numPlayers
        for i in range(0, self.numPlayers):
            self.playerList[i] = i + 1
        self.rankList = [22] * self.numPlayers
        self.livesList = [6] * self.numPlayers
        self.rollList = [0] * (self.numPlayers * 2)
        self.playRound()

    def rollRanker(self, a1, a2):
        if a1 < a2:
            placeHolder = a1
            a1 = a2
            a2 = placeHolder
        if a1 == 2 and a2 == 1:
            return 1
        elif a1 == 6 and a2 == 6:
            return 2
        elif a1 == 5 and a2 == 5:
            return 3
        elif a1 == 4 and a2 == 4:
            return 4
        elif a1 == 3 and a2 == 3:
            return 5
        elif a1 == 2 and a2 == 2:
            return 6
        elif a1 == 1 and a2 == 1:
            return 7
        elif a1 == 6 and a2 == 5:
            return 8
        elif a1 == 6 and a2 == 4:
            return 9
        elif a1 == 6 and a2 == 3:
            return 10
        elif a1 == 6 and a2 == 2:
            return 11
        elif a1 == 6 and a2 == 1:
            return 12
        elif a1 == 5 and a2 == 4:
            return 13
        elif a1 == 5 and a2 == 3:
            return 14
        elif a1 == 5 and a2 == 2:
            return 15
        elif a1 == 5 and a2 == 1:
            return 16
        elif a1 == 4 and a2 == 3:
            return 17
        elif a1 == 4 and a2 == 2:
            return 18
        elif a1 == 4 and a2 == 1:
            return 19
        elif a1 == 3 and a2 == 2:
            return 20
        elif a1 == 3 and a2 == 1:
            return 21

    def roundOver(self):
        roundResponse = str(input("Thanks for playing! To play again press Y, otherwise press N\n"))
        if roundResponse == "Y":
            self.newGame()
        elif roundResponse == "N":
            print("Okay, thanks for playing!")
        else:
            print("Please answer correctly")
            self.roundOver()

    def playRound(self):
        mexicoRound = False
        print("Rolling Dice... ")
        print("Results: ")
        loserList = [0]
        lowPlayerRank = 0
        livePlayers = 0
        for i in self.playerList:
            if i != 0:
                livePlayers = livePlayers + 1
                self.dice1.roll()
                ROLLN1 = self.dice1.faceValue()
                self.dice1.roll()
                ROLLN2 = self.dice1.faceValue()
                print("Player " + str(i) + " rolled a " + str(ROLLN1) + " and a " + str(ROLLN2))
                ACTIVERANK = self.rollRanker(ROLLN1, ROLLN2)
                if ACTIVERANK == 1:
                    print("Player " + str(i) + " threw Mexico!")
                    mexicoRound = True
                    self.printMexicoFlag()
                if lowPlayerRank < ACTIVERANK:
                    lowPlayerRank = ACTIVERANK
                    loserList = [i]
                elif lowPlayerRank == ACTIVERANK:
                    loserList.append(i)
                self.continuePrompt()
        for loser in loserList:
            print("Player " + str(loser) + " is a big loser")
            if mexicoRound:
                self.livesList[loser - 1] = self.livesList[loser - 1] - 2
                print("Player " + str(loser) + " lost 2 life because Mexico was thrown this round")
            else:
                self.livesList[loser - 1] = self.livesList[loser - 1] - 1
                print("Player " + str(loser) + " lost 1 life")
            if self.livesList[loser - 1] < 1:
                print("Player " + str(loser) + " died! \nOnly " + str(self.numPlayers - 1) + " left!")
                self.playerList[loser - 1] = 0
                livePlayers = livePlayers - 1
        if livePlayers == 1:
            for winner in self.playerList:
                if winner != 0:
                    print("Player " + str(winner) + " won!!!")
                    self.printTrophy()
                    self.roundOver()
        elif livePlayers < 1:
            print("No winners today! It's a dead game!")
            self.roundOver()
        elif livePlayers > 1:
            self.printScoreboard()
            print("Ready for the next round?")
            self.continuePrompt()
            self.playRound()


game1 = Game()
game1.newGame()
exit()
