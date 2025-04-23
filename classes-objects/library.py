# class, bojects, & methods exercise - fc000

class Book:
  def __init__(self, title, author, isbn, available):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = available

  def borrow(self):
    if self.available:
      self.available = False
      print(f"You have borrowed '{self.title}'.")
    else:
      print(f"Sorry, '{self.title}' is not available right now.")

  def return_book(self):
    self.available = True
    print(f" '{self.title}' has been returned. Thank you!")

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"ISBN: {self.isbn}")
    print(f"Available: {self.available}")
    


book1 = Book("skibidi", "toilet", 947-000, True)
book2 = Book("toilet", "skibidi", 532-110, False)

book1.display_info()
book1.borrow()
book1.display_info()
book1.return_book()
book1.display_info()