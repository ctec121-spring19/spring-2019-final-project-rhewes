# View.py
# 
# For TicTacToe

from graphics import *

class View:

    def __init__(self):
        self.win = GraphWin("Tic Tac Toe",300,400)
        self.win.setCoords(0, 0, 3, 4)
        self.objList = []
        
        # Horizontal
        Line(Point(0, 1), Point(3, 1)).draw(self.win)
        Line(Point(0, 2), Point(3, 2)).draw(self.win)
        Line(Point(0, 3), Point(3, 3)).draw(self.win)
        
        # Vertical
        Line(Point(1, 0), Point(1, 3)).draw(self.win)
        Line(Point(2, 0), Point(2, 3)).draw(self.win)
    
        # Text box
        self.topText = Text(Point(1.5, 3.5),"")
        self.topText.setStyle("bold")
        self.topText.setSize(18)
        self.topText.draw(self.win)
    
    def getClick(self):
        pt = self.win.getMouse()

        if pt.getX() <= 3 and pt.getY() <= 3:
            cellNum = int(pt.getY()) * 3 + int(pt.getX())
        else:
            cellNum = -1
        return cellNum
    
    # Calculate coordinates from cellNum
    
    def drawO(self, cellNum):
        y = cellNum // 3
        x = cellNum % 3
        center = Point(x + 0.5, y + 0.5)
        c = Circle(center, .3)
        c.draw(self.win)
        self.objList.append(c)
    
    
    def drawX(self,cellNum):
        # draw 2 diagonal lines
        # add both lines to objList
        y = cellNum // 3
        x = cellNum % 3
        center = Point(x + 0.5, y + 0.5)
        x1 = Line((0.5, 1.5),1)
        x2 = Line((0.5, 1.5),1)
        x1.draw(self.win)
        x2.draw(self.win)
        self.objList.append(x1)
        self.objList.append(x2)
        

    def reset(self):
        for obj in self.objList:
            obj.undraw()
        self.objList.clear()
        self.startText.setText("")

    def startText(self, message):
        self.topText.setText(message)

def ViewTest():
    v = View()
    # test setting text
    v.startText("Test")
    # test getClick
    # print(v.getClick())
    
    # test draw O
    for i in range(9):
        # v.drawO(i)
        v.drawX(i)

    input()
    v.reset()
    input()
    
if __name__ == "__main__":
    ViewTest()
