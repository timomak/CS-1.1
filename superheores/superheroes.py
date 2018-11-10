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
            damage += ability.attack()
            print("{} is adding {} damage".format(self.name, damage))
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

    def attack(self):
        '''
        Return a random attack value
        between 0 and attackStrenght.
        '''
        damage = randint(0, self.attackStrenght)
        print("ability attack damage: ",damage, " by ", self.name)
        return damage

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between one half to the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        damage = randint((self.attackStrenght / 2), self.attackStrenght)
        print("Weapon damage",damage)
        return damage

class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        '''Add Hero object to heroes list.'''
        self.heroes.append(Hero)
        pass

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if hero == name:
                self.heroes.remove(hero)
        pass

    def view_all_heroes(self):
        '''Print out all heroes to the console.'''
        for hero in self.heroes:
            print("team member: ",hero.name)
        pass

if __name__ == "__main__":

    # hero = Hero("Wonder Woman")
    # ability = Ability("Divine Speed", 20)
    # hero.add_ability(ability)
    # new_ability = Ability("Super Human Strength", 30)
    #
    # hero.add_ability(new_ability)
    #
    #
    # hero2 = Hero("Jodie Foster")
    #
    # axe = Weapon("axe", 80)
    # hero2.add_ability(axe)
    #
    # ability2 = Ability("Science", 40)
    # hero2.add_ability(ability2)
    #
    #
    #
    # hero.fight(hero2)

    batman = Hero("Batman")
    superman = Hero("Superman")
    justiceLeague = Team("Justice League")

    justiceLeague.add_hero(batman)
    justiceLeague.add_hero(superman)

    justiceLeague.view_all_heroes()
    justiceLeague.remove_hero(superman)
    justiceLeague.view_all_heroes()
