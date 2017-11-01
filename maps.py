class Map(object):
    def __init__(self, height, width, start=(0,0)):
        self.map = [[None for j in range(width)] for i in range(height)] 
    def __getitem__(self, key):
        return self.map[key[0]][key[1]]
    def __setitem__(self, key, val):
        self.map[key[0]][key[1]] = val
    def __str__(self):
        result = ""
        for row in self.map:
            for entry in row:
                result += "%s| " % ((entry.name + 11*" ")[0:11] if entry else 11*" ")
            result += "\n"
        return result

class EldritchMap(Map):
    def __init__(self, start=0):
        self.map = []
        self.current = 0
    def __getitem__(self, key):
        return self.map[self.current]
    def __setitem__(self, key, val):
        self.map.append(val)
    def __str__(self):
        return "???"
