class Event:
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                 event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.event_name}.")
        else:
            print("Not enough available seats.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")

    def display_event_details(self):
        print("Event Details:")
        print("Name:", self.event_name)
        print("Date:", self.event_date)
        print("Time:", self.event_time)
        print("Venue:", self.venue_name)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("Ticket Price:", self.ticket_price)
        print("Event Type:", self.event_type)


class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                 event_type, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                         event_type)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print("Genre:", self.genre)
        print("Actor:", self.actor_name)
        print("Actress:", self.actress_name)


class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                 event_type, artist, music_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                         event_type)
        self.artist = artist
        self.music_type = music_type

    def display_event_details(self):
        super().display_event_details()
        print("Artist:", self.artist)
        print("Music Type:", self.music_type)


class Sports(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                 event_type, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                         event_type)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print("Sport Name:", self.sport_name)
        print("Teams:", self.teams_name)


# Example Usage:
if __name__ == "__main__":
    # Creating instances of subclasses
    movie = Movie("The Avengers", "2024-05-15", "18:00", "Grand Theater", 100, 100, 10.00, "Movie", "Action",
                  "Robert Downey Jr.", "Scarlett Johansson")
    concert = Concert("Live Concert", "2024-05-20", "20:00", "City Stadium", 200, 200, 50.00, "Concert", "Ed Sheeran",
                      "Pop")
    sports = Sports("Football Match", "2024-06-01", "15:00", "National Stadium", 50000, 50000, 20.00, "Sports",
                    "Football", "Real Madrid vs Barcelona")

    # Display details of different events
    movie.display_event_details()
    print("\n")
    concert.display_event_details()
    print("\n")
    sports.display_event_details()
