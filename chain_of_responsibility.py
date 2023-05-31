from abc import ABC


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self): pass

    @property
    def defense(self): pass

    @property
    def query(self): pass


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        # todo
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = Query(self.initial_defense, 'attack')
        for creature in self.game.creatures:
            creature.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.initial_defense, 'defense')
        for creature in self.game.creatures:
            creature.query(self, q)
        return q.value

    def query(self, caller, q):
        if self is not caller and q.query == 'defense':
            q.value += 1


class GoblinKing(Goblin):
    def __init__(self, game, attack=3, defense=3):
        # todo
        super().__init__(game, attack, defense)

    def query(self, caller, q):
        if self is not caller and q.query == 'attack':
            q.value += 1
        else:
            super().query(caller, q)


class Query:
    def __init__(self, inital_value, query):
        self.value = inital_value
        self.query = query


class Game:
    def __init__(self):
        self.creatures = []

game = Game()
goblin = Goblin(game)
game.creatures.append(goblin)

print(1, goblin.attack)
print(1, goblin.defense)

goblin2 = Goblin(game)
game.creatures.append(goblin2)

print(1, goblin.attack)
print(2, goblin.defense)

goblin3 = GoblinKing(game)
game.creatures.append(goblin3)

print(2, goblin.attack)
print(3, goblin.defense)