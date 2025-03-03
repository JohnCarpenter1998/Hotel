from hotel import Hotel

hotel = Hotel("Holiday Inn","16 Wolf Road", 3, 20)
print(hotel.name)
hotel.BookReservation("John", 205)
print(hotel.rooms[2][5])
print(hotel.rooms)