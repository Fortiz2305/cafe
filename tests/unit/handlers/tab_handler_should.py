from expects import expect, be_a, have_properties
from doublex import Spy, ANY_ARG
from doublex_expects import have_been_called_with

from tests.mamba_reserved_words import before, context, description, it, self

from commands.open_tab import OpenTab
from domain_events.tab_opened import TabOpened
from handlers.tab_handler import TabHandler
from domain.tab_aggregate import TabAggregate


with description('Tab Handler'):
    with context('When Opening a Tab'):
        with before.each:
            self.test_id = 'an_irrelevant_id'
            self.test_table_number = 10
            self.test_waiter = 'an_irrelevant_waiter'
            self.event_publisher = Spy()
            self.repository = Spy()
            self.handler = TabHandler(self.event_publisher, self.repository)

        with it('should add "TabOpened" event to event list when sending a "OpenTab" command'):
            with Spy() as repository:
                repository.get_tab_by_id(ANY_ARG).returns(TabAggregate(self.test_id))
            self.handler.repository = repository
            open_tab_command = OpenTab(
                tab_id=self.test_id,
                table_number=self.test_table_number,
                waiter=self.test_waiter)

            self.handler.handle_open_tab(open_tab_command)

            expect(self.event_publisher.publish).to(have_been_called_with(be_a(TabOpened)))
            expect(self.event_publisher.publish).to(have_been_called_with(have_properties({
                'id': self.test_id,
                'table_number': self.test_table_number,
                'waiter': self.test_waiter
            })))
