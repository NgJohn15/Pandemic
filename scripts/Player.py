from Role import Role


class Player:
    def __init__(self, role: Role):
        self.role = role
        self.actions = 4
        self.hand = []
        self.location = "Atlanta"
    
    def action(self):
        pass