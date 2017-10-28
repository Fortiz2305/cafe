from domain.tab_aggregate import TabAggregate


class TabHandler:
    def __init__(self, event_publisher, repository):
        self.event_publisher = event_publisher
        self.repository = repository

    def handle_open_tab(self, open_tab_command):
        tab = TabAggregate(tab_id=open_tab_command.id)
        tab.open_tab(table_number=open_tab_command.table_number, waiter=open_tab_command.waiter)
        self.send_uncommited_events(tab)

    def handle_place_order(self, place_order_command):
        tab = self.repository.get_tab_by_id(place_order_command.id)
        tab.place_order(items_list=place_order_command.items_list)

    def send_uncommited_events(self, tab):
        for event in tab.uncommited_events:
            self.event_publisher.publish(event)
