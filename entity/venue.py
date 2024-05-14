class Venue:
    def __init__(self, venue_name, address):
        self._venue_name = venue_name
        self._address = address

    def get_venue_name(self):
        return self._venue_name

    def set_venue_name(self, venue_name):
        self._venue_name = venue_name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def display_venue_details(self):
        print("Venue Details:")
        print(f"Name: {self._venue_name}")
        print(f"Address: {self._address}")


