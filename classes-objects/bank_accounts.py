# Bank Account via Codedex but added change_pin


class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
      self.balance = self.balance + amount
      return self.balance
    
  def withdraw(self, amount):
      self.balance = self.balance - amount

  def display_balance(self):
      print(f"${self.balance}")
  
  def change_pin(self):
      new_pin = input("New pin: ")
      self.pin = new_pin
      print("PIN successfully changed")
    
checking_account = BankAccount("Jane", "Doe", 123456, "checking", 0000, 250.00)

checking_account.deposit(100)

checking_account.display_balance()

checking_account.withdraw(50)

checking_account.display_balance()

checking_account.change_pin()


