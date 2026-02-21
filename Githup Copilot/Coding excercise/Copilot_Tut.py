# number = [1, 2, 3, 4, 5]
# strings = ["one", "two", "three", "four", "five"]

# for(num, string) in zip(number, strings):
#     print(f"{num} is written as {string}")

# Function to calculate sum of 2 numbers
# def sum(a, b):
#     return a + b

# convert celsius to fahrenheit
# def c_to_f(celsius):
#     return (celsius * 9/5) + 32 

# print(sum(3, 5))
# print(c_to_f(25))



# /* Bubble sort implementation */
# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         # Last i elements are already sorted
#         for j in range(0, n-i-1):
#             # Traverse the array from 0 to n-i-1
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print("Sorted array is:", sorted_arr)


#class to manage a bank account with deposit and withdrawal methods
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")