DIRECTIONS = {"w": (-1, 0), "d":(0,1), "s":(1,0), "a":(0,-1)}
COMPASS = {"north":"w", "east":"d", "south":"s", "west":"a"}

class Room(object):
    def __init__(self, name, desc, stuff, items, north, east, south, west, use={}):
        self.name = name
        self.desc = desc
        self.stuff = stuff or {} 
        self.items = items or []
        self.w = north and "north"
        self.d = east and "east"
        self.s = south and "south"
        self.a = west and "west"
        self.use = use
    def __contains__(self, key):
        return key in self.items
    def __str__(self):
        doors = "You can go " + (", ".join(filter(lambda x: bool(x), [self.w, self.d, self.s, self.a])) or ["nowhere"] ) + "."
        return "%s:\n\t%s\n\t%s" % \
               (self.name, self.desc, doors)
    def unlock(self, direction):
        setattr(self, COMPASS[direction], direction)
    def update(self, field, value):
        setattr(self, field, value)
    def remove(self, item, player):
        player -= item
    def do(self, action, player):
        if action in DIRECTIONS:
            player @= (getattr(player.current(), action, None) and DIRECTIONS.get(action)) or (0,0)
        elif action.startswith("look "):
            print(self.stuff.get(action.lstrip("look ")) or "???")
        elif action == "search":
            for item in self.items:
                player += item
            setattr(self, "items", [])
        elif action.startswith("use ") and self.use.get(action.lstrip("use "), None):
            item = action.lstrip("use ")
            for f in self.use[item]:
                getattr(self, f[0])(*(f[1:]))
        else:
            print("???")


class Shop(Room):
    def __init__(self, name, desc, selling, north, east, south, west, use={}):
        super(Shop, self).__init__(name, desc, 0, 0, north, east, south, west, use)
        self.selling = selling
    def __getitem__(self, key):
        return self.selling.get(key, None)
    def __isub__(self, right):
        if right in self.selling: 
            self.selling.pop(right)
        return self
    def __str__(self):
        selling = "There is " + (", ".join([key + " (" + str(self.selling[key]) + " coins)" for key in self.selling]) or "nothing") + " for sale."
        doors = "You can go " + (", ".join(filter(lambda x: bool(x), [self.w, self.d, self.s, self.a]) or ["nowhere"]) ) + "."
        return "%s:\n\t%s\n\t%s\n\t%s" % (self.name, self.desc, selling, doors)
    def __contains__(self, key):
        if type(key) is str:
            return key in self.selling
        else:
            return NotImplemented
    def do(self, action, character):
        if action.lstrip("buy ") in self and self[action.lstrip("buy ")] in character:
            character += action.lstrip("buy ")
            character -= self[action.lstrip("buy ")]
            self -= action.lstrip("buy ")
        else:
            super(Shop, self).do(action, character)


class PortalRoom(Room):
    def __init__(self, name, desc, stuff, items, key, portal,  north, east, south, west, use={}):
        super(PortalRoom, self).__init__(name, desc, stuff, items,  north, east, south, west, use)
        self.key = key
        self.portal = portal or {}
    def do(self, action, character):
        if action.startswith("enter ") and self.portal.get(action.lstrip("enter "), None) and self.key in character:
            character.location = self.portal.get(action.lstrip("enter "), None)
        else:
            super(PortalRoom, self).do(action, character)   


class PortalShop(Shop):
    def __init__(self, name, desc, selling, key, portal,  north, east, south, west, use={}):
        super(PortalShop, self).__init__(name, desc, selling,  north, east, south, west, use)
        self.key = key
        self.portal = portal or {}
    def do(self, action, character):
        if action.startswith("enter ") and self.portal.get(action.lstrip("enter "), None) and self.key in character:
            character.location = self.portal.get(action.lstrip("enter "), None)
        else:
            super(PortalShop, self).do(action, character)


class NPCRoom(Room):
    def __init__(self, name, desc, stuff, items, speech, trade,  north, east, south, west, use={}):
        super(NPCRoom, self).__init__(name, desc, stuff, items, north, east, south, west, use)
        self.speech = speech
        self.trade = trade
    def __getitem__(self, key):
        return self.trade.get(key, None)
    def __isub__(self, right):
        if right in self.trade: 
            self.trade.pop(right)
        return self
    def __contains__(self, key):
        if type(key) is str:
            return key in self.trade
        else:
            return NotImplemented
    def do(self, action, character):
        if action == "trade" and self.trade[1] in character:
            character += self.trade[0] 
            character -= self.trade[1]
            self.trade = []
        elif action == "talk":
            print(self.speech[int(bool(self.trade))-1])
        else:
            super(NPCRoom, self).do(action, character)


class EldritchRoom(Room):
    def __init__(self, name, desc, stuff, items,  north, east, south, west, use={}):
        super(EldritchRoom, self).__init__(name, desc, stuff, items,  north, east, south, west, use)
    def __getitem__(self, key):
        return self
    def __str__(self):
            doors = "You can go north, east, south, west."
            return "%s:\n\t%s\n\t%s" % \
                   (self.name, self.desc, doors)
    def do(self, action, character):
        if action in DIRECTIONS:
            character.location = getattr(self, action)
        else:
            super(EldritchRoom, self).do(action, character)
