class Swarm(list):
    def __call__(self, *args, **kwds):
        attack = 0
        for item in self:
            attack += item(*args, **kwds)
        return attack

class Game:
    def __init__(self):
        # todo
        self.swarm = Swarm()


class Rat:
    def __init__(self, game):
        self.game = game
        self._attack = 1
        # todo
        self.game.swarm.append(self.contribute_to_attack)

    def contribute_to_attack(self):
        return self._attack

    @property
    def attack(self):
        return self.game.swarm()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.game.swarm.remove(self.contribute_to_attack)



game = Game()
rat = Rat(game)
print(1, rat.attack)

game = Game()
rat = Rat(game)
rat2 = Rat(game)
print(2, rat.attack)
print(2, rat2.attack)

game = Game()
rat = Rat(game)
print(1, rat.attack)

rat2 = Rat(game)
print(2, rat.attack)
print(2, rat2.attack)

with Rat(game) as rat3:
    print(3, rat.attack)
    print(3, rat2.attack)
    print(3, rat3.attack)

print(2, rat.attack)
print(2, rat2.attack)