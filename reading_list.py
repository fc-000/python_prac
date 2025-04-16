# Reading List 📚
# Codédex

books = ['The Alchemist', 
         'The Little Prince', 
         'The Karamov Brothers', 
         'The Stranger']

print(books)

add_book = input("What book would you like to add? ")
books.append(add_book)
print(f"'{add_book}' added!")
print(books)

remove_book = input("What book would you like to remove? ")
books.remove(remove_book)
print(f"'{remove_book}' removed!")

remove_book_pos = int(input("What book would you like to remove by position (number)? "))
remove_by_position = books.pop(remove_book_pos)
print(f"'{remove_by_position}' removed!")


print(books)

'''
books = ['Harry Potter',
         '1984',
         'The Fault in Our Stars',
         'The Mom Test',
         'Life in Code']

print(books)

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)

print(books)

'''