from errors import NotEnoughSpaceError, NotEnoughProductError, WrongProductError


class BaseStorage :
    def __init__(self, items, capacity:int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpaceError
        self.__items[name] = self.__items.get(name, 0) + amount #не уверен что сработает (затестить)

    def remove(self,name: str, amount: int) -> None:
        if amount > self.__items[name]:
            raise NotEnoughProductError
        if name not in self.__items:
            raise WrongProductError
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self ):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
