# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.


class Device:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def get_info(self) -> str:
        return f'brand = {self.__brand}\tmodel = {self.__model}\tprice = {self.__price}'


class Laptop(Device):
    def __init__(self,brand, model, price,ram, storage):
        super().__init__(brand, model, price)
        self.__ram = ram
        self.__storage = storage

    def get_info(self) -> str:
        return super().get_info() + f'\tram = {self.__ram}\tstorage = {self.__storage}'

class Smartphone(Device):
    def __init__(self, brand, model, price, camera_megapixels, battery_capacity):
        super().__init__(brand, model, price)
        self.__camera_megapixels = camera_megapixels
        self.__battery_capacity = battery_capacity

    def get_info(self) -> str:
        return super().get_info() + f'\tcamera_megapixels = {self.__camera_megapixels}\tbattery_capacity = {self.__battery_capacity}'


class Store:
    def __init__(self):
        self.__list_devices = []

    def add_device(self, device):
        if isinstance(device, Device):
            self.__list_devices.append(device)
        else:
            print("неизвестное устройство")

    def list_devices(self):
        for item in self.__list_devices:
            print(item.get_info())


if __name__ == '__main__':
    dev = Device("brand", "model", "price")
    lap = Laptop("brand", "model", "price","ram", "storage")
    smrt =Smartphone("brand", "model", "price", "camera_megapixels", "battery_capacity")
    s = "str"

    store = Store()
    store.add_device(dev)
    store.add_device(lap)
    store.add_device(smrt)
    store.add_device(s)
    print("store содержит:")
    store.list_devices()