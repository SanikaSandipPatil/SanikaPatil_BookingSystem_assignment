from datetime import datetime
from entity.event import Event
from entity.venue import Venue
from entity.movie import Movie
from entity.concert import Concert
from entity.sport import Sport
from entity.customer import Customer
from entity.booking import Booking

if __name__ == "__main__":
    # Example usage of Event and Venue classes
    venue = Venue("ABC Theater", "123 Main Street")
    event_date = datetime(2024, 5, 15)
    event_time = datetime.strptime("18:30", "%H:%M")
    event = Event("Movie Night", event_date, event_time, venue, 100, 10.00, "Movie")
    event.book_tickets(5)
    event.display_event_details()
    print("Total Revenue:", event.calculate_total_revenue())
    print("------------------------")
    venue.display_venue_details()

    print("______________movie,concert,sport subclass implementation___________________")
    # Example usage of Event and its subclasses
    venue = Venue("ABC Theater", "123 Main Street")
    event_date = datetime(2024, 5, 15)
    event_time = datetime.strptime("18:30", "%H:%M")

    # Create instances of different event types
    movie_event = Movie("Movie Night", event_date, event_time, venue, 100, 10.00)
    concert_event = Concert("Concert Night", event_date, event_time, venue, 200, 20.00)
    sport_event = Sport("Sport Event", event_date, event_time, venue, 150, 15.00)

    # Display event details
    movie_event.display_event_details()
    print("Total Revenue:", movie_event.calculate_total_revenue())
    concert_event.display_event_details()
    print("Total Revenue:", concert_event.calculate_total_revenue())
    sport_event.display_event_details()
    print("Total Revenue:", sport_event.calculate_total_revenue())

    print("----------customer class example usage------------------")

    # Example usage of Customer class
    customer = Customer("John Doe", "john@example.com", "+1234567890")
    customer.display_customer_details()

    print("_________ Example usage of Booking class________________________")

    # Example usage of Booking class
    venue = Venue("ABC Theater", "123 Main Street")
    event_date = datetime(2024, 5, 15)
    event_time = datetime.strptime("18:30", "%H:%M")
    event = Event("Movie Night", event_date, event_time, venue, 100, 10.00, "Movie")

    customer1 = Customer("John Doe", "john@example.com", "+1234567890")
    customer2 = Customer("Jane Smith", "jane@example.com", "+9876543210")

    customers = [customer1, customer2]

    booking = Booking(customers, event, 2, 20.00)
    booking.display_booking_details()