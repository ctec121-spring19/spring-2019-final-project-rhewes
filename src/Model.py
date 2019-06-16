# Model.py
#
# For TicTacToe

from View import View

class Model:

    def __init__(self, View):
        self.view = View
        self.cellContents = ['e','e','e','e','e','e','e','e','e']
        
    def reset(self):
        self.cellContents = ['e','e','e','e','e','e','e','e','e']

    def isEmpty(self, cellNum):
        
        if self.cellContents[i] == 'e':
            return True
        return False

def ModelTest():
    # delete and enter your code here
    pass

if __name__ == "__main__":
    ModelTest()
