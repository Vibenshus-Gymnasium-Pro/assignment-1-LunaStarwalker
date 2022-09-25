#Exercise 2 - Classes and Objects

class SimpleCounter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def clear(self):
        self._count = 0

    def get_value(self):
        return self._count


class DecrementingCounter(SimpleCounter):

    def decrement(self):
        self._count -= 1

    def increment(self):
        self._count += 2


my_counter = SimpleCounter()
my_dec_counter = DecrementingCounter()

my_counter.increment()
my_dec_counter.increment()

print(my_counter.get_value())
print(my_dec_counter.get_value())