import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id": str})
df_Card = pd.read_csv("cards.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """book hotel by changing in data to not available = 'NO' """
        df.loc[df["id"] == self.hotel_id, "available"] = "yes"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel avaailable or no"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_objects):
        self.customer_name = customer_name
        self.hotel = hotel_objects


    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here aro your booking information:
        Name = {self.customer_name}
        Hotel_name = {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvs, holder):
        card_data = {"number": self.number, "expiration": expiration,
                   "csv": cvs, "holder": holder}
        if card_data in df_Card:
            return True
        else:
            return False



print(df)
hotel_id = input("Enter a hotel id number: ")
hotel = Hotel(hotel_id)


if hotel.available():
    creditcard = CreditCard()
    if creditcard.validate():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_objects=hotel)
        print(reservation_ticket.generate())
    else:
        print("Payment was unsuccessfull: ")
else:
    print("Hotel is not free!")

