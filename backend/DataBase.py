from IDB import IDataBase
import pandas as pd

class DataBase(IDataBase):

    def __init__(self, file_path: str) -> None:

        self.df = pd.read_csv(file_path)
        super().__init__()

    
    def get_first_row(self) -> dict:
        return self.df.iloc[0].to_dict()

    def get_word(self) -> str:
        pass

    def insert_word(self, word: str) -> bool:
        pass
   
    def get_full_table(self) -> dict:
        return self.df.to_dict()