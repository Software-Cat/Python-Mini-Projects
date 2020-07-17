class Player:
    def __init__(self, hand):
        self.hand = hand
    
    def turn(self):
        pass

class HumanPlayer(Player):
    def __init__(self, hand):
        Player.__init__(self, hand)
    
    def turn(self):
        pass

class AIPlayer(Player):
    def __init__(self, hand):
        Player.__init__(self, hand)
    
    def turn(self):
        pass