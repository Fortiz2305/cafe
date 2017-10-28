from domain_events.tab_opened import TabOpened


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
