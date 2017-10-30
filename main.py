from maps import Map
from rooms import Room, Shop, PortalShop, PortalRoom, NPCRoom, EldritchRoom
from character import Character

m = Map(10, 10, (2,1))
heaven = Map(10, 10, (1, 5))
hell = Map(10, 10, (3,2))

start = (6,0) #(2,1)
player = Character([], 0, m, start) 

heaven[1,5] = PortalShop("Heavenly Shop I", "A white, pure shop with items that never run out of stock.", {"holy water": ["water", 10]}, 0, {"light":m}, 0, 0, 0, 0) # water and 10 coins
heaven[5,2] = Room("Heaven I", "A white room with biblical verses written in gold on the walls.", {}, ["holy water"], 0, 0, 0, 0)

hell[3,2] = PortalShop("Hellish Shop I", "A fiery, dimly lit shop. Blood covers the walls.", \
    {"satanic bible":["paper","blood", 20], "hell key":["key", 7]}, 0, {"chasm":m}, 0, 0, 0, 0)
hell[5, -1] = Room("Hell I", "A dimly lit room. The floor is covered with blood.", {}, [], 0, 0, 0, 1)
hell[5, -2] = Room("Hell II", "A pentagram covers the floor.", {}, [], 0, 1, 0, 0)

m[0, 3] = Room("Dark Room", "A dark room.", {}, [], 0, 0, 1, 0)
m[1,2] = Shop("Shop I", "A quaint little shop.", {"orange carrot":5, "goat":35}, 0, 0, 1, 0)
m[1, 3] = Room("Hallway III", "A thin narrow room with scribbles on the walls.", \
    {"scribbles": 'the only thing you can make out is "beware the empty room" and "I know the code! I have scribbled it on the walls!"'}, \
    ["glasses"], 1, 1, 0, 0)
m[1, 4] = Room("Hall II", "A large room with scribbles on the walls.", {"scribbles": "The walls read: I have found the code! I am not insane!"}, \
    [], 0, 1, 1, 1)
m[1, 5] = PortalRoom("Cathedral I", "You are in what appears to be the interior of a church. There are rows of seats, a large crucifix at the front of the " + \
    "room, and a beam of heavenly light in the center.", {"seats": "The seats appear neglected from years of disuse", \
    "crucifix": "Upon closer inspection, you find the crucifix has been disfigured by vandals.", \
    "beam of light": "A beam of holy light, emanating from nowhere in particular."}, [], "bible", {"light": heaven}, 0, 1, 1, 1)
m[1, 6] = Room("Cathedral II", "You are in a side room of a church.", {}, [5, "pen"], 0, 0, 1, 1)
m[2,0] = Room("Hole in the Wall", "A small room hidden behind a fake wall.", {}, ["key"], 0, 1, 0, 0)
m[2,1] = Room("Start", "A sparse room with a door. There is a crack on the west wall.", {"crack": \
    "Maybe if you had a hammer you could try breaking the wall."}, [], 0, 1, 0, 0, \
    use={"hammer":[["unlock", "west"],["remove", "hammer", player],["update", "desc", "A sparse room with a door. There is a hole in the west wall."]]})
m[2,2] = Room("Hall I", "A room with doors in every direction.", {}, [15], 1, 1, 1, 1)
m[2,3] = NPCRoom("Hallway I", "A room with a man in the centre. There is a locked door to the east.", {}, [], \
    ['"I will give you a hammer if you give me an orange carrot."', '"Beware of empty rooms."'], ["hammer", "orange carrot"], 0, 0, 0, 1, \
    use={"key":[["unlock", "east"], ["remove", "key", player], ["update", "desc", "A room with a man in the centre."]]})
m[2,4] = Room("Hallway II", "A narrow hallway. The wall are covered in scribbles, and there is a pentagram in what you hope is red paint.", \
    {"scribbles": "You count 2497 scribbles.", "pentagram":"I don't think that's paint..."}, [12, "red paint"], 1, 0, 0, 1)
m[2, 5] = Room("Fountain Room", "A room with a fountain in the centre.", {"foutain": "The fountain is full of water."}, ["water"], 1, 1, 1, 0)
m[2,6] = NPCRoom("Cathedral III", "A small room with a man in the centre of it.", {}, [], \
    ['"I will write you a bible if you give me 10 coins, paper, and a pen."', '"Only those of faith may enter Heaven."'], \
    ["bible", [10, "pen", "paper"]], 1, 0, 1, 1)
m[3,0] = Room("Pedestal Room III", "A small room with a pedestal in the centre.", \
    {"pedestal": "a stone pedestal with nothing on it, occupying the centre of the room."}, \
    ["small rock"], 0, 0, 1, 1)
m[3,1] = Room("Pedestal Room IV", "A small room with a pedestal in the centre.", \
    {"pedestal": "a stone pedestal with nothing on it, occupying the centre of the room."}, \
    [6], 0, 0, 1, 1)
use3_2 = {"red paint":[["remove", "red paint", player],\
                       ["update", "desc", "An empty room with a pentagram painted on the floor in red paint."],\
                       ["update", "use", {"goat":[["update", "key", True], \
                                                  ["remove", "goat", player], \
                                                  ["update", "desc", "A room with a pentagram on the floor in red paint, an infernal chasm leading to hell."]]}]],\
          "blood":[["remove", "blood", player],\
                   ["update", "desc", "An empty room with a pentagram painted on the floor in blood."],\
                   ["update", "use", {"goat":[["update", "key", True], \
                                              ["remove", "goat", player], \
                                              ["update", "desc", "A room with a pentagram on the floor in blood, an infernal chasm leading to hell."]]}]] \
         }
m[3,2] = PortalRoom('"Empty" Room', "An empty room.", {}, [], None, {"chasm":hell}, 1, 0, 0, 0, \
    use= use3_2)
m[3,3] = NPCRoom("Hallway III.V", "A hallway with a bearded man in it.", {}, [10], \
    ['"I will trade you my beard for an apple."', '"The password is obvious."'], ["beard", "apple"], 0, 1, 1, 0)
m[3,4] = Room("Hidden Room I", "A secret room hidden behind a clock. There is an unholy creature guarding the west door.", \
    {"creature":"You can't get past the creature, it's too tough."}, [], 0, 1, 0, 0, \
    use={"bible":[["unlock", "west"], ["remove", "bible", player], ["update", "desc", "A secret room hidden behind a clock."]]}) 
m[3, 5] = Room("Clock Room", "A large room with a giant clock covering a large portion of the west wall.", \
    {"clock": "There seems to be something behind the clock."}, [23, "paper"], 1, 1, 0, 1)
m[3, 6] = Room("Hallway IV", "A hallway with writing on the wall.", \
    {"writing": 'The writing on the wall reads "Hannah 5, Mary 17, Solomon 45". It appears to be the score of some sort of game.'}, \
    [], 1, 0, 0, 1)
m[4,0] = Room("Pedestal Room II", "A small room with a pedestal in the centre.", \
    {"pedestal": "a stone pedestal with nothing on it, occupying the centre of the room."}, \
    [], 1, 1, 0, 0)
m[4,1] = Room("Pedestal Room I", "A small room with a pedestal in the centre.", \
    {"pedestal": "a stone pedestal with nothing on it, occupying the centre of the room."}, \
    [], 1, 1, 0, 1)
m[4,2] = Room("Mirror Room", "A large room with a pedestal in the centre and a mirror on the north wall.", \
    {"pedestal": "A large stone pedestal with nothing on it, occupying the centre of the room.", "mirror": "You would look better with a beard."}, \
    ["small rock"], 0, 1, 0, 1)
m[4,3] = NPCRoom("Hall III", "A room with doors in every direction, and a bearded man in the centre. The south door is locked.", {}, [], \
    ['"I WILL GIVE YOU THE KEY IF YOU GET ME A BEARD!"', '"WITH MY NEW BEARD I AM TWICE AS STRONG!"'], ["key", "beard"], 1, 1, 0, 1, \
    use={"key":[["unlock", "south"], ["remove", "key", player], ["update", "desc", "A room with doors in every direction, and a bearded man in the centre."]]})
m[4,4] = Shop("Shop II", "A filthy, overpriced shop.", {"apple":5, "match":7, "small rock":5}, 0, 0, 0, 1)
m[5,3] = Room("Hallway V", "A small, non-descript hallway.", {}, ["small rock"], 1, 0, 0, 1)
m[5,2] = Room("Chapel", "A small room for praying. There is a beam of heavenly light in the centre of the room.", \
    {"beam of light":"A beam of holy light, emanating from nowhere in particular."}, [], 0, 1, 0, 1)
m[5,1] = Room("Hallway VI", "A narrow hallway, blocked on the west by fire.", {"fire":"If only you had some way of extinguishing the fire..."}, \
    [19], 0, 1, 0, 0, use={"water":[["unlock", "west"], ["update", "desc", "A narrow hallway."], ["remove", "water", player]]})
m[5,0] = Room("Hallway VII", "A narrow hallway with blood spatters covering the walls. The west door is locked.", {"blood":"Hopefully it was just a scrape."}, ["blood"], \
    0, 1, 0, 0, use={"key":[["unlock", "west"], ["remove", "key", player], ["update", "desc", "A narrow hallway with blood spatters covering the walls."]]})
m[5,-1] = Room("Crypt I", "An underground room where bodies are buried. There is an infernal chasm in the centre of the room.", \
    {"chasm":"A fiery hole straight to the depths of hell."}, [], 0, 1, 0, 0)
m[5, -2] = Room("Hidden Room II", "A secret room with no exits, accessible only from hell. There is an infernal chasm in the centre of the room.", \
    {}, ["key"], 0, 0, 0, 0)
m[6, -1] = Room("Rainbow Room I", "A multicolored room.", {}, [], 1, 1, 0, 0)
m[6, 0] = Room("Rainbow Room II", "A multicolored room.", {}, [], 0, 0, 1, 1)


red = EldritchRoom("Red Room", "A red room.", {}, [], None, None, None, None)
orange = EldritchRoom("Orange Room", "An orange room.", {}, [], None, None, None, None)
yellow = EldritchRoom("Yellow Room", "A yellow room.", {}, [], None, None, None, None)
green = EldritchRoom("Green Room", "A green room.", {}, ["Book of Cthulhu"], None, None, None, None)
blue = EldritchRoom("Blue Room", "A blue room.", {}, [], None, None, None, None)
purple = EldritchRoom("Purple Room", "A purple room.", {}, [], None, None, None, None)
red.w = red
red.d = purple
red.s = green
red.a = orange
orange.w = yellow
orange.d = purple
orange.s = red
orange.a = orange
yellow.w = blue
yellow.d = orange
yellow.s = green
yellow.a = yellow
green.w = purple
green.d = blue
green.s = yellow
green.a = red
blue.w = green
blue.d = purple
blue.s = red
blue.a = blue
purple.w = blue
purple.d = red
purple.s = purple
purple.a = green

m[7,0] = red

if __name__ == "__main__":
    print(m)
    while True:
        print(player)
        print(player.current())
        player.do(input(">>> ").strip()) 

