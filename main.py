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
    """
    db = DBController()
    command = f"DELETE FROM books WHERE title = '{title}';"
    db.execute(command)
    db.commit()
    db.close()


def book_id_retrieval(title):
    """
    This function will retrieve the ID of a book of a provided title.

    Return
    -------------
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


def update_book(book_id,title,rating,genre,desc,review):
    db = DBController()
    command = f"UPDATE books SET title='{title}', rating='{rating}', genre='{genre}', desc='{desc}' , review='{review}' WHERE id = {book_id};"
    print(command)
    db.execute(command)
    db.commit()
    db.close()
    
if __name__ == "__main__":
    ui = UI()
    #new_book("HP",5,"Fantasy","Wizards","This is good book.")
    #book_id_retrieval("NAH")
