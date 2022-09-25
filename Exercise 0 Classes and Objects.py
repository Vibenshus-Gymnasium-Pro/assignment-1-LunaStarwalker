#Exercise 0 - Classes and Objects

class SimpleCounter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def clear(self):
        self._count = 0

    def get_value(self):
        return self._count


my_counter = SimpleCounter()

print(my_counter.get_value())

my_counter.increment()
my_counter.increment()

print(my_counter.get_value())

my_counter.clear()

print(my_counter.get_value())