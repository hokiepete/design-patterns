from abc import ABC
import math

class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo
        return b*b - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # todo
        disc = b*b - 4*a*c
        if disc < 0:
            return float('nan')
        else:
            return disc


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        # todo
        print(a,b,c)
        disc = complex(
            self.strategy.calculate_discriminant(a, b, c),
            0
        )
        ans1 = (-b + disc**(1/2))/(2*a)
        ans2 = (-b - disc**(1/2))/(2*a)
        return ans1, ans2
    

strategy = OrdinaryDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 10, 16)
print(complex(-2, 0), results[0])
print(complex(-8, 0), results[1])

strategy = RealDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 10, 16)
print(complex(-2, 0), results[0])
print(complex(-8, 0), results[1])

strategy = OrdinaryDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 4, 5)
print(complex(-2, 1), results[0])
print(complex(-2, -1), results[1])

strategy = RealDiscriminantStrategy()
solver = QuadraticEquationSolver(strategy)
results = solver.solve(1, 4, 5)
print(True, math.isnan(results[0].real))
print(True, math.isnan(results[1].real))
print(True, math.isnan(results[0].imag))
print(True, math.isnan(results[1].imag))