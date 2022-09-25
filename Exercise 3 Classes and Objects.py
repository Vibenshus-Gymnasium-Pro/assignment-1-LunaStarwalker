#Exercise 3 - Classes and Objects

class BankAccount:

    def __init__(self, pin):
        self._balance = 0
        self._pin = pin

    def pin_check(self, pin):
        if pin == self._pin:
            return True
        else:
            print("The pin is incorrect. Please try again.")
            return False

    def amount_check(self, amount):
        if amount > self._balance:
            print("Withdrawal cannot be completed due to lacking funds in account.")
            return False
        else:
            return True

    def deposit(self, pin, amount):
        if self.pin_check(pin):
            self._balance +=  amount

    def withdraw(self, pin, amount):
        if self.pin_check(pin) and self.amount_check(amount):
            self._balance -= amount

    def balance(self, pin):
        if self.pin_check(pin):
            return self._balance

    def new_pin(self, old_pin, new_pin):
        if self.pin_check(old_pin):
            self._pin = new_pin

    def see_pin(self):
        return self._pin


class SavingsAccount(BankAccount):

    def interest_rate(self, pin, rate, time):
        if self.pin_check(pin):
            self._balance = self._balance*((1+rate)**time)


my_savings = SavingsAccount(1234)

my_savings.deposit(1234, 100000)

my_savings.interest_rate(1234, 0.05, 6)

print(my_savings.balance(1234))
