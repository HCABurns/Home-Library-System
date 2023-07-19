#Imports
from tkinter import *
from db_controller import DBController


class UI():

    def __init__(self):
        #Create a basic window.
        self.root = Tk()
        self.width = 800
        self.height =600
        self.root.geometry("{}x{}".format(self.width, self.height))
        #Change icon and title of the window.
        self.root.title("Home Library System")
        self.root.iconbitmap("images\icon.ico")

        #Add background image
        bg = PhotoImage(file="images/bg.png")
        bg_canvas = Canvas( self.root, width = self.width,height = self.height)
        bg_canvas.pack(fill = "both", expand = True)
        bg_canvas.create_image(0,0, image=bg, anchor = "nw")
        
        #Set the home page.
        self.home_page()
        #Run the mainloop.
        self.root.mainloop()


    def home_page(self):
        """
        This function will add the relevant buttons for the home page.
        """
        pass

if __name__ == "__main__":
    ui = UI()
