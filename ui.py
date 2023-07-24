#Imports
from tkinter import *
from db_controller import DBController
from PIL import ImageTk, Image
import time
from tkinter import ttk

class UI():
    """
    This class will store all the information regarding the UI.

    Methods
    --------------
    __init__() - Creates a window with correct geometry, title and logo.
    set_background() - Adds an image to the canvas as a background image.
    home_page() - Sets the UI for the home page.
    add_page() - Sets the UI for the adding a book page.
    add_confirmation_page() - Sets the UI for confirmation the book has been added to the database.
    delete_page() - Sets the UI for the delete a book page.
    delete_book(title) - Sends the title of the book to be removed from the database.
    delete_book_confirmation() - Adds UI to confirm a book has been deleted from the database.
    view_page() - Sets the UI for the view books page.
    edit_page_search() - Sets the UI for the search for a book to be editted.
    edit_page(book_id) - Sets the UI to allow a book to be editted.
    edit_page_confirmation(book_id,title,rating,genre,desc,review) - Sends information to be used to
                                                                     update the books information and
                                                                     displays a confirmation page.
    check_title(title) - Checks if a title is in the database or not.
    check_all_details(self,title,rating,genre,desc,review) - Checks if all the relevant information
                                                             has been entered for adding a book.
    
    add_return_button() - This adds a return button and update label to the window.
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

        #Set transparent if lime background colour
        self.root.wm_attributes('-transparentcolor', 'lime')

        #Change icon and title of the window.
        self.root.title("Home Library System")
        self.root.iconbitmap("images\icon.ico")

        #Set the home page.
        self.home_page(None)

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


    def home_page(self,e):
        """
        This function will add the relevant buttons for the home page.

        Parameters
        ----------------
        e : Event
            This is the event object from clikcing a button.
        """
        #Remove previous content
        self.clear_window()

        #Unbind the scroll
        self.canvas.unbind_all("<MouseWheel>")
    
        #Define button location.
        button_location = 300
        
        #Create a frame for the buttons to be placed
        button_frame = Frame(self.canvas,background="")
        button_frame.pack(pady=(270,0))

        #Add logo to the page
        image = PhotoImage(file="images\logo2sm.png")
        self.root.image = image #Prevents garbage collection
        self.canvas.create_image(self.width/2,150, image=image)

        #Button to add a new book
        image = PhotoImage(file="images/add_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,button_location, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", self.add_page)
        """image2 = Image.open("images/add_book_button.png")
        add_button = ImageTk.PhotoImage(image2)
        label = Label(image=add_button, bg = "lime")
        label.image=add_button
        button = Button(button_frame,image=add_button,bd = 0, command = self.add_page, borderwidth=0)#, bg = "lime")
        button.pack(pady=(0, 15))"""

        
        #Button to view all books
        button_location += 84
        image = PhotoImage(file="images/view_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,button_location, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", self.view_page)
        """
        image = Image.open("images/view_book_button.png")
        view_button = ImageTk.PhotoImage(image)
        label = Label(image=view_button)
        label.image=view_button
        button = Button(button_frame,image=view_button,bd = 0, command = self.view_page, borderwidth=0)
        button.pack(pady=(0, 15))
        """

        #Button to edit a book.
        button_location += 84
        image = PhotoImage(file="images/edit_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,button_location, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", self.edit_page_search)
        """
        image = Image.open("images/edit_book_button.png")
        edit_button = ImageTk.PhotoImage(image)
        label = Label(image=edit_button)
        label.image=edit_button
        button = Button(button_frame,image=edit_button,bd = 0, command = self.edit_page_search, borderwidth=0)
        button.pack(pady=(0, 15))
        """

        #Button to delete a new book
        button_location += 84
        image = PhotoImage(file="images/delete_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,button_location, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", self.delete_page)
        """
        image2 = Image.open("images/delete_book_button.png")
        delete_button = ImageTk.PhotoImage(image2)
        label = Label(image=delete_button)
        label.image=delete_button
        button = Button(button_frame,image=delete_button,bd = 0, command = self.delete_page, borderwidth=0)
        button.pack(pady=(0, 15))
        """


    def add_page(self,e):
        """
        This function will set the screen to be able to input data and add a new book to the collection.

        Parameters
        ----------------
        e : Event
            This is the event object from clikcing a button.
        """
        #Remove previous content
        self.clear_window()

        #Add Label and input for title.
        title_frame = Frame(self.canvas)
        title_frame.pack(pady=(40,20))
        title_label = Label(title_frame,text = "Title: ", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        title_label.grid(row = 0, column = 0)
        title_entry = Entry(title_frame, width = 100)
        title_entry.grid(row = 0, column = 1)

        #Add Label and input for rating.
        rating_frame = Frame(self.canvas)
        rating_frame.pack(pady=(0,20))
        rating_label = Label(rating_frame,text = "Rating:", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        rating_label.grid(row = 0, column = 0)
        rating_entry = Entry(rating_frame,width = 97)
        rating_entry.grid(row = 0, column = 1)

        #Add Label and input for genre.
        genre_frame = Frame(self.canvas)
        genre_frame.pack(pady=(0,20))
        genre_label = Label(genre_frame,text = "Genre:", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        genre_label.grid(row = 0, column = 0)
        genre_entry = Entry(genre_frame, width = 98)
        genre_entry.grid(row = 0, column = 1)

        #Add Label and input for description.
        desc_frame = Frame(self.canvas, bg = "#4487b8")
        desc_frame.pack(pady=(0,20))
        desc_label = Label(desc_frame,text = "Description:", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        desc_label.grid(row = 0, column = 0)
        desc_entry = Text(desc_frame, width = 68, height = 3)
        desc_entry.grid(row = 0, column = 1)

        #Add Label and input for review.
        review_frame = Frame(self.canvas, bg = "#4487b8")
        review_frame.pack()
        review_label = Label(review_frame,text = "Review:      ", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        review_label.grid(row = 0, column = 0)
        review_entry = Text(review_frame, width = 68, height = 10)
        review_entry.grid(row = 0, column = 1)

        #Button to add a new book
        image = PhotoImage(file="images/add_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,self.height-120, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", lambda e:self.check_all_details(e, title_entry.get(),
                                                                                           rating_entry.get(),
                                                                                           genre_entry.get(),
                                                                                           desc_entry.get(1.0,END),
                                                                                           review_entry.get(1.0,END)))
        """
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
        """
        self.add_return_button()
        

    def add_confirmation_page(self):
        """
        This function will add the return button after a book has been added to the database.
        """
        #Remove previous content
        self.clear_window()

        #Add the return button and updated label.
        l = Label(self.canvas,text="Book has been successfully added!", font=("Helvetica", "16", "bold"),bg="#4487b8",fg="white")
        l.place(x=self.width/2-160,y=self.height/2)
        self.add_return_button()


    def delete_page(self,e):
        """
        This function will set the screen to be able to delete a book that is in the collection.

        Parameters
        ----------------
        e : Event
            This is the event object from clikcing a button.
        """
        #Remove previous content
        self.clear_window()

        #Add Label and input for title.
        title_frame = Frame(self.canvas)
        title_frame.pack(pady=(self.height/2-40,0))
        title_label = Label(title_frame,text = "Title: ", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        title_label.grid(row = 0, column = 0)
        title_entry = Entry(title_frame, width = 100)
        title_entry.grid(row = 0, column = 1)

        #Button to delete a new book
        image = PhotoImage(file="images/delete_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,self.height/2+30, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", lambda e: self.delete_book(e,title_entry.get()))
        """
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/delete_book_button.png")
        delete_button = ImageTk.PhotoImage(image)
        label = Label(image=delete_button)
        label.image=delete_button
        button = Button(button_frame,image=delete_button,bd = 0, command = lambda : self.delete_book(title_entry.get()), borderwidth=0)
        button.pack(pady=(0, 15))
        """
        
        #Add the return button
        self.add_return_button()


    def delete_book(self,e,title):
        """
        This will remove a book from the collection.

        Parameters
        ------------------
        e : Event
            Event that occurs when a button is pressed.
        title : str
            This is the title of the book to be deleted from the collection.
        """
        if title != "":
            from main import delete_book
            deleted = delete_book(title)
            if deleted:
                self.delete_book_confirmation()


    def delete_book_confirmation(self):
        """
        This function will confirm when a book has been deleted.
        """
        #Remove previous content
        self.clear_window()

        #Updated label
        l = Label(self.canvas,text="Book has been successfully deleted!", font=("Helvetica", "16", "bold"),bg="#4487b8",fg="white")
        l.place(x=self.width/2-160,y=self.height/2)
        
        #Add the return button
        self.add_return_button()

    def view_page(self, e):
        """
        This function will set the screen to be able to view the books that are in the collection.

        Parameters
        ----------------
        e : Event
            This is the event object from clikcing a button.
        """
        #Remove previous content
        self.clear_window()

        #Get all books
        from main import get_all_books
        books = get_all_books()
        
        #Add books in a scrollable frame     
        display_frame = Canvas(self.canvas,width = self.width-100, height=self.height-150)
        display_frame.pack(side=LEFT, expand=1,anchor="n",pady=(30,0))

        scrollbar = ttk.Scrollbar(self.canvas,orient=VERTICAL,command=display_frame.yview)
        scrollbar.pack(side=RIGHT,fill=Y)

        display_frame.configure(yscrollcommand = scrollbar.set)
        display_frame.bind('<Configure>',lambda e: display_frame.configure(scrollregion=display_frame.bbox("all")))

        book_frame = Frame(display_frame)
        display_frame.create_window((0,0), window=book_frame ,anchor="nw")

        self.canvas.bind_all("<MouseWheel>", lambda e: self._on_mousewheel(e,display_frame))

        for i in range(len(books)):
            frame = Frame(book_frame)
            l = Label(frame,wraplength=self.width,text = f"Title: {books[i].get_title()}\nRating: {books[i].get_rating()}/10\nGenre: {books[i].get_genre()}\nDescription: {books[i].get_desc()}\nReview: {books[i].get_review()}\n\n", anchor = "w",justify="left").grid(row=i,column=0)
            frame.grid(sticky="W",row = i, column=0)

        #Add return button
        self.add_return_button()

        """
        button_frame = Frame(book_frame)
        button_frame.grid(row=len(books),column = 0)
        image = Image.open("images/return_button.png")
        return_button = ImageTk.PhotoImage(image)
        label = Label(image=return_button)
        label.image=return_button
        button = Button(button_frame,image=return_button,bd = 0, command = self.home_page)
        button.pack(pady=(0, 15))
        """

    def _on_mousewheel(self,event, book_frame):
        book_frame.yview_scroll(int(-1*(event.delta/120)), "units")

        
                
    def edit_page_search(self,e):
        """
        This function will set the screen to be able to search for a book that is in the collection to be editted.

        Parameters
        ----------------
        e : Event
            This is the event object from clikcing a button.
        """
        #Remove previous content
        self.clear_window()

        #Search bar for the book name
        title_frame = Frame(self.canvas)
        title_frame.pack(pady=(self.height/2-40,0))
        title_label = Label(title_frame,text = "Title: ", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        title_label.grid(row = 0, column = 0)
        search_entry = Entry(title_frame, width = 100)
        search_entry.grid(row = 0, column = 1)

        #Search button
        image = PhotoImage(file="images/search_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,self.height/2+30, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", lambda e: self.check_title(e,search_entry.get()))
        """
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/search_button.png")
        delete_button = ImageTk.PhotoImage(image)
        label = Label(image=delete_button)
        label.image=delete_button
        button = Button(button_frame,image=delete_button,bd = 0, command = lambda : self.check_title(search_entry.get()), borderwidth=0)
        button.pack(pady=(0, 15))
        """

        #Add return button
        self.add_return_button()

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
        title_frame.pack(pady=(40,20))
        title_label = Label(title_frame,text = "Title: ", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        title_label.grid(row = 0, column = 0)
        title_entry = Entry(title_frame, width = 100)
        title_entry.insert(0, book.get_title())
        title_entry.grid(row = 0, column = 1)

        #Add Label and input for rating.
        rating_frame = Frame(self.canvas)
        rating_frame.pack(pady=(0,20))
        rating_label = Label(rating_frame,text = "Rating:", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        rating_label.grid(row = 0, column = 0)
        rating_entry = Entry(rating_frame,width = 97)
        rating_entry.insert(0, book.get_rating())
        rating_entry.grid(row = 0, column = 1)

        #Add Label and input for genre.
        genre_frame = Frame(self.canvas)
        genre_frame.pack(pady=(0,20))
        genre_label = Label(genre_frame,text = "Genre:", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        genre_label.grid(row = 0, column = 0)
        genre_entry = Entry(genre_frame, width = 98)
        genre_entry.insert(0, book.get_genre())
        genre_entry.grid(row = 0, column = 1)

        #Add Label and input for description.
        desc_frame = Frame(self.canvas, bg = "#4487b8")
        desc_frame.pack(pady=(0,20))
        desc_label = Label(desc_frame,text = "Description:", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        desc_label.grid(row = 0, column = 0)
        desc_entry = Text(desc_frame, width = 68, height = 3)
        desc_entry.insert(END, book.get_desc())
        desc_entry.grid(row = 0, column = 1)

        #Add Label and input for review.
        review_frame = Frame(self.canvas, bg = "#4487b8")
        review_frame.pack()
        review_label = Label(review_frame,text = "Review:      ", font=("Helvetica", "16"), bg = "#4487b8",fg="white")
        review_label.grid(row = 0, column = 0)
        review_entry = Text(review_frame, width = 68, height = 10)
        review_entry.insert(END, book.get_review())
        review_entry.grid(row = 0, column = 1)
        
        """
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
        review_entry.grid(row = 0, column = 1)"""

        #Button to edit a book.
        image = PhotoImage(file="images/edit_book_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        add_b = self.canvas.create_image(self.width/2,self.height-120, image=image)
        self.canvas.tag_bind(add_b, "<Button-1>", lambda e: self.edit_page_confirmation(e,
                                                                                       book_id,
                                                                                      title_entry.get(),
                                                                                      rating_entry.get(),
                                                                                      genre_entry.get(),
                                                                                      desc_entry.get('1.0',END),
                                                                                      review_entry.get('1.0',END)))
        """
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/edit_book_button.png")
        edit_button = ImageTk.PhotoImage(image)
        label = Label(image=edit_button)
        label.image=edit_button
        button = Button(button_frame,image=edit_button,bd = 0, command = lambda : self.edit_page_confirmation(book_id,
                                                                                                       title_entry.get(),
                                                                                                       rating_entry.get(),
                                                                                                       genre_entry.get(),
                                                                                                       desc_entry.get(),
                                                                                                       review_entry.get()))
        button.pack(pady=(0, 15))
        """

    def edit_page_confirmation(self,e,book_id,title,rating,genre,desc,review):
        """
        This function will edit a book that is in the databse

        Parameters
        -----------------
        e : Event
            This is an event that occurs when a button is pressed.
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
        l = Label(self.canvas,text="Book has been successfully editted!", font=("Helvetica", "16", "bold"),bg="#4487b8",fg="white")
        l.place(x=self.width/2-160,y=self.height/2)
        
        #Add the return button and updated label.
        self.add_return_button()

        
    def check_title(self,e,title):
        """
        This function will check if a book with a title is in the database.

        Parameters
        ----------------
        e : Event
            This is an event that occurs when a button is pressed.
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


    def check_all_details(self,event,title,rating,genre,desc,review):
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
        if rating == "" or rating.isnumeric() == False:
            valid = False
            print("wad")
            print(rating.isnumeric())
        if genre == "":
            valid = False
        if desc == "":
            valid = False
        if review == "":
            valid = False
        #If all is valid, then add the book to the database.
        if valid:
            from main import new_book
            new_book(title,rating,genre,desc,review)
            self.add_confirmation_page()


    def add_return_button(self):
        """
        This function will add the return button for the confirmation pages.
        """
        #Return Button
        image = PhotoImage(file="images/return_button.png")
        label = Label(image=image) #Prevents garbage collection
        label.image=image #Prevents garbage collection
        return_button = self.canvas.create_image(self.width/2,self.height-50, image=image)
        self.canvas.tag_bind(return_button, "<Button-1>", self.home_page)

        """
        button_frame = Frame(self.canvas)
        button_frame.pack()
        image = Image.open("images/return_button.png")
        return_button = ImageTk.PhotoImage(image)
        label = Label(image=return_button)
        label.image=return_button
        button = Button(button_frame,image=return_button,bd = 0, command = self.home_page)
        button.pack(pady=(0, 15))
        """
    
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
