from base_storage import BaseStorage
from errors import ToManyDifferentProductError


class Shop(BaseStorage):
    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise ToManyDifferentProductError
        super().add(name, amount)
