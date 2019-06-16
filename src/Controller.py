# Controller.py
#
# For TicTacToe

from View import View
from Model import Model

class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model(self.view)
        self.player = ""

    def play(self):
        while True:
            self.playAGame()

            # ask if user wants to play another game
            # if no, break

    def playAGame(self):
        self.view.reset()
        self.player = "X"
        # update message in View to say it's X's turn
        self.view.startText("X\'s turn0")
        
        while True:
            # get click/cellNum
            # loop until have vaild cellNum
                # valid: 0 >= cellNum <= 8 AND v.model.isEmpty(cellNum) returns True 
            # provide message if click was not in valid cell
            # self.model.turn(cellNum, self.player) - model updates data and tells you to draw player
            # answer = self.model.isDone() - return "X" or "O" or "Draw" or "Continue"
            # if answer is "X" or "O"
                # self.view.startText("winner is" answer)
                # break
            # if answer is "draw"
                # self.view.startText("Game was a draw")
                # break
            
            # switches to other player
            # if self.player == "X":
                # self.player = "O"
            # else:
                # self.player = "X"
            # self.view.startText(self.player + "\s turn") 

def ControllerTest():
    c = Controller()

    input()

'''
def play():
    done = false
    while not done:
        playAGame():
		
        do you want to play again?
        if yes done = false, if no done = true
		
def playAGame():
    initializeDisplay()
	
    done = false
    player = player1
    output player message ("X's turn" or "O's turn")
    while not done:
        player takes turn
        is there a winner
            if yes, done = true
            output winner message
        can play continue
            if no, done = true
            output draw message
        player = next player
        output player message 	
'''

if __name__ == "__main__":
    ControllerTest()
