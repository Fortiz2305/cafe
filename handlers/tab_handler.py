from domain.tab_aggregate import TabAggregate
from commands.command_types import (
    OPEN_TAB,
    PLACE_ORDER
)


class TabHandler:
    def __init__(self, event_publisher, repository):
        self.event_publisher = event_publisher
        self.repository = repository
        self._command_process_map = {
            OPEN_TAB: self._handle_open_tab,
            PLACE_ORDER: self._handle_place_order
        }

    def handle(self, command):
        self._command_process_map.get(command.type, self._do_nothing)(command)

    def _do_nothing(self, event):
        pass

    def _handle_open_tab(self, open_tab_command):
        tab = TabAggregate(tab_id=open_tab_command.id)
        tab.open_tab(table_number=open_tab_command.table_number, waiter=open_tab_command.waiter)
        self.send_uncommited_events(tab)

    def _handle_place_order(self, place_order_command):
        tab = self.repository.get_tab_by_id(place_order_command.id)
        tab.place_order(items_list=place_order_command.items_list)

    def send_uncommited_events(self, tab):
        for event in tab.uncommited_events:
            self.event_publisher.publish(event)
