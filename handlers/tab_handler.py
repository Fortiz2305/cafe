class TabHandler:
    def __init__(self, event_publisher, repository):
        self.event_publisher = event_publisher
        self.repository = repository

    def handle_open_tab(self, command):
        tab = self.repository.get_tab_by_id(tab_id=command.id)
        tab.open_tab(table_number=command.table_number, waiter=command.waiter)
        self.send_uncommited_events(tab)

    def send_uncommited_events(self, tab):
        for event in tab.uncommited_events:
            self.event_publisher.publish(event)
