from spellchecker import SpellChecker
from Levenshtein import distance


class Spell:
    def __init__(self, custom=None):
        self.s = SpellChecker()
        if custom:
            for w in custom:
                self.s.word_frequency.load_words([w])

    def identify(self, t):
        w = t.split()
        m = self.s.unknown(w)
        return m

    def suggest(self, m):
        d = {}
        for w in m:
            c = self.s.candidates(w)
            if c:
                b = min(c, key=lambda x: distance(w, x))
                d[w] = b
        return d

    def autocorrect(self, t):
        m = self.identify(t)
        s = self.suggest(m)
        c = t
        for w, r in s.items():
            c = c.replace(w, r)
        return c


c = [""]
s = Spell(c)

while True:
    i = input("Enter text (or 'quit' to exit): ")
    if i.lower() == 'quit':
        break
    r = s.autocorrect(i)
    print("Corrected Text:", r)
