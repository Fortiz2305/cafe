from domain_events.events import TabOpened
from domain.exceptions import TabNotOpen


class TabAggregate:
    def __init__(self):
        self._opened = False
        self.uncommited_events = []

    def open(self, tab_id, table_number, waiter):
        tab_opened_event = TabOpened(
            tab_id=tab_id,
            table_number=table_number,
            waiter=waiter)
        self.uncommited_events.append(tab_opened_event)

    def place_order(self, items_list):
        raise TabNotOpen('Tab should be opened before place an order')

    @staticmethod
    def apply(events):
        tab = TabAggregate()
        tab.apply_tab_opened_event()
        return tab

    def apply_tab_opened_event(self):
        self._opened = True
