SPECIAL_CHAR = set(['+', '-', '(', ')'])
class ExpressionProcessor:
    def __init__(self):
        self.variables = {}
        self.tokens = []

    def calculate(self, expression):
        # todo
        self.tokenize(expression)
        result = self.parse_tokens(self.tokens)

        return result
    
    def tokenize(self, expression):
        for c in expression:
            if c in SPECIAL_CHAR:
                self.tokens.append(c)
            elif len(self.tokens) == 0 or self.tokens[-1] in SPECIAL_CHAR:
                self.tokens.append(c)
            else:
                self.tokens[-1] += c

    def get_subexpression(self, tokens):
        parens = 1
        subexpression = []
        while parens:
            current_token = tokens.pop()
            if current_token == '(':
                parens += 1
            elif current_token == ')':
                parens -= 1
            if parens:
                subexpression.append(current_token)
        return tokens, subexpression

    def cast_to_int(self, value):
        try:
            return int(value)
        except ValueError as e:
            if value in self.variables:
                return self.variables[value]
            else:
                raise e

    def parse_tokens(self, tokens):
        tokens = tokens[::-1]
        be = BinaryExpression()
        while tokens:
            current_token = tokens.pop()
            if current_token == '(':
                tokens, subexpression = self.get_subexpression(tokens)
            elif current_token in SPECIAL_CHAR:
                be.operator = current_token
            else:
                if be.lhs:
                    try:
                        be.rhs = self.cast_to_int(current_token)
                    except ValueError:
                        return 0
                    value = be.value
                    be = BinaryExpression()
                    be.lhs = value
                else:
                    try:
                        be.lhs = self.cast_to_int(current_token)
                    except ValueError:
                        return 0
        return be.lhs


class BinaryExpression:
    def __init__(self) -> None:
        self.lhs = None
        self.operator = None
        self.rhs = None

    @property
    def value(self):
        if self.operator == '+':
            return self.lhs + self.rhs
        else:
            return self.lhs - self.rhs



ep = ExpressionProcessor()
ep.variables['x'] = 5
print(1, ep.calculate('1'))

ep = ExpressionProcessor()
ep.variables['x'] = 5
print(3, ep.calculate('1+2'))

ep = ExpressionProcessor()
ep.variables['x'] = 5
print(6, ep.calculate('1+x'))

ep = ExpressionProcessor()
ep.variables['x'] = 5
print(0, ep.calculate('1+xy'))