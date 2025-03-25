class Library :
    def __init__(self,list,name)
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for books in self.booklist:
            print(books)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book has been updated, you may proceed to take the book")

        else:
            print(f"The book has already been lend to {self.lendDict[book]}")   


    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")


    def returnbook(self,book):
        self.lendDict.pop(book)


if __name__ == "__main__":
    
    books = Library(["Basic Tips of Coding","Harry Potter", "Timmy Failure","Dairy of Wimpy kid","Python for beginners"],"Jurong East Library")
    

    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a book")
        print("4. Return a book")
        user_input = input()
        if user_input not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_input = int(user_input)

        if user_input == 1:
            books.displayBooks()

        elif user_input == 2:
            books = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            books.lendbook(user,books)


        elif user_input == 3 :
            books = input("Enter the name of the book you want to add to the Library")
            books.addbook(books)

        