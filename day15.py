# class Dog:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#     def bark(self):
#         print(f"{self.name} says {self.sound}!")

# rex = Dog("Rex", "Woof")
# rex.bark()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("not enough funds")
        else:
            self.balance = self.balance - amount
    def show(self):
        print(f"Account holder: {self.owner} \nBalance: ${self.balance}")

acc = BankAccount("Yasir", 100)
print(acc.balance)      # 100
acc.deposite(50)
print(acc.balance)      # 150
acc.withdraw(30)        # enough → subtract
print(acc.balance)      # 120
acc.withdraw(500)       # too much → refuse
print(acc.balance)      # still 120
acc.show()
