# util/property_util.py

class PropertyUtil:
    @staticmethod
    def get_property_string():
        hostname = 'localhost'
        dbname = 'ticket_booking_system'
        username = 'root'
        password = 'sanika'
        port = 3306

        connection_string = f"host={hostname} dbname={dbname} user={username} password={password} port={port}"
        return connection_string
