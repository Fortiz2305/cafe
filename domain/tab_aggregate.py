from domain_events.events import TabOpened, DrinksOrdered
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
        if not self._opened:
            raise TabNotOpen('Tab should be opened before place an order')
        drinks_ordered_event = DrinksOrdered(
            tab_id=self._tab_id,
            drinks_list=items_list)
        self.uncommited_events.append(drinks_ordered_event)

    @staticmethod
    def apply(events):
        tab = TabAggregate()
        for event in events:
            tab.apply_tab_opened_event(event)
        return tab

    def apply_tab_opened_event(self, tab_opened_event):
        self._tab_id = tab_opened_event.tab_id
        self._opened = True
