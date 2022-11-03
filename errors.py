class BaseError(Exception):
    massage = 'что-то пошло не так'


class NotEnoughSpaceError(BaseError):
    massage = 'Недостаточно места'


class NotEnoughProductError(BaseError):
    massage = 'Недостаточно товара'


class ToManyDifferentProductError(BaseError):
    massage = 'товаров слишком много'


class InvalidRequestError(BaseError):
    massage = 'некорректный запрос'


class UnknownStorageError(BaseError):
    massage = 'неизвестный склад'


class WrongProductError(BaseError):
    massage = 'неизвестный продукт'
