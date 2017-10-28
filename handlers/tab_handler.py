from domain.tab_aggregate import TabAggregate


class TabHandler:
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher

    def handle_open_tab(self, open_tab_command):
        tab = TabAggregate(tab_id=open_tab_command.id)
        tab.open_tab(table_number=open_tab_command.table_number, waiter=open_tab_command.waiter)
        self.send_uncommited_events(tab)

    def handle_place_order(self, place_order_command):
        pass

    def send_uncommited_events(self, tab):
        for event in tab.uncommited_events:
            self.event_publisher.publish(event)
