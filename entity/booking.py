from datetime import datetime

class Booking:
    booking_counter = 0  # Class variable to track booking IDs

    def __init__(self, customers, event, num_tickets, total_cost):
        Booking.booking_counter += 1
        self.booking_id = Booking.booking_counter
        self.customers = customers
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = total_cost
        self.booking_date = datetime.now()

    # Getter and Setter methods
    def get_booking_id(self):
        return self.booking_id

    def get_customers(self):
        return self.customers

    def set_customers(self, customers):
        self.customers = customers

    def get_event(self):
        return self.event

    def set_event(self, event):
        self.event = event

    def get_num_tickets(self):
        return self.num_tickets

    def set_num_tickets(self, num_tickets):
        self.num_tickets = num_tickets

    def get_total_cost(self):
        return self.total_cost

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    def get_booking_date(self):
        return self.booking_date

    def set_booking_date(self, booking_date):
        self.booking_date = booking_date

    # Method to display booking details
    def display_booking_details(self):
        print("Booking Details:")
        print(f"Booking ID: {self.booking_id}")
        print("Customers:")
        for customer in self.customers:
            print(f"  Name: {customer.get_customer_name()}, Email: {customer.get_email()}, Phone Number: {customer.get_phone_number()}")
        print("Event Details:")
        self.event.display_event_details()
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Total Cost: {self.total_cost}")
        print(f"Booking Date: {self.booking_date.strftime('%Y-%m-%d %H:%M:%S')}")
