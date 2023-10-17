"""
Приложение выводит список сезонных месяцев. Выбор сезона задает пользователь.
"""


class Season:
    def __init__(self, name):
        self.__name = name
    
    def __str__(self):
        return self.__name
    
    @staticmethod
    def __output_months(months):
        if not isinstance(months, list):
            raise TypeError("months should be a list")
        print(months)
    
    def print_months(self, months=None):
        self.__output_months(months)


class Winter(Season):
    __months = ['December', 'January', 'February']
    
    def __init__(self):
        super().__init__("Winter")
    
    def public_method(self):
        super().public_method(self.__months)


class Spring(Season):
    __months = ['March', 'April', 'May']
    
    def __init__(self):
        super().__init__("Spring")
        
    def public_method(self):
        super().public_method(self.__months)


class Summer(Season):
    __months = ['June', 'July', 'August']
    
    def __init__(self):
        super().__init__("Summer")
    
    def print_months(self):
        if not isinstance(self.__months, list):
            raise TypeError("months should be a list")
        months_upper = tuple(map(str.upper, self.__months))
        print(months_upper)


class Autumn(Season):
    __months = ['September', 'October', 'November']
    
    def __init__(self):
        super().__init__("Autumn")
        
    def public_method(self):
        super().public_method(self.__months)
        

try:
    season = input("Enter a season: ")
    if not season.isalpha():
        raise ValueError("Season should be a string")
    
    if season.lower() == "winter":
        s = Winter()
    elif season.lower() == "spring":
        s = Spring()
    elif season.lower() == "summer":
        s = Summer()
    elif season.lower() == "autumn":
        s = Autumn()
    else:
        raise ValueError("Unknown season")
    
    print(f'{s}:')
    s.print_months()
    
except ValueError as e:
    print(e)
    
except TypeError as e:
    print(e)
