#Imports
import sqlite3

class DBController():
    """
    This class deals with requests to the database.

    Methods
    -----------
    __init__ - Creates a connection the the database
    execute(command) - Executes a given command (String) on the database.
    commit - Commits any changes to the database.
    close - Closes the connection to the database.
    """

    def __init__(self):
        #Create a connection to the database.
        self.con = sqlite3.conn('books.db', check_same_thread=False)
        self.cur = self.con.cursor()


    def execute(self,command):
        """
        This method will execute a command on the database.

        Parameters
        ------------------
        command : str
            This is a string of the command that will be executed.

        Return
        ------------------
        sqlite3.Cursor object - Can be iterated through to get each row retrieved back.
        """
        return self.cur.execute(command)
        

    def commit(self):
        """
        This method will commit (update) any changes made to the database.
        """
        self.con.commit()


    def close(self):
        """
        This method will close the connection to the database.
        """
        self.commit()
        self.con.close()
