from request import Request


class Courier:
    def __init__(self, request: Request, storages):
        self.__request = request

        self.departure = storages[self.__request.departure]
        self.destination = storages[self.__request.destination]

    def move(self):
        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер забирает {self.__request.amount} из {self.__request.departure}")

        print(f"Курьер везет {self.__request.amount} {self.__request.departure}"
              f" со {self.__request.departure} в {self.__request.destination}")

        self.destination.add(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер доставил {self.__request.amount} из {self.__request.destination}")

    def cancel(self):
        self.departure.add(name=self.__request.product, amount=self.__request.amount)
