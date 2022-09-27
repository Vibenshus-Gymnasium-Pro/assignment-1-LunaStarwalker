#Envelope Game

import random

class EnvelopeGame:

    def __init__(self, list):
        if len(list) < 10000:
            print("Please insert more envelopes. (min 10000)")
        else:
            self._envelopes = list
            self._maxEnvelope = 0

    def low_value(self):
        return min(self._envelopes)

    def pick_env(self):

        _currentEnvelopes = []

        for _i in range(3673):
            _value = random.choice(self._envelopes)
            _currentEnvelopes.append(_value)
            self._envelopes.remove(_value)

        self._maxEnvelope = max(_currentEnvelopes)

        return self._maxEnvelope

    def find_max(self):

        for _i in self._envelopes:
            if _i < self._maxEnvelope and _i != self._envelopes[-1]:
                self._envelopes.remove(_i)
            elif _i > self._maxEnvelope or _i == self._envelopes[-1]:
                self._maxEnvelope = _i

        return self._maxEnvelope

    def show_env(self):
        return self._envelopes


my_list = []

for i in range(10000):
    value = random.randint(1, 50000)
    my_list.append(value)


my_game = EnvelopeGame(my_list)

print(my_list)
print(max(my_game.show_env()))
print(my_game.pick_env())
print(my_game.show_env())
print(my_game.find_max())

