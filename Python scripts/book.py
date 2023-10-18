def sort(collection, item):
  item = item.capitalize()
  index = 0
  for thing in collection:
    if thing[0] > item[0]:
      index = index + 1
  books.insert(index, item)

books = []

print("What is the title of the first book?")
book1 = input()
sort(books, book1)

print("What is the title of the second book?")
book2 = input()
sort(books, book2)

print("What is the title of the third book?")
book3 = input()
sort(books, book3)

print("Your alphabetical collection is...")
print(books)
