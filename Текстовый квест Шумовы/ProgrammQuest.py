class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def player_choice(self, choice):
        choice = int(input())


player = Player(str(input("Введите имя персонажа:")), [])


class Scene:
    def __init__(self, description, options):
        self.description = description
        self.options = options



class Item:
    def __init__(self, title, item_description):
        self.title = title
        self.item_description = item_description
