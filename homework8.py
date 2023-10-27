"""
The application displays a list of seasonal months. The choice of season is set by the user.
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
    def __init__(self):
        self.__months = ['December', 'January', 'February']
        super().__init__("Winter")
    
    def print_months(self):
        super().print_months(self.__months)


class Spring(Season):
    def __init__(self):
        self.__months = ['March', 'April', 'May']
        super().__init__("Spring")
        
    def print_months(self):
        super().print_months(self.__months)


class Summer(Season):
    def __init__(self):
        self.__months = ['June', 'July', 'August']
        super().__init__("Summer")
    
    def print_months(self):
        if not isinstance(self.__months, list):
            raise TypeError("months should be a list")
        months_upper = tuple(map(str.upper, self.__months))
        print(months_upper)


class Autumn(Season):
    def __init__(self):
        self.__months = ['September', 'October', 'November']
        super().__init__("Autumn")
        
    def print_months(self):
        super().print_months(self.__months)
        

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
