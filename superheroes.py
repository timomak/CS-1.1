from random import randint

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()


    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        # print("abilities: ", self.abilities)
        pass

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        damage = 0
        for ability in self.abilities:
            damage += ability.attackAbility()
        print("{} is attacking with attack power of {}".format(self.name, damage))
        return damage

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        self.current_health -= damage
        pass

    def is_alive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        print("fighting!")
        while self.is_alive() == True and opponent.is_alive() == True:
          opponent.take_damage(self.attack())
          self.take_damage(opponent.attack())
          print("{}'s health is: ".format(self.name), self.current_health)
          print("{}'s health is: ".format(opponent.name), opponent.current_health)

        if self.is_alive() == False:
            print("{} died".format(self.name))

        if opponent.is_alive() == False:
            print("{} died".format(opponent.name))


class Ability:
    def __init__(self, name, attackStrenght):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        self.name = name
        self.attackStrenght = attackStrenght

    def attackAbility(self):
        '''
        Return a random attack value
        between 0 and attackStrenght.
        '''
        damage = randint(0, self.attackStrenght)
        print(damage)
        return damage


if __name__ == "__main__":
    hero = Hero("Wonder Woman",1000)
    ability = Ability("Divine Speed", 20)
    hero.add_ability(ability)
    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)


    hero2 = Hero("Jodie Foster", 1000)
    ability2 = Ability("Science", 800)
    hero2.add_ability(ability2)
    hero.fight(hero2)
