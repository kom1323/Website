from abc import ABC, abstractmethod



class IDataBase(ABC):

    def __init__(self) -> None:
        super().__init__()


    @abstractmethod
    def get_first_row(self) -> dict:
        pass

    @abstractmethod
    def get_word(self) -> str:
        pass

    @abstractmethod
    def insert_word(self, word: str) -> bool:
        pass

    @abstractmethod
    def get_full_table(self) -> dict:
        pass