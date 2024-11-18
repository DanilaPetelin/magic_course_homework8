# Создайте класс Employee, который инкапсулирует следующие данные:

# Приватные поля __name, __position, __salary.
# Методы set_name, set_position и set_salary для изменения значений
# этих полей (например, при повышении сотрудника).
# Ограничьте прямой доступ к __salary, добавив проверку,
# чтобы зарплату можно было изменить только через метод, например,
# при повышении. Запрещается устанавливать зарплату ниже текущего значения.

# Метод get_employee_info, который возвращает информацию о сотруднике в
# виде строки.

class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def __compare_position(self, other_position):
        sorted_positions = ["worker", "manager", "director", "owner"]
        index_other = -1
        if other_position in sorted_positions:
            index_other = sorted_positions.index(other_position)
        return sorted_positions.index(self.__position) < index_other

    def set_name(self, name):
        self.__name = name

    def set_position(self, position):
        self.__position = position

    def __set_salary(self, salary):
        self.__salary = salary

    def rise_position(self, new_position, new_salary):
        if self.__compare_position(new_position) and self.__salary <= new_salary:
            self.set_position(new_position)
            self.__set_salary(new_salary)
        else:
            print("повышение невозможно ;( ")

    def get_employee_info(self):
        print(f'name = {self.__name},  position = {self.__position},   salary = {self.__salary}')


if __name__ == '__main__':
    emp = Employee("Ivan", "manager", 10)
    emp.get_employee_info()

    emp.rise_position("manager", 20)
    emp.get_employee_info()

    emp.rise_position("worker", 20)
    emp.get_employee_info()

    emp.rise_position("owner", 10)
    emp.get_employee_info()

    emp.rise_position("director", 10)
    emp.get_employee_info()
