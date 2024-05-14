from .event import Event

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price):
        super().__init__(event_name, event_date, event_time, venue, total_seats, ticket_price, "Movie")
