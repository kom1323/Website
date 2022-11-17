import mysql.connector
from IDB import IDataBase
import sys

sys.path.insert(0, r"C:\Users\Omer\OneDrive\Desktop\All Projects\python projects\Website")

from config import my_sql_user, my_sql_pass

database_name = "pets"

class MySQLDataBase(IDataBase):

    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=my_sql_user,
            password=my_sql_pass,
            database=database_name
        )
        
        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SELECT * FROM cats")
        for x in self.mycursor:
            print(type(x))


        super().__init__()

    def get_first_row(self) -> dict:
        pass

    def get_word(self) -> str:
        pass

    def insert_word(self, word: str) -> bool:
        pass

    def get_full_table(self) -> dict:
        pass






db = MySQLDataBase()