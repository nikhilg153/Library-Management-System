#Create a library class
#display book
#lend book(who owns the book if not present)
#add book
#return book

#Harrylibrary = Library(listofbooks,library name)

#dictionary(books:nameofperson)
#create a main function and run an innfinite while loop askinng users for
# their input

class Library:
    def __init__(self,list_of_books,name):
        self.list_of_books = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.list_of_books:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(f"Database has been updated.you can take the book now")
        else:
            print(f"Book is already being taken by {self.lendDict[book]} ")

    def addBook(self,book):
        self.list_of_books.append(book)
        print("Book has been added to the list")

    def returnbook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    nikhil = Library(["C","python","C++","Java"],"codewithnikhil")

    while(True):
        print(f"Welcome to the {nikhil.name} library.Enter your choice to continue")
        print(" 1.Display Books\n 2.Lend Book\n 3.Add Book\n 4.Return Book\n")
        user_choice = input()
        if user_choice not in ["1","2","3","4"]:
            print("Enter valid number")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            nikhil.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            nikhil.lendBook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            nikhil.addBook(book)


        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            nikhil.returnbook(book)

        else:
            print("Not a valid number")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue




