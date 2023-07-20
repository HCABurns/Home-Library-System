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
    edit_page() - Sets the UI for the edit a book page.
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

        #Set the background image
        self.set_background()
         
        #Add logo to the page
        image1 = PhotoImage(file="images/logo2sm.png")
        self.canvas.create_image(self.width/2,150, image=image1)

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
        #Create a frame for the buttons to be placed
        button_frame = Frame(self.canvas,background="")
        button_frame.pack(pady=(270,0))

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
        button = Button(button_frame,image=edit_button,bd = 0, command = self.edit_page, borderwidth=0)
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

        #Set the background again.
        self.set_background()


        #Add Label and input for title

        #Add Label and input for rating

        #Add Label and input for genre

        #Add Label and input for description

        #Add Label and input for review

    def delete_page(self):
        """
        This function will set the screen to be able to delete a book that is in the collection.
        """
        #Remove previous content
        self.clear_window()

        #Add Label and input for title

        pass


    def view_page(self):
        """
        This function will set the screen to be able to view the books that are in the collection.
        """
        #Remove previous content
        self.clear_window()

        #Add books in a scrollable frame
        
        pass


    def edit_page(self):
        """
        This function will set the screen to be able to edit a book that is in the collection.
        """
        #Remove previous content
        self.clear_window()

        #Search bar for the book name

        #Search button
        
        pass


    def clear_window(self):
        """
        This function will destroy everything in the window and leave it empty..
        """
        for widget in self.root.winfo_children():
            widget.destroy()


    
if __name__ == "__main__":
    ui = UI()
