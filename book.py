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
    to_string() - This function will print the title, rating, genre, desc and review
                 of the book to the console.
    get_title() - Returns the title of the book.
    get_rating() - Returns the rating of the book.
    get_genre() - Returns the genre of the book.
    get_desc() - Returns the description of the book.
    get_review() - Returns the review of the book.
    set_title(title) - Sets the title of the book.
    set_rating(rating) - Sets the rating of the book.
    set_genre(genre) - Sets the genre of the book.
    set_desc(desc) - Sets the description of the book.
    set_review(review) - Sets the review of the book.
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


    def to_string(self):
        """
        This is a method to print out the book parameters to console for testing purposes.
        """
        print(f"Title: {self.__title}")
        print(f"Rating: {self.__rating}/10")
        print(f"Genre: {self.__genre}")
        print(f"Description: {self.__desc}")
        print(f"Review: {self.__review}\n")


    def get_title(self):
        """
        Returns the title of the book.
        """
        return self.__title


    def get_rating(self):
        """
        Returns the rating of the book.
        """
        return self.__rating
    

    def get_genre(self):
        """
        Returns the genre of the book.
        """
        return self.__genre
    

    def get_desc(self):
        """
        Returns the description of the book.
        """
        return self.__desc
    

    def get_review(self):
        """
        Returns the review of the book.
        """
        return self.__review
    

    def set_title(self,title):
        """
        Sets the title of the book to the given text.

        Parameter
        -----------------
        title : str
             This will change the title to the given string. 
        """
        self.__title = title
         

    def set_rating(self,rating):
        """
        Sets the rating of the book to the given integer.

        Parameter
        -----------------
        rating : int
             This will change the rating to the given integer.
        """
        self.__rating = rating
         

    def set_genre(self,genre):
        """
        Sets the genre of the book to the given text.

        Parameter
        -----------------
        genre : str
             This will change the genre to the given string. 
        """
        self.__genre = genre
         

    def set_desc(self,desc):
        """
        Sets the description of the book to the given text.

        Parameter
        -----------------
        desc : str
             This will change the description to the given string. 
        """
        self.__desc = desc
         

    def set_review(self,review):
        """
        Sets the review of the book to the given text.

        Parameter
        -----------------
        review : str
             This will change review to the given string. 
        """
        self.__review = review

    
def test_harness():
    """
    This is a test harness to test the functionality of the Book class. 
    """
    book1 = Book()
    book2 = Book("HP","7","Fantasy","Wizards beat bloke with no nose","Good")
    #book1.to_string()
    #book2.to_string()
    #book2.set_rating(9)
    #book2.to_string()

    book2.__title = "THIS WILL NOT WORK"
    book2.to_string()
    book2.set_title("USING CORRECT METHOD")
    print(book2.get_title())
    book2.to_string()

if __name__ == "__main__":
    test_harness()


    
