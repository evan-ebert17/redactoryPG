import playerStats

class Item:
    def __init__(self, name, description, item_type, stat_effects=None,use_message=None,function=None):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.stat_effects = stat_effects if stat_effects is not None else {}
        self.function = function
                                                        #this is just the default, placeholder message
        self.use_message = use_message if use_message is not None else f"You used the {self.name}."

    #this function simply just exists to check IF an item has a function, and if it does, use the function specified.
    def use(self, hero):
        if self.function is not None:
            #passing the hero (player) value here allows the use command to modify the players stats, such as healing from a potion
            self.function(hero)
            print(self.use_message)
        else:
            print(f"You can't use the {self.name}.")

    #defines how the item will be printed when called, example: look rock -> " Rock: "Just an unremarkable rock." ";
    def __str__(self):
        return f"{self.name}: {self.description}";

    def heal(hero):
        hero.stats[4] += 10  # Increase HP by 10
        print(f"{hero.name}'s HP is healed by 10.")

    def unlock(self):
        print("wip");



#create items here

potion = Item("Health Potion", "A potion that restores 10 HP.", None, None,"You drank the health potion.",Item.heal);
key = Item("Red Key", "A red key that might open something.",None,None, None,"You inserted the key.");
rock = Item("Rock","Just an unremarkable rock.",None,None,None,None);
ironHelm = Item("Iron Helmet","An iron helmet with two horns, one of which is broken.",item_type="head", stat_effects={"str":1,"hp":2})
rustySword = Item("Rusty Sword","A sword covered in rust. Sturdy, but it has seen better days.",item_type="weapon",stat_effects={"str":1})
