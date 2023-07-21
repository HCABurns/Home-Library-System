#Imports
from tkinter import *
from db_controller import DBController
from PIL import ImageTk, Image
import time


class UI():
    """
    This class will store all the information regarding the UI.

    Methods
    --------------
    __init__() - Creates a window with correct geometry, title and logo.
    home_page() - Sets the UI for the home page.
    add_page() - Sets the UI for the adding a book page.
    view_page() - Sets the UI for the view books page.
    edit_page_search() - Sets the UI for the search for a book to be editted.
    edit_page(book_id) - Sets the UI to allow a book to be editted.
    check_title(title) - Checks if a title is in the database or not.
    check_all_details(self,title,rating,genre,desc,review) - Checks if all the relevant information
                                                             has been entered for adding a book.
    delete_page() - Sets the UI for the delete a book page.

    clear_window() - Removes all widgets that are currently on the page.
    """

    def __init__(self):
        """
        Creates a window, adds a background image and adds the logo to the top of the page.
        """
        #Create a basic window.
        self.root = Tk()
        self.width = 800
        self.height =600
        self.root.geometry("{}x{}".format(self.width, self.height))

        #Change icon and title of the window.
        self.root.title("Home Library System")
        self.root.iconbitmap("images\icon.ico")

        #Set the home page.
        self.home_page()

        #Run the mainloop.
        self.root.mainloop()


    def set_background(self):
        """
        This function will add the background picture to the screen.
        """
        self.bg = PhotoImage(file="images/bg.png")
        self.canvas = Canvas(self.root, width = self.width,height = self.height)
        self.canvas.pack(fill = "both", expand = True)
        self.canvas.create_image(0,0, image=self.bg, anchor = "nw")


    def home_page(self):
        """
        This function will add the relevant buttons for the home page.
        """
        #Remove previous content
        self.clear_window()
        
        #Create a frame for the buttons to be placed
        button_frame = Frame(self.canvas,background="")
        button_frame.pack(pady=(270,0))

        #Add logo to the page
        image = PhotoImage(file="images\logo2sm.png")
        self.root.image = image #Prevents garbage collection
        self.canvas.create_image(self.width/2,150, image=image)

        #Button to add a new book
        image2 = Image.open("images/add_book_button.png")
        add_button = ImageTk.PhotoImage(image2)
        label = Label(image=add_button)
        label.image=add_button
        button = Button(button_frame,image=add_button,bd = 0, command = self.add_page, borderwidth=0)
        button.pack(pady=(0, 15))

        #Button to view all books
        image = Image.open("images/view_book_button.png")
        view_button = ImageTk.PhotoImage(image)
        label = Label(image=view_button)
        label.image=view_button
        button = Button(button_frame,image=view_button,bd = 0, command = self.view_page, borderwidth=0)
        button.pack(pady=(0, 15))

        #Button to edit a book.
        image = Image.open("images/edit_book_button.png")
        edit_button = ImageTk.PhotoImage(image)
        label = Label(image=edit_button)
        label.image=edit_button
        button = Button(button_frame,image=edit_button,bd = 0, command = self.edit_page_search, borderwidth=0)
        button.pack(pady=(0, 15))

        #Button to delete a new book
        image2 = Image.open("images/delete_book_button.png")
        delete_button = ImageTk.PhotoImage(image2)
        label = Label(image=delete_button)
        label.image=delete_button
        button = Button(button_frame,image=delete_button,bd = 0, command = self.delete_page, borderwidth=0)
        button.pack(pady=(0, 15))


    def add_page(self):
        """
        This function will set the screen to be able to input data and add a new book to the collection.
        """
        #Remove previous content
        self.clear_window()

        #Add Label and input for title.
        title_frame = Frame(self.canvas)
        title_frame.pack()
        title_label = Label(title_frame,text = "Title:")
        title_label.grid(row = 0, column = 0)
        title_entry = Entry(title_frame)
        title_entry.grid(row = 0, column = 1)

        #Add Label and input for rating.
        rating_frame = Frame(self.canvas)
        rating_frame.pack()
        rating_label = Label(rating_frame,text = "Rating:")
        rating_label.grid(row = 0, column = 0)
        rating_entry = Entry(rating_frame)
        rating_entry.grid(row = 0, column = 1)

        #Add Label and input for genre.
        genre_frame = Frame(self.canvas)
        genre_frame.pack()
        genre_label = Label(genre_frame,text = "Genre:")
        genre_label.grid(row = 0, column = 0)
        genre_entry = Entry(genre_frame)
        genre_entry.grid(row = 0, column = 1)

        #Add Label and input for description.
        desc_frame = Frame(self.canvas)
        desc_frame.pack()
        desc_label = Label(desc_frame,text = "Description:")
        desc_label.grid(row = 0, column = 0)
        desc_entry = Entry(desc_frame)
        desc_entry.grid(row = 0, column = 1)

        #Add Label and input for review.
        review_frame = Frame(self.canvas)
        review_frame.pack()
        review_label = Label(review_frame,text = "Review:")
        review_label.grid(row = 0, column = 0)
        review_entry = Entry(review_frame)
        review_entry.grid(row = 0, column = 1)

        #Button to add a new book
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image2 = Image.open("images/add_book_button.png")
        add_button = ImageTk.PhotoImage(image2)
        label = Label(image=add_button)
        label.image=add_button
        button = Button(button_frame,image=add_button,bd = 0, borderwidth=0, command = lambda :self.check_all_details(title_entry.get(),
                                                                                                       rating_entry.get(),
                                                                                                       genre_entry.get(),
                                                                                                       desc_entry.get(),
                                                                                                       review_entry.get()))
        button.pack(pady=(0, 15))
        

    def delete_page(self):
        """
        This function will set the screen to be able to delete a book that is in the collection.
        """
        #Remove previous content
        self.clear_window()

        #Add Label and input for title.
        title_frame = Frame(self.canvas)
        title_frame.pack()
        title_label = Label(title_frame,text = "Title:")
        title_label.grid(row = 0, column = 0)
        title_entry = Entry(title_frame)
        title_entry.grid(row = 0, column = 1)

        #Button to delete a new book
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/delete_book_button.png")
        delete_button = ImageTk.PhotoImage(image)
        label = Label(image=delete_button)
        label.image=delete_button
        button = Button(button_frame,image=delete_button,bd = 0, command = lambda : self.delete_book(title_entry.get()), borderwidth=0)
        button.pack(pady=(0, 15))
        pass


    def view_page(self):
        """
        This function will set the screen to be able to view the books that are in the collection.
        """
        #Remove previous content
        self.clear_window()

        #Add books in a scrollable frame
        
        pass


    def edit_page_search(self):
        """
        This function will set the screen to be able to search for a book that is in the collection to be editted.
        """
        #Remove previous content
        self.clear_window()

        #Search bar for the book name
        search_frame = Frame(self.canvas)
        search_frame.pack()
        search_label = Label(search_frame,text = "Title:")
        search_label.grid(row = 0, column = 0)
        search_entry = Entry(search_frame)
        search_entry.grid(row = 0, column = 1)

        #Search button
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/search_button.png")
        delete_button = ImageTk.PhotoImage(image)
        label = Label(image=delete_button)
        label.image=delete_button
        button = Button(button_frame,image=delete_button,bd = 0, command = lambda : self.check_title(search_entry.get()), borderwidth=0)
        button.pack(pady=(0, 15))


    def edit_page(self,book_id):
        """
        This function allows for editing the details of a book in the database.

        Parameters
        ----------------
        book_id : int
            This refers to the primary key of the book that is to be editted.
        """
        #Remove previous content
        self.clear_window()

        from main import book_retriever
        print("Book id: ",book_id)
        book = book_retriever(book_id)
        book.to_string()
        
        #Add Label and input for title.
        title_frame = Frame(self.canvas)
        title_frame.pack()
        title_label = Label(title_frame,text = "Title:")
        title_label.grid(row = 0, column = 0)
        title_entry = Entry(title_frame)
        title_entry.insert(0, book.get_title())
        title_entry.grid(row = 0, column = 1)

        #Add Label and input for rating.
        rating_frame = Frame(self.canvas)
        rating_frame.pack()
        rating_label = Label(rating_frame,text = "Rating:")
        rating_label.grid(row = 0, column = 0)
        rating_entry = Entry(rating_frame)
        rating_entry.insert(0, book.get_rating())
        rating_entry.grid(row = 0, column = 1)

        #Add Label and input for genre.
        genre_frame = Frame(self.canvas)
        genre_frame.pack()
        genre_label = Label(genre_frame,text = "Genre:")
        genre_label.grid(row = 0, column = 0)
        genre_entry = Entry(genre_frame)
        genre_entry.insert(0, book.get_genre())
        genre_entry.grid(row = 0, column = 1)

        #Add Label and input for description.
        desc_frame = Frame(self.canvas)
        desc_frame.pack()
        desc_label = Label(desc_frame,text = "Description:")
        desc_label.grid(row = 0, column = 0)
        desc_entry = Entry(desc_frame)
        desc_entry.insert(0, book.get_desc())
        desc_entry.grid(row = 0, column = 1)

        #Add Label and input for review.
        review_frame = Frame(self.canvas)
        review_frame.pack()
        review_label = Label(review_frame,text = "Review:")
        review_label.grid(row = 0, column = 0)
        review_entry = Entry(review_frame)
        review_entry.insert(0, book.get_review())
        review_entry.grid(row = 0, column = 1)

        #Button to edit a book.
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/edit_book_button.png")
        edit_button = ImageTk.PhotoImage(image)
        label = Label(image=edit_button)
        label.image=edit_button
        button = Button(button_frame,image=edit_button,bd = 0, command = lambda : self.edit_page_update(book_id,
                                                                                                       title_entry.get(),
                                                                                                       rating_entry.get(),
                                                                                                       genre_entry.get(),
                                                                                                       desc_entry.get(),
                                                                                                       review_entry.get()))
        button.pack(pady=(0, 15))


    def edit_page_update(self,book_id,title,rating,genre,desc,review):
        """
        This function will edit a book that is in the databse

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
        from main import update_book
        update_book(book_id,title,rating,genre,desc,review)

        #Remove previous content
        self.clear_window()

        #Updated label
        updated_label = Label(self.canvas,text = "Update Successful!")
        updated_label.pack()

        #Return Button
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/return_button.png")
        return_button = ImageTk.PhotoImage(image)
        label = Label(image=return_button)
        label.image=return_button
        button = Button(button_frame,image=return_button,bd = 0, command = self.home_page)
        button.pack(pady=(0, 15))

        
    def check_title(self,title):
        """
        This function will check if a book with a title is in the database.

        Parameters
        ----------------
        title : str
            This is title of the book that is being checked.
        """
        from main import book_id_retrieval
        #Retrieve the book id or None if it's not in the database.
        book_id = book_id_retrieval(title)
        if book_id != None:
            self.edit_page(book_id)
        #Testing output
        else:
            print("NO BOOK FOUND WITH TITLE")


    def check_all_details(self,title,rating,genre,desc,review):
        """
        This function checks that all the information is present when adding a book.

        Parameters
        -----------------
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
        print(title)
        print(rating)
        print(genre)
        print(desc)
        print(review)
        valid = True
        #Ensure that they're not empty
        if title == "":
            valid = False
            pass
        if rating == "" or rating.isnumeric() == False:
            valid = False
            pass
        if genre == "":
            valid = False
            pass
        if desc == "":
            valid = False
            pass
        if review == "":
            valid = False
            pass
        #If all is valid, then add the book to the database.
        if valid:
            from main import new_book
            new_book(title,rating,genre,desc,review)
            

    def delete_book(self,title):
        """
        This will remove a book from the collection.

        Parameters
        ------------------
        title : str
            This is the title of the book to be deleted from the collection.
        """
        if title != "":
            from main import delete_book
            delete_book(title)
        
    
    def clear_window(self):
        """
        This function will destroy everything in the window and leave it empty..
        """
        for widget in self.root.winfo_children():
            widget.destroy()

        #Set the background again.
        self.set_background()


    
if __name__ == "__main__":
    ui = UI()
