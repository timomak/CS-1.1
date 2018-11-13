class Tiger(object):
    def __init__(self, name, age=0, food="hot dog"):
        self.name = name
        self.age = age
        self.food = food
    def __str__(self):
        return "{0} is {1} year old. {0} eats {2}".format(self.name, self.age, self.food)


tony = Tiger("Tony", 66)
print(tony)

hobbes = Tiger("Hobbes",food="fish")
print(hobbes)
