from typing import Callable

class CountTarget():

    def __init__(self) -> None:
        self.__allocated_num = 0
        self.__win_num = 0
        self.__lose_num = 0
    
    @property
    def allocated_num(self) -> int:
        return self.__allocated_num
    
    @property
    def win_num(self) -> int:
        return self.__win_num
    
    @property
    def lose_num(self) -> int:
        return self.__lose_num
    
    def check_set_integer(func:Callable):

        def _wrapper(self, value):

            if type(value) != int:
                print(func.__name__ + " value allow only int")
                return
            
            return func(self,value)
        
        return _wrapper
    
    def check_set_zero(func:Callable):

        def _wrapper(self, value):

            if value != 0:
                print(func.__name__ + " value allow only 0")
                return
            
            return func(self,value)
        
        return _wrapper
    
    @allocated_num.setter
    @check_set_integer
    @check_set_zero
    def allocated_num(self, value:int) -> None:
        self.__allocated_num = value
    
    @win_num.setter
    @check_set_integer
    @check_set_zero
    def win_num(self, value:int) -> None:
        self.__win_num = value
    
    @lose_num.setter
    @check_set_integer
    @check_set_zero
    def lose_num(self, value:int) -> None:
        self.__lose_num = value
    
    def allocated_num_increment(self) -> None:
        self.__allocated_num += 1
    
    def win_num_increment(self) -> None:
        self.__win_num += 1
    
    def lose_num_increment(self) -> None:
        self.__lose_num += 1
