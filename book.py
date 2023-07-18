#Imports
#None

class Book():
    """
    This Book class is used to store information regarding an individual book.
    NOTE: This class uses the __  variables. This means they're private and can only be changed using the set functionality.

    Methods
    ----------------
    __init__() - This function will instantiate a book object.
    __init__(title, rating,genre,desc,review) - This function will instantiate
                                                a book object and fill it with
                                                information.
    toString() - This function will print the title, rating, genre, desc and review
                 of the book to the console.
    getTitle() - Returns the title of the book.
    getRating() - Returns the rating of the book.
    getGenre() - Returns the genre of the book.
    getDesc() - Returns the description of the book.
    getReview() - Returns the review of the book.
    setTitle(title) - Sets the title of the book.
    setRating(rating) - Sets the rating of the book.
    setGenre(genre) - Sets the genre of the book.
    setDesc(desc) - Sets the description of the book.
    setReview(review) - Sets the review of the book.
    """
    def __init__(self,title = None, rating = None,genre = None,desc = None,review = None):
        """
        This function will instantiate a book object and fill it with information.

        Parameters
        -------------
        title : string
            This is a string of the title of the book.
        rating : int
            This is an integer (0-10) of the given rating of the book.
        genre : string
            This is a string of what genre the book is.
        desc : string
            This is a string of a short description of the plot of the book.
        review : string
            This is a string of a review of the book. 
        """
        self.__title = title
        self.__rating = rating
        self.__genre = genre
        self.__desc = desc
        self.__review = review


    def toString(self):
        """
        This is a method to print out the book parameters to console for testing purposes.
        """
        print(f"Title: {self.__title}")
        print(f"Rating: {self.__rating}/10")
        print(f"Genre: {self.__genre}")
        print(f"Description: {self.__desc}")
        print(f"Review: {self.__review}\n")


    def getTitle(self):
        """
        Returns the title of the book.
        """
        return self.__title


    def getRating(self):
        """
        Returns the rating of the book.
        """
        return self.__rating
    

    def getGenre(self):
        """
        Returns the genre of the book.
        """
        return self.__genre
    

    def getDesc(self):
        """
        Returns the description of the book.
        """
        return self.__desc
    

    def getReview(self):
        """
        Returns the review of the book.
        """
        return self.__review
    

    def setTitle(self,title):
        """
        Sets the title of the book to the given text.

        Parameter
        -----------------
        title : str
             This will change the title to the given string. 
        """
        self.__title = title
         

    def setRating(self,rating):
        """
        Sets the rating of the book to the given integer.

        Parameter
        -----------------
        rating : int
             This will change the rating to the given integer.
        """
        self.__rating = rating
         

    def setGenre(self,genre):
        """
        Sets the genre of the book to the given text.

        Parameter
        -----------------
        genre : str
             This will change the genre to the given string. 
        """
        self.__genre = genre
         

    def setDesc(self,desc):
        """
        Sets the description of the book to the given text.

        Parameter
        -----------------
        desc : str
             This will change the description to the given string. 
        """
        self.__desc = desc
         

    def setReview(self,review):
        """
        Sets the review of the book to the given text.

        Parameter
        -----------------
        review : str
             This will change review to the given string. 
        """
        self.__review = review

    
def testHarness():
    """
    This is a test harness to test the functionality of the Book class. 
    """
    book1 = Book()
    book2 = Book("HP","7","Fantasy","Wizards beat bloke with no nose","Good")
    #book1.toString()
    #book2.toString()
    #book2.setRating(9)
    #book2.toString()

    book2.__title = "THIS WILL NOT WORK"
    book2.toString()
    book2.setTitle("USING CORRECT METHOD")
    print(book2.getTitle())
    book2.toString()

if __name__ == "__main__":
    testHarness()


    
