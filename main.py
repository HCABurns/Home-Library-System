from ui import UI
from db_controller import DBController

def new_book(title,rating,genre,desc,review):
    db = DBController()
    command = f"INSERT INTO books (title,rating,genre,desc,review) VALUES ('{title}',{rating},'{genre}','{desc}','{review}');"
    db.execute(command)
    db.commit()
    db.close()


def delete_book(title):
    db = DBController()
    command = f"DELETE FROM books WHERE title = '{title}';"
    db.execute(command)
    db.commit()
    db.close()

if __name__ == "__main__":
    ui = UI()
    new_book("HP",5,"Fantasy","Wizards","This is good book.")
