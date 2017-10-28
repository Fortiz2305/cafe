from domain.tab_aggregate import TabAggregate


class TabHandler:
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher

    def handle_open_tab(self, command):
        tab = TabAggregate(tab_id=command.id)
        tab.open_tab(table_number=command.table_number, waiter=command.waiter)
        self.send_uncommited_events(tab)

    def send_uncommited_events(self, tab):
        for event in tab.uncommited_events:
            self.event_publisher.publish(event)
