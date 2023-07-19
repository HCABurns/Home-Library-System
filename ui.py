#Imports
from tkinter import *
from db_controller import DBController


class UI():

    def __init__(self):
        self.root = Tk()
        self.width = 800
        self.height =600
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.root.title("Home Library System")






if __name__ == "__main__":
    ui = UI()
    ui.root.mainloop()
