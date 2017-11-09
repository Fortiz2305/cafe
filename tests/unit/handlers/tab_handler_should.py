from expects import expect, be_a, have_properties, raise_error, contain_exactly
from doublex import Spy, Stub, ANY_ARG
from doublex_expects import have_been_called_with

from tests.mamba_reserved_words import before, context, description, it, self

from commands.commands import (
    OpenTab,
    PlaceOrder
)
from domain_events.events import (
    TabOpened,
    DrinksOrdered
)
from handlers.tab_handler import TabHandler
from domain.exceptions import TabNotOpen
from domain.drink import Drink


with description('Tab Handler'):
    with context('When Opening a Tab'):
        with before.each:
            self.test_id = 'an_irrelevant_id'
            self.test_table_number = 10
            self.test_waiter = 'an_irrelevant_waiter'
            self.event_publisher = Spy()
            self.tab_handler = TabHandler(self.event_publisher, Stub())

        with it('should publish "TabOpened" event when handling an "OpenTab" command'):
            open_tab_command = OpenTab(
                tab_id=self.test_id,
                table_number=self.test_table_number,
                waiter=self.test_waiter)

            self.tab_handler.handle(open_tab_command)

            expect(self.event_publisher.publish).to(have_been_called_with(be_a(TabOpened)))
            expect(self.event_publisher.publish).to(have_been_called_with(have_properties({
                'tab_id': self.test_id,
                'table_number': self.test_table_number,
                'waiter': self.test_waiter
            })))

    with context('When placing Orders'):
        with before.each:
            self.test_id = 'an_irrelevant_id'
            self.repository = Stub()
            self.event_publisher = Spy()
            self.tab_handler = TabHandler(self.event_publisher, self.repository)

        with it('Cannot place an order if the tab is not open'):
            with Stub() as repository:
                repository.get_events_by_id(ANY_ARG).returns([])
            self.tab_handler.repository = repository
            place_order_command = PlaceOrder(
                tab_id=self.test_id,
                items_list=['an_irrelevant_item'])

            expect(lambda: self.tab_handler.handle(place_order_command)).to(raise_error(TabNotOpen))

        with it('Should publish "DrinksOrdered" event when receiving and order with only drinks'):
            with Stub() as repository:
                repository.get_events_by_id(ANY_ARG).returns([
                    TabOpened(self.test_id, 'an_irrelevant_number', 'an_irrelevant_waiter')
                ])
            self.tab_handler.repository = repository
            place_order_command = PlaceOrder(
                tab_id=self.test_id,
                items_list=[Drink('an_irrelevant_drink'), Drink('an_irrelevant_drink')]
            )

            self.tab_handler.handle(place_order_command)

            expect(self.event_publisher.publish).to(have_been_called_with(be_a(DrinksOrdered)))
            expect(self.event_publisher.publish).to(have_been_called_with(have_properties({
                'tab_id': self.test_id,
                'drinks_list': contain_exactly(be_a(Drink), be_a(Drink))
            })))
