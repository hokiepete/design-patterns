class Token:
    def __init__(self, idx, capitalize):
        self.idx = idx
        self.capitalize = capitalize

class Sentence:
    words = []
    def __init__(self, plain_text):
        # todo
        self.tokens = []
        for word in plain_text.split(" "):
            if word in Sentence.words:
                self.tokens.append(
                    Token(Sentence.words.index(word), False)
                )
            else:
                Sentence.words.append(word)
                self.tokens.append(
                    Token(len(Sentence.words)-1, False)
                )
    
    def __getitem__(self, item):
        return self.tokens[item]
        
    def __str__(self):
        results = []
        for token in self.tokens:
            word = Sentence.words[token.idx]
            results.append(
                word.upper() if token.capitalize else word
            )
        return " ".join(results)
    
s = Sentence('alpha beta gamma')
s[1].capitalize = True
print(str(s), 'alpha BETA gamma')