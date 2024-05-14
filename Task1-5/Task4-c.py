class Customer:
    def __init__(self, customer_name, email, phone_number):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print("Customer Details:")
        print("Name:", self.customer_name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)


# Example Usage:
if __name__ == "__main__":
    # Creating a Customer object
    customer = Customer("sakshi patil", "sakshi@gmail.com", "123-456-7890")

    # Display customer details
    customer.display_customer_details()
