import items

class Room:
    def __init__(self,possibleDirections,name,index,items, entryDescription,specificDescription,specialQual,hasBattle=False):

        #possible directions notated like {"north": (index),"south": (index)} and so on
        self.possibleDirections = possibleDirections;
        self.name = name;
        self.index = index;
        self.items = items;
        #perhaps keep the "commands" attribute for later for more unique room encounters, but for now the text parser already handles most commands
        #self.commands = commands;
        self.entryDescription = entryDescription;
        self.specificDescription = specificDescription;
        self.specialQual = specialQual;
        self.hasBattle = hasBattle;

    def get_room_index(self):
        return self.index;

    def findItem(self,name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i;

                                                                                #N
                                                                           #W        #E            
                                                                                #S
rooms_dict = {
    #spawn+interactTile    
    1: Room({"north":2},"spawnTemple",1,[items.rock,items.rustySword,
                                    #"Dagger","Wooden Staff","Backpack",
                                    items.potion],"As your eyes begin to open and your senses come about you, you find yourself in an abandoned stone Temple. \n",
                 "Its walls cracked and its ceilings collapsed in many places, the once-majestic structure now lies in ruin. \n"
                 "It's as if time has stood still in this abandoned temple, as now the scent of decay and mustiness permeates the air. \n" 
                 "The only source of light shimmers down as weak rays of sunshine filtering through the broken ceiling, casting a dusty glow on the crumbling stone pillars. \n"
                 "It is hard to imagine a place, as grand as this, is all but helpless against the elements. \n",
                 'spawnPoint'),
    #genericTile
    2: Room({"south":1,"west":3,"east":65},"forest",2,[items.rock,
                                                       #"Rock","Log","Weeds"
                                                       ],'You find an opening.',
                        'Unfortunately a bit unremarkable... \n but there is a bit of rubble and greenery about.',None),
                 
    #interactTile
    65: Room({"east":66,"west":2},"riverCamp",65,[items.rock,
                                               #"Bottle","Note","Vase","Tent"
                                               ],'You are near a river and come across what seems to be the remnants of a campsite',
                          "As you look around more closely..."
                          "There is a weather-worn tent with an extinguished camp fire nearby. "
                          "The area is quiet and still, quite still in fact, and still quite quiet, still things could be quite worse...",None),
    #interactTile
    3: Room({"east":2,"west":4},"preBattle",3,[items.bloodiedBackpack,items.rock

                                                ],"You enter into a clearing and hear loud shouting to the west.",
                            "When you look around the area, you notice that there are *gulp* quite a few blood stains about\n."
                            "In the foliage, you spot a bloodied backpack and momentarily mourn the loss of a fellow traveller.\n"
                            "Of course, due to the western noise, you quickly get over it.\n"
                            "There is also a carving on a tree nearby."),

    #battleTile
    4: Room({"north":5,"east":2},"battleBloodied",4,[],
                                        "Oh GOD! There are enemies here!","You really know how to be urgent huh?","battle",hasBattle=True),

    #genericTile
    #66:Room(),


    #67:Room(),
};