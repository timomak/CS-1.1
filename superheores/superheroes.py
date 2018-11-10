from random import randint
import random

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

        self.armors = list()
        self.deaths = 0
        self.kills = 0
        self.defence = 0


    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        pass

    def add_armor(self, armor):
        ''' Add ability to abilities list '''
        self.armors.append(armor)
        self.defence = 0
        for armor in self.armors:
            self.defence += armor.block()
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
        if self.defence > 0:
            print("{} has armor".format(self.name))
            self.defence -= damage
            if self.defence < 0:
                print("Pierced throught block. Current defence: ", self.defence)
                pierceDamage = self.defence * -1
                self.current_health -= pierceDamage
        else:
            self.current_health -= damage
            print("{} has no armor".format(self.name))
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
            self.deaths += 1
            opponent.kills += 1
            print("{} died".format(self.name))


        if opponent.is_alive() == False:
            opponent.deaths += 1
            self.kills += 1
            print("{} died. He has {} deaths.".format(opponent.name, opponent.deaths))


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

    def attack(self, other_team):
        '''
        This function should randomly select a living hero from each team and have them fight until one or both teams have no surviving heroes.

        Hint: Use the fight method in the Hero class.
        '''
        randomTeamHero = random.choice(self.heroes)
        randomEnemyTeamHero = random.choice(other_team.heroes)
        print("{} against {}".format(randomTeamHero.name, randomEnemyTeamHero.name))

        pass

    def revive_heroes(self, health=100):
        '''
        This method should reset all heroes health to their
        original starting value.
        '''
        pass

    def stats(self):
        '''
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the console.
        '''
        pass

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        defence = randint(0, self.max_block)
        return defence

if __name__ == "__main__":
    batman = Hero("Batman")
    # batsuit = Armor("Bat Suit", 1)
    # batman.add_armor(batsuit)



    superman = Hero("Superman")
    # superStreanght = Ability("Super Streanght", 100)
    # superman.add_ability(superStreanght)

    justiceLeague = Team("League")
    evilLeague = Team("Evil League")

    justiceLeague.add_hero(batman)
    evilLeague.add_hero(superman)
    justiceLeague.attack(evilLeague)
