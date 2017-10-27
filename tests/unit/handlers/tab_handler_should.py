from expects import expect
from doublex import Spy
from doublex_expects import have_been_called_with

from tests.mamba_reserved_words import before, context, description, it, self

from commands.open_tab import OpenTab
from events.tab_opened import TabOpened
from handlers.tab_handler import TabHandler


with description('Tab Handler'):
    with context('When Opening a Tab'):
        with before.each:
            self.test_id = 'an_irrelevant_id'
            self.test_table_number = 10
            self.test_waiter = 'an_irrelevant_waiter'
            self.event_publisher = Spy()
            self.handler = TabHandler(self.event_publisher)

        with it('should add "TabOpened" event to event list when sending a "OpenTab" command'):
            open_tab_command = OpenTab(
                tab_id=self.test_id,
                table_number=self.test_table_number,
                waiter=self.test_waiter)

            self.handler.handle(open_tab_command)

            expected_event = TabOpened(
                tab_id=self.test_id,
                table_number=self.test_table_number,
                waiter=self.test_waiter)
            expect(self.event_publisher.publish).to(have_been_called_with(expected_event))
