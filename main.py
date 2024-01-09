import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """book hotel by changing in data to not available = 'NO' """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel avaailable or no"""
        availablity = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availablity == "yes":
            return True
        else:
            return False

        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_objects):
        pass

    def generate(self):
        pass


print(df)
hotel_id = input("Enter a hotel id number: ")
hotel = Hotel(hotel_id)


if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free!")

