# View.py
# 
# For TicTacToe

from graphics import *

class View:

    def __init__(self):
        self.win = GraphWin("Tic Tac Toe",300,400)
        self.win.setCoords(0, 0, 3, 4)
        
        # Horizontal
        Line(Point(0, 1), Point(3, 1)).draw(self.win)
        Line(Point(0, 2), Point(3, 2)).draw(self.win)
        Line(Point(0, 3), Point(3, 3)).draw(self.win)
        
        # Vertical
        Line(Point(1, 0), Point(1, 3)).draw(self.win)
        Line(Point(2, 0), Point(2, 3)).draw(self.win)

    def getClick():
        pt = self.win.getMouse()

        if pt.getX() <= 3 and
           pt.getY() <= 3:
           cellNum = int(getX) * 3 + int(getY)
        else:
            cellNum = -1 

def ViewTest():
    v = View()

    input()
    
if __name__ == "__main__":
    ViewTest()
