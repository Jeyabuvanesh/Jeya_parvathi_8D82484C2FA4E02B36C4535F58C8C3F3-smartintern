# -*- coding: utf-8 -*-
"""challenge02.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OL2z1u8NndeaaPgZ83DV1uZzA4wSnsjA
"""

class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance+=amount
      #self.__account_balance=self.__account_balance+amount
      print("Deposit ₹{}.New balance:₹{}".format(amount,self.__account_balance))
    else:
        print("Invalid deposit amount. Please deposit a positive amount.")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      #self.__account_balance=self.__account_balance_amount
      print("Withdraw ₹{}.New balance:₹{}".format(amount,self.__account_balance))
    else:
     print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
     print("Account balance for {}(Account #{}): ₹{}".format(self.__account_number,self.__account_holder_name,
                                                            self.__account_balance))

account= BankAccount(account_number="123456789",account_holder_name="Shanmugam",
                     initial_balance=5000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()