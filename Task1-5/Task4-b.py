class Venue:
    def __init__(self, venue_name, address):
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print("Venue Details:")
        print("Name:", self.venue_name)
        print("Address:", self.address)


# Example Usage:
if __name__ == "__main__":
    # Creating a Venue object
    venue = Venue("Grand Theater", "123 Main Street, Cityville")

    # Display venue details
    venue.display_venue_details()
