from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        # todo
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        self.hit(c1, c2)
        self.hit(c2, c1)
        if c1.health <= 0 and c2.health > 0:
            return 1
        elif c1.health > 0 and c2.health <= 0:
            return 0
        else:
            return -1

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    # todo
    def hit(self, attacker, defender):
        if attacker.attack >= defender.health:
            defender.health = 0

class PermanentDamageCardGame(CardGame):
    # todo
    def hit(self, attacker, defender):
        defender.health -= attacker.attack


c1 = Creature(1, 2)
c2 = Creature(1, 2)
game = TemporaryDamageCardGame([c1, c2])
print(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')
print(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')

c1 = Creature(1, 1)
c2 = Creature(2, 2)
game = TemporaryDamageCardGame([c1, c2])
print(1, game.combat(0, 1))

c1 = Creature(2, 1)
c2 = Creature(2, 2)
game = TemporaryDamageCardGame([c1, c2])
print(-1, game.combat(0, 1))

c1 = Creature(1, 2)
c2 = Creature(1, 3)
game = PermanentDamageCardGame([c1, c2])
print(-1, game.combat(0, 1), 'Nobody should win this battle.')
print(1, c1.health)
print(2, c2.health)
print(1, game.combat(0, 1), 'Creature at index 1 should win this')
