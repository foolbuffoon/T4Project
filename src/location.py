class Location:
    name = ""
    has_monsters = False
    has_items = False
    get = ["placeholder1", "placeholder2"]
    go = ["placeholder3", "placeholder4", "placeholder5"]
    flavor = ""

    def __init__(self):
        self.name = "test"
        self.has_monsters = True
        self.has_items = True
        self.get = ["a location", "another location"]
        self.go = ["a new place", "a different place", "a third place! wowee!"]
        self.flavor = "bitter, with notes of cellulose and TV static"

    def travel(self, go, get):
        return self.name
