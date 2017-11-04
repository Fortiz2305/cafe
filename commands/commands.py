from commands.command_types import (
    OPEN_TAB,
    PLACE_ORDER
)


class OpenTab:
    def __init__(self, tab_id, table_number, waiter):
        self.id = tab_id
        self.table_number = table_number
        self.waiter = waiter
        self.type = OPEN_TAB


class PlaceOrder:
    def __init__(self, tab_id, items_list):
        self.id = tab_id
        self.items_list = items_list
        self.type = PLACE_ORDER
