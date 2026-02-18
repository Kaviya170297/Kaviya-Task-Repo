# #1.  BankAccount with attributes like account_number and balance and methods like deposit() and withdraw().
# # Inherit from this class  to create subclasses SavingsAccount and CurrentAccount
#
# class BankAccount:
#     def __init__(self, account_number, initial_balance=0):
#         self.account_number = account_number
#         # Encapsulation: __balance is private to prevent direct external access
#         self.__balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         # Base logic for withdrawal
#         if amount > self.__balance:
#             print("Insufficient funds!")
#             return False
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#             return False
#
#         self.__balance -= amount
#         print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
#         return True
#
#     def get_balance(self):
#         """Public method to safely view the private balance."""
#         return self.__balance
#
#     def _set_balance(self, amount):
#         """Protected method for subclasses to update balance if needed."""
#         self.__balance = amount
#
#
# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, initial_balance, interest_rate):
#         super().__init__(account_number, initial_balance)
#         self.interest_rate = interest_rate  # e.g., 0.05 for 5%
#
#     def apply_interest(self):
#         interest = self.get_balance() * self.interest_rate
#         self.deposit(interest)
#         print(f"Interest of {interest} applied at rate {self.interest_rate * 100}%")
#
#
# class CurrentAccount(BankAccount):
#     def __init__(self, account_number, initial_balance, min_balance):
#         super().__init__(account_number, initial_balance)
#         self.min_balance = min_balance
#
#     def withdraw(self, amount):
#         # Override withdrawal to respect minimum balance requirement
#         potential_balance = self.get_balance() - amount
#         if potential_balance < self.min_balance:
#             print(f"Transaction failed: Must maintain a minimum balance of {self.min_balance}")
#             return False
#
#         return super().withdraw(amount)
#
#
# # --- Example Usage ---
#
# print("--- Savings Account ---")
# savings = SavingsAccount("SAV123", 100000, 0.05)
# savings.apply_interest()
#
# print("\n--- Current Account ---")
# current = CurrentAccount("CUR456", 50000, 1000)
# current.withdraw(49500)  # Should fail due to min_balance
# current.withdraw(100)  # Should succeed

#2.Employee management:
# class Employee:
#    def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# def calculate_salary(self):
#         return self.salary
#
#
# # RegularEmployee subclass
# class RegularEmployee(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)   # call parent constructor
#         self.bonus = bonus
#     def calculate_salary(self):
#         return self.salary + self.bonus
#
#
# # ContractEmployee subclass
# class ContractEmployee(Employee):
#     def __init__(self, name, salary, contract_bonus):
#         super().__init__(name, salary)
#         self.contract_bonus = contract_bonus
#
#     def calculate_salary(self):
#         return self.salary + self.contract_bonus
#
#
# # Manager subclass
# class Manager(Employee):
#     def __init__(self, name, salary, allowance):
#         super().__init__(name, salary)
#         self.allowance = allowance
#
#     def calculate_salary(self):
#         return self.salary + self.allowance
#
#
# # Main program
# emp1 = RegularEmployee("Kumar", 30000, 5000)
# emp2 = ContractEmployee("Ravi", 25000, 3000)
# emp3 = Manager("Anita", 50000, 10000)
#
# print(emp1.name, "Salary:", emp1.calculate_salary())
# print(emp2.name, "Salary:", emp2.calculate_salary())
# print(emp3.name, "Salary:", emp3.calculate_salary())
#
# #3. Vehicle rental
#
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
#     def __init__(self, model, rental_rate, brand):
#         super().__init__(model, rental_rate)
#         self.brand = brand
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Bike class
# class Bike(Vehicle):
#     def __init__(self, model, rental_rate, brand):
#         super().__init__(model, rental_rate)
#         self.brand = brand
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Truck class
# class Truck(Vehicle):
#     def __init__(self, model, rental_rate, brand):
#         super().__init__(model, rental_rate)
#         self.brand = brand
#
#     def calculate_rental(self, days):
#         return self.rental_rate * days
#
#
# # Main program
# car = Car("City", 2000, "Honda")
# bike = Bike("R15", 500, "Yamaha")
# truck = Truck("407", 3000, "Tata")
#
# days = 3
#
# print("Car Brand:", car.brand)
# print("Car Model:", car.model)
# print("Car Rental:", car.calculate_rental(days))
#
# print("\nBike Brand:", bike.brand)
# print("Bike Model:", bike.model)
# print("Bike Rental:", bike.calculate_rental(days))
#
# print("\nTruck Brand:", truck.brand)
# print("Truck Model:", truck.model)
# print("Truck Rental:", truck.calculate_rental(days))
