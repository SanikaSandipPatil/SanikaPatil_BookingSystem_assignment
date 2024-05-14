from abc import ABC, abstractmethod
from entity.booking import Booking
from entity.customer import Customer

class IBookingSystemServiceProvider(ABC):
    @abstractmethod
    def calculate_booking_cost(self, num_tickets: int) -> float:
        pass

    @abstractmethod
    def book_tickets(self, event_name: str, num_tickets: int, customers: list) -> Booking:
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int) -> bool:
        pass

    @abstractmethod
    def get_booking_details(self, booking_id: int) -> Booking:
        pass
