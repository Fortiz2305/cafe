from domain_events.event_types import (
    TAB_OPENED,
    DRINKS_ORDERED,
    FOOD_ORDERED
)


class TabOpened:
    def __init__(self, tab_id, table_number, waiter):
        self.id = tab_id
        self.table_number = table_number
        self.waiter = waiter
        self.type = TAB_OPENED


class DrinksOrdered:
    def __init__(self, tab_id, drinks_list):
        self.id = tab_id
        self.drinks_list = drinks_list
        self.type = DRINKS_ORDERED


class FoodOrdered:
    def __init__(self, tab_id, food_list):
        self.id = tab_id
        self.food_list = food_list
        self.type = FOOD_ORDERED
