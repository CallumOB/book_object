"""
    This program was written for a lab test in university. 
    The program demonstrates object oriented qualities such as inheritance and operator overloading.

    The aim of this program is to create two classes: 
    - A publication class which contains basic information about a publication (title and price).
    - A book class which inherits attributes from the publication class, and builds upon them.
    - The book class overloads the addition operator, so that when two book objects are added to eachother,
      a new object is returned featuring a new title the user specifies, and a combined page number and price 
      from the two book objects added together. This includes proper error checking.

    I achieved a score of 95% with this program.

    Written By: Callum O'Brien
    Date Created: 13/12/22
"""

class Publication(object):
    """ A class to store information about a publication such as title and price. """
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price 

    def __str__(self):
        """ Displays information about the publication including title and price. """
        return f"Title: {self.title}\nPrice: €{self.price}"


class Book(Publication):
    """ A class to store information about a book, using attributes inherited from the publication class.  """
    def __init__(self, title: str = "", price: float = 0, pages: int = 0):
        # If the constructor is called with no arguments, the constructor prompts the user to enter their own values.
        if title == "":
            # This loop runs until the program is satisfied the user has entered the correct values.
            while True:
                try: 
                    title = input("Please enter the title of the book.\t")
                    price = float(input("Please enter the book price.\t"))
                    Publication.__init__(self, title, price)
                    self.pages = int(input("Please enter the number of pages.\t"))
                    break
                except ValueError:
                    print("\n\nPlease enter valid answers.\n\n")

        # If the constructor is called with arguments, the instance is intialised as such using those arguments. This occurs in the __add__ method.
        else:
            Publication.__init__(self, title, price)
            self.pages = pages

    def __add__(self, other_book):
        """ When the user adds two books together, a new instance is created with the combined page count and price of the two books. """
        if type(other_book) == Book:
            new_title = input("Please enter the title of the new book.\t")
            new_price = self.price + other_book.price
            new_pages = self.pages + other_book.pages
            new_book = Book(new_title, new_price, new_pages)

            return new_book
        else:
            return "You can only add another book to a book instance.\n"

    def __str__(self):
        """ Displays information about the book, including title, price and page count. """
        return f"Title: {self.title}\nPrice: €{self.price}\nPage Count: {self.pages}\n"


book1 = Book()
print(book1)

book2 = Book()
print(book2)

print(book1 + book2)

print(book1 + 1) # This demonstrates the error checking in place.