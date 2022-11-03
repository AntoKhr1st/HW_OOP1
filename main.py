from Shop import Shop
from courier import Courier
from errors import BaseError, NotEnoughProductError, WrongProductError, NotEnoughSpaceError, InvalidRequestError
from request import Request
from store import Store

store = Store(items={
    'картошка': 10,
    'печенька': 10,
},
    capacity=100,
)

shop = Shop(items={
    'печенька': 5,
},
    capacity=20)

storages = {
    'склад': store,
    'магазин': shop,

}


def main():
    print('добрый день!')
    while True:
        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится:\n{storage.get_items()}')

        raw_request = input('введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
                            'stop или стоп для завершения:\n')
        if raw_request in ['stop', 'стоп']:
            return
        try:
            request = Request(request=raw_request, storages=storages)
        except BaseError as error:
            print(error.massage)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        # except NotEnoughSpaceError as error:
        #     print(error.massage)
        #     courier.cancel()
        #     continue
        # except NotEnoughProductError or WrongProductError or InvalidRequestError as error:
        #     print(error.massage)
        #     continue
        except BaseError as error:
            if error == NotEnoughSpaceError:
                print(error.massage)
                courier.cancel()
                continue
            else:
                print(error.massage)
                continue

if __name__ == '__main__':
    main()
