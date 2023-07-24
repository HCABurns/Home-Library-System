from ui import UI
from db_controller import DBController
from book import Book

def new_book(title,rating,genre,desc,review):
    """
    This function will add a book to the database.
    """
    db = DBController()
    command = f"INSERT INTO books (title,rating,genre,desc,review) VALUES ('{title}',{rating},'{genre}','{desc}','{review}');"
    db.execute(command)
    db.commit()
    db.close()


def delete_book(title):
    """
    This function will remove a book of a provided title from the database.

    Parameters
    ----------------
    title : str
        This is the title of the book to be deleted.

    Return
    -----------------
    boolean - True if removed and false if it has not been.
    """
    #If the book is in the database, then delete it. Otherwise return False.
    if book_id_retrieval(title) != None:
        db = DBController()
        command = f"DELETE FROM books WHERE title = '{title}';"
        executed = db.execute(command)
        db.commit()
        db.close()
        return True
    return False


def book_id_retrieval(title):
    """
    This function will retrieve the ID of a book of a provided title.

    Parameters
    ----------------
    title : str
        This is the title of the book to be retrieve the id of.

    Return
    ---------------
    int - Integer of the books id or None if not in the database.
    """
    db = DBController()
    command = f"SELECT id FROM books WHERE title = '{title}';"
    book_ids = db.execute(command)
    for book_id in book_ids:
        db.close()
        return book_id[0]
    db.close()
    return None


def book_retriever(book_id):
    """
    This function will take a book_id and return a book object containing all the relevant information.

    Return
    ----------------
    Book - Book object with all the information in the database about that book. 
    """
    db = DBController()
    command = f"SELECT * FROM books WHERE id = {book_id};"
    book = db.execute(command)
    for info in book:
        db.close()
        return Book(info[1],info[2],info[3],info[4],info[5])
    db.close()
    return None


def is_book_present(title):
    """
    This function will take a book title and return a book object containing all the relevant information.

    Return
    ----------------
    Book - Book object with all the information in the database about that book. 
    """
    db = DBController()
    command = f"SELECT * FROM books WHERE title = {title};"
    book = db.execute(command)
    for info in book:
        db.close()
        return True
    db.close()
    return False


def update_book(book_id,title,rating,genre,desc,review):
    """
    This function will update a record in the database.

    Parameters
    -----------------
    book_id : int
        This is the book id to be updated.
    title : str
        This is the title of the book.
    rating : int
        This is a value regarding the rating of the book.
    genre : str
        This is the genre of the book.
    desc : str
        This is a brief description of the book.
    review : str
        This is a review of the book.
    """
    db = DBController()
    command = f"UPDATE books SET title='{title}', rating='{rating}', genre='{genre}', desc='{desc}' , review='{review}' WHERE id = {book_id};"
    db.execute(command)
    db.commit()
    db.close()


def get_all_books():
    """
    This function will return an array of book objects for every book in the databse.

    Return
    ---------------
    Array - Array of Book objects for every book in the database.
    """
    db = DBController()
    command = "SELECT * FROM books"
    executed = db.execute(command)
    books = []
    for info in executed:
        books.append(Book(info[1],info[2],info[3],info[4],info[5]))
    return books

    
if __name__ == "__main__":
    ui = UI()
    #new_book("HP",5,"Fantasy","Wizards","This is good book.")
    #book_id_retrieval("NAH")
