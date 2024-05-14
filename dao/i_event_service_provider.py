from abc import ABC, abstractmethod
from entity.event import Event
from entity.venue import Venue

class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                    event_type: str, venue: Venue) -> Event:
        pass

    @abstractmethod
    def get_event_details(self) -> list:
        pass

    @abstractmethod
    def get_available_no_of_tickets(self) -> int:
        pass
