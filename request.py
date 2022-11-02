from errors import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, request: str, storages):
        split_request = request.strip().lower().split(' ')
        if len(split_request) != 7:
            raise InvalidRequestError
        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise UnknownStorageError
