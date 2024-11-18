# Создайте класс Vehicle, представляющий транспортное средство.
# Этот класс должен содержать:

# Поля make, model и year.
# Метод get_info, возвращающий строку с информацией о транспортном средстве.

# Затем создайте подклассы Car и Motorcycle, которые расширяют класс Vehicle:
# Класс Car должен иметь поле number_of_doors и метод get_info,
# который добавляет информацию о количестве дверей.
# Класс Motorcycle должен иметь поле has_sidecar (True или False)
# и метод get_info, который указывает, есть ли у мотоцикла коляска.

class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_info(self) -> str:
        return f'make = {self.__make}, model = {self.__model}, year = {self.__year}'


class Car(Vehicle):
    def __init__(self, make, model, year,number_of_doors ):
        super().__init__(make, model, year)
        self.__number_of_doors = number_of_doors

    def get_info(self):
        return super().get_info() + f' number_of_doors = {self.__number_of_doors}'

class  Motorcycle(Vehicle):
    def __init__(self,make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.__has_sidecar = has_sidecar

    def get_info(self):
        return super().get_info() + f'has_sidecar is {self.__has_sidecar} '
