class BankAccount():
  def deposit():
    pass
  
  def withdraw():
    pass
  
class SavingsAccount(BankAccount):
  def __init__(self):
    self.balance = 0
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Error!'

    else:
      raise ValueError()

  def withdraw(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Insufficient funds'
      else:
        return 'Error!'
    else:
      raise ValueError() 
 
class Atm(BankAccount):
  def __init__(self):
    self.balance = 10000
      
  def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:
          if (self.balance -amount) > 1000:
            self.balance-=amount
            return self.balance
          else:
            return 'Insufficient funds!'
        else:
          return 'Insufficient Funds'
      else:
        return 'Error!'
    else:
      raise ValueError()
      
