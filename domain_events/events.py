class TabOpened:
    def __init__(self, tab_id, table_number, waiter):
        self.id = tab_id
        self.table_number = table_number
        self.waiter = waiter


class DrinksOrdered:
    def __init__(self, tab_id, drinks_list):
        self.id = tab_id
        self.drinks_list = drinks_list


class FoodOrdered:
    def __init__(self, tab_id, food_list):
        self.id = tab_id
        self.food_list = food_list
