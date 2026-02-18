# #1.Bank Account:
## Base class
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.__balance = balance   # encapsulation (private variable)
#
#     # deposit method
#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited:", amount)
#
#     # withdraw method
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")
#
#     # method to get balance safely
#     def get_balance(self):
#         return self.__balance
#
#
# # SavingsAccount subclass
# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate
#
#     # calculate interest
#     def calculate_interest(self):
#         interest = self.get_balance() * self.interest_rate / 100
#         print("Interest:", interest)
#
#
# # CurrentAccount subclass
# class CurrentAccount(BankAccount):
#     def __init__(self, account_number, balance, minimum_balance):
#         super().__init__(account_number, balance)
#         self.minimum_balance = minimum_balance
#
#     # override withdraw method
#     def withdraw(self, amount):
#         if self.get_balance() - amount >= self.minimum_balance:
#             super().withdraw(amount)
#         else:
#             print("Cannot withdraw. Minimum balance required.")
#
#
# # Main program
# savings = SavingsAccount("SA123", 10000, 5)
# current = CurrentAccount("CA456", 8000, 2000)
#
# print("Savings Account Balance:", savings.get_balance())
# savings.deposit(2000)
# savings.calculate_interest()
# savings.withdraw(3000)
# print("Final Savings Balance:", savings.get_balance())
#
# print("\nCurrent Account Balance:", current.get_balance())
# current.deposit(1000)
# current.withdraw(7000) #cannot withdraw
# current.withdraw(5000)
# print("Final Current Balance:", current.get_balance())

#
#2.Employee management:
# Base class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def calculate_salary(self):
#         return self.salary
#
#
# # RegularEmployee subclass
# class RegularEmployee(Employee):
#     def calculate_salary(self):
#         return self.salary
#
#
# # ContractEmployee subclass
# class ContractEmployee(Employee):
#     def calculate_salary(self):
#         return self.salary
#
#
# # Manager subclass
# class Manager(Employee):
#     def calculate_salary(self):
#         return self.salary
#
#
# # Main program
# emp1 = RegularEmployee("Kumar", 30000)
# emp2 = ContractEmployee("Ravi", 20000)
# emp3 = Manager("Priya", 50000)
#
# print("Regular Employee:", emp1.name)
# print("Salary:", emp1.calculate_salary())
#
# print("\nContract Employee:", emp2.name)
# print("Salary:", emp2.calculate_salary())
# 
# print("\nManager:", emp3.name)
# print("Salary:", emp3.calculate_salary())

#
# #3. Vehicle rental
# # Base class
# class Vehicle:
#     def __init__(self, model, rental_rate):
#         self.model = model
#         self.rental_rate = rental_rate
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Car class
# class Car(Vehicle):
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Bike class
# class Bike(Vehicle):
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Truck class
# class Truck(Vehicle):
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Main program
# car = Car("Honda City", 2000)
# bike = Bike("Yamaha R15", 500)
# truck = Truck("Tata 407", 3000)
#
# days = 2
#
# print("Car Model:", car.model)
# print("Car Rental:", car.calculate_rental(days))
#
# print("\nBike Model:", bike.model)
# print("Bike Rental:", bike.calculate_rental(days))
#
# print("\nTruck Model:", truck.model)
# print("Truck Rental:", truck.calculate_rental(days))

