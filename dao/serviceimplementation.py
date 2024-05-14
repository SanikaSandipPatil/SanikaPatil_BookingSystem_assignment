import sqlite3
from typing import List
from abc import ABC, abstractmethod
from entity.event import Event
from entity.venue import Venue
from entity.customer import Customer
from entity.booking import Booking


class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: Venue) -> Event:
        try:
            cursor = self.db_conn.cursor()
            cursor.execute('''INSERT INTO events (event_name, event_date, event_time, venue_name, venue_address, total_seats, available_seats, ticket_price, event_type)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (event_name, date, time, venue.venue_name, venue.address, total_seats, total_seats, ticket_price, event_type))
            self.db_conn.commit()
            event_id = cursor.lastrowid
            cursor.close()
            return Event(event_id, event_name, date, time, venue, total_seats, total_seats, ticket_price, event_type)
        except sqlite3.Error as e:
            print("Error creating event:", e)

    def get_event_details(self) -> List[Event]:
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM events")
            events = []
            for row in cursor.fetchall():
                event_id, event_name, date, time, venue_name, venue_address, total_seats, available_seats, ticket_price, event_type = row
                venue = Venue(venue_name, venue_address)
                event = Event(event_id, event_name, date, time, venue, total_seats, available_seats, ticket_price, event_type)
                events.append(event)
            cursor.close()
            return events
        except sqlite3.Error as e:
            print("Error fetching event details:", e)

    def get_available_no_of_tickets(self) -> int:
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT SUM(available_seats) FROM events")
            available_seats = cursor.fetchone()[0]
            cursor.close()
            return available_seats if available_seats else 0
        except sqlite3.Error as e:
            print("Error fetching available seats:", e)

    def calculate_booking_cost(self, num_tickets: int):
        # Assuming ticket price is same for all events
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT ticket_price FROM events LIMIT 1")
            ticket_price = cursor.fetchone()[0]
            total_cost = num_tickets * ticket_price
            cursor.close()
            return total_cost
        except sqlite3.Error as e:
            print("Error calculating booking cost:", e)

    def book_tickets(self, event_name: str, num_tickets: int, list_of_customer: List[Customer]):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT event_id, available_seats FROM events WHERE event_name=?", (event_name,))
            event_id, available_seats = cursor.fetchone()
            if available_seats < num_tickets:
                print("Insufficient seats available.")
                return
            cursor.execute("UPDATE events SET available_seats=available_seats-? WHERE event_id=?",
                           (num_tickets, event_id))
            booking_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for customer in list_of_customer:
                cursor.execute("INSERT INTO customers (customer_name, email, phone_number) VALUES (?, ?, ?)",
                               (customer.customer_name, customer.email, customer.phone_number))
                customer_id = cursor.lastrowid
                cursor.execute(
                    "INSERT INTO bookings (event_id, customer_id, num_tickets, total_cost, booking_date) VALUES (?, ?, ?, ?, ?)",
                    (event_id, customer_id, num_tickets, self.calculate_booking_cost(num_tickets), booking_date))
            self.db_conn.commit()
            print("Tickets booked successfully.")
        except sqlite3.Error as e:
            self.db_conn.rollback()
            print("Error booking tickets:", e)
        finally:
            cursor.close()

    def cancel_booking(self, booking_id: int):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT event_id, num_tickets FROM bookings WHERE booking_id=?", (booking_id,))
            result = cursor.fetchone()
            if not result:
                print("Booking not found.")
                return False
            event_id, num_tickets = result
            cursor.execute("UPDATE events SET available_seats=available_seats+? WHERE event_id=?",
                           (num_tickets, event_id))
            cursor.execute("DELETE FROM bookings WHERE booking_id=?", (booking_id,))
            self.db_conn.commit()
            print("Booking canceled successfully.")
            return True
        except sqlite3.Error as e:
            self.db_conn.rollback()
            print("Error canceling booking:", e)
        finally:
            cursor.close()

    def get_booking_details(self, booking_id: int):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute('''SELECT bookings.booking_id, events.event_name, customers.customer_name, customers.email, customers.phone_number,
                                 bookings.num_tickets, bookings.total_cost, bookings.booking_date
                                 FROM bookings
                                 JOIN events ON bookings.event_id = events.event_id
                                 JOIN customers ON bookings.customer_id = customers.customer_id
                                 WHERE bookings.booking_id=?''', (booking_id,))
            booking_details = cursor.fetchone()
            if booking_details:
                print("Booking Details:")
                booking_id, event_name, customer_name, email, phone_number, num_tickets, total_cost, booking_date = booking_details
                print(f"Booking ID: {booking_id}")
                print(f"Event Name: {event_name}")
                print(f"Customer Name: {customer_name}")
                print(f"Email: {email}")
                print(f"Phone Number: {phone_number}")
                print(f"Number of Tickets: {num_tickets}")
                print(f"Total Cost: {total_cost}")
                print(f"Booking Date: {booking_date}")
            else:
                print("Booking not found.")
        except sqlite3.Error as e:
            print("Error fetching booking details:", e)
        finally:
            cursor.close()
