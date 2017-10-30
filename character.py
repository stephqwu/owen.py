
class Character(object):
    def __init__(self, items, coins, location, pos):
        self.items = items or []
        self.coins = coins or 0
        self.location = location
        self.pos = pos
    def __iadd__(self, right):
        if type(right) is int:
            self.coins += right
        elif type(right) is str:
            if right: self.items.append(right)
        elif type(right) is list:
            for item in right:
                self += item
        else:
            return NotImplemented
        return self
    def __isub__(self, right):
        if type(right) is int:
            self.coins = max(self.coins - right, 0)
        elif type(right) is str:
            if right in self.items: self.items.remove(right)
        elif type(right) is list:
            for item in right:
                self -= item
        else:
            return NotImplemented
        return self
    def __matmul__(self, right):
        self.pos = (self.pos[0] + right[0], self.pos[1] + right[1])
        return self
    def __contains__(self, key):
        if type(key) is int:
            return key <= self.coins
        elif type(key) is str:
            return key in self.items
        elif type(key) is list:
            return all([item in self for item in key])
        else:
            return NotImplemented
    def __str__(self):
        return "coins: %s\nitems: %s" % (int(self.coins), ", ".join(self.items))
    def current(self):
        return self.location[self.pos]
    def do(self, action):
            if action == "map":
                print(self.location)
            elif action == "quit":
                raise KeyboardInterrupt 
            else:
                self.current().do(action, self)

