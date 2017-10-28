from domain_events.events import TabOpened
from domain.exceptions import TabNotOpen


class TabAggregate:
    def __init__(self, tab_id):
        self.id = tab_id
        self.uncommited_events = []

    def open_tab(self, table_number, waiter):
        tab_opened_event = TabOpened(
            tab_id=self.id,
            table_number=table_number,
            waiter=waiter)
        self.uncommited_events.append(tab_opened_event)

    def place_order(self, items_list):
        raise TabNotOpen('Tab should be opened before place an order')
